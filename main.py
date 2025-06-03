from pathlib import Path
import pandas as pd
from src.data_loader import load_raw_data
from src.data_processing import (
    add_delivery_days,
    filter_valid_deliveries,
    merge_orders_customers,
    get_top_selling_products,
    merge_reviews_with_delivery
)
from src.rfm_analysis import calculate_rfm, add_rfm_scores, run_kmeans


def main():
    print("🔄 Iniciando pipeline de dados Olist...")

    # Define os caminhos
    ROOT_DIR = Path(__file__).resolve().parent
    DATA_RAW_PATH = ROOT_DIR / 'data' / 'raw'
    DATA_PROCESSED_PATH = ROOT_DIR / 'data' / 'processed'
    DATA_PROCESSED_PATH.mkdir(exist_ok=True)

    # Carrega os dados
    print("📥 Carregando dados brutos...")
    raw_data = load_raw_data(DATA_RAW_PATH)

    # Processamento
    print("🧹 Limpando e processando dados...")
    orders = add_delivery_days(raw_data['orders'])
    orders_cleaned = filter_valid_deliveries(orders)
    orders_customers = merge_orders_customers(orders, raw_data['customers'], raw_data['payments'])
    products_top = get_top_selling_products(
        raw_data['items'], raw_data['products'], raw_data['category_translation']
    )
    reviews_delivery = merge_reviews_with_delivery(orders_cleaned, raw_data['reviews'])

    # 🔍 Análise RFM
    print("🔍 Iniciando análise RFM e clusterização...")
    rfm = calculate_rfm(orders_customers)
    rfm = add_rfm_scores(rfm)
    rfm = run_kmeans(rfm, n_clusters=4)

    # Exporta arquivos processados
    print("💾 Salvando arquivos em 'data/processed/'...")
    orders_cleaned.to_csv(DATA_PROCESSED_PATH / 'orders_cleaned.csv', index=False)
    orders_customers.to_csv(DATA_PROCESSED_PATH / 'orders_customers.csv', index=False)
    products_top.to_csv(DATA_PROCESSED_PATH / 'products_top10.csv', index=False)
    reviews_delivery.to_csv(DATA_PROCESSED_PATH / 'reviews_delivery.csv', index=False)
    rfm.to_csv(DATA_PROCESSED_PATH / 'rfm_clusters.csv', index=False)

    print("✅ Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    main()
