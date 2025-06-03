from pathlib import Path
import pandas as pd

def load_raw_data(base_path: Path) -> dict:
    return {
        'orders': pd.read_csv(base_path / 'olist_orders_dataset.csv', parse_dates=[
            'order_purchase_timestamp', 'order_approved_at',
            'order_delivered_carrier_date', 'order_delivered_customer_date',
            'order_estimated_delivery_date'
        ]),
        'customers': pd.read_csv(base_path / 'olist_customers_dataset.csv'),
        'items': pd.read_csv(base_path / 'olist_order_items_dataset.csv'),
        'payments': pd.read_csv(base_path / 'olist_order_payments_dataset.csv'),
        'products': pd.read_csv(base_path / 'olist_products_dataset.csv'),
        'reviews': pd.read_csv(base_path / 'olist_order_reviews_dataset.csv'),
        'sellers': pd.read_csv(base_path / 'olist_sellers_dataset.csv'),
        'category_translation': pd.read_csv(base_path / 'product_category_name_translation.csv')
    }
