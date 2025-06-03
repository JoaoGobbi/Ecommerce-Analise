from pathlib import Path
import pandas as pd
import numpy as np
import os
import sys
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Para importar config de fora da pasta /src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.config import DATA_PROCESSED_PATH

def calculate_rfm(df: pd.DataFrame) -> pd.DataFrame:
    snapshot_date = df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

    rfm = df.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (snapshot_date - x.max()).days,
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index()

    rfm.columns = ['customer_unique_id', 'Recencia', 'Frequencia', 'Valor']
    return rfm


def add_rfm_scores(rfm: pd.DataFrame) -> pd.DataFrame:
    rfm['R_Score'] = pd.qcut(rfm['Recencia'], 4, labels=[4,3,2,1])
    rfm['F_Score'] = pd.qcut(rfm['Frequencia'].rank(method="first"), 4, labels=[1,2,3,4])
    rfm['V_Score'] = pd.qcut(rfm['Valor'], 4, labels=[1,2,3,4])

    rfm['RFM_Score'] = (
        rfm['R_Score'].astype(str) +
        rfm['F_Score'].astype(str) +
        rfm['V_Score'].astype(str)
    )
    return rfm


def run_kmeans(rfm: pd.DataFrame, n_clusters=4) -> pd.DataFrame:
    features = rfm[['R_Score', 'F_Score', 'V_Score']].astype(int)
    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    rfm['Cluster'] = kmeans.fit_predict(scaled)

    return rfm


def main():
    print("🔍 Executando análise RFM...")

    # Carregar dados processados
    orders_customers = pd.read_csv(DATA_PROCESSED_PATH / 'orders_customers.csv', parse_dates=['order_purchase_timestamp'])

    rfm = calculate_rfm(orders_customers)
    rfm = add_rfm_scores(rfm)
    rfm = run_kmeans(rfm, n_clusters=4)
    
    # Garantir que o diretório existe
    DATA_PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

    # Salvar o arquivo
    rfm.to_csv(DATA_PROCESSED_PATH / 'rfm_clusters.csv', index=False)


if __name__ == "__main__":
    main()
