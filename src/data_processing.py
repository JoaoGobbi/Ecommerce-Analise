import pandas as pd

def add_delivery_days(orders: pd.DataFrame) -> pd.DataFrame:
    orders['delivery_days'] = (
        orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']
    ).dt.days
    return orders

def filter_valid_deliveries(orders: pd.DataFrame) -> pd.DataFrame:
    return orders[
        (orders['delivery_days'].notnull()) &
        (orders['delivery_days'] > 0) &
        (orders['delivery_days'] < 100)  # ajuste esse limite conforme necessário
    ]

def merge_orders_customers(orders: pd.DataFrame, customers: pd.DataFrame, payments: pd.DataFrame) -> pd.DataFrame:
    # Agrupa pagamentos por pedido
    payments_agg = payments.groupby('order_id', as_index=False).agg({
        'payment_value': 'sum',
        'payment_installments': 'max',
        'payment_type': lambda x: ', '.join(set(x))  # caso tenha mais de um tipo por pedido
    })
    
    # Merge com customers e payments
    merged = pd.merge(orders, customers, on='customer_id')
    merged = pd.merge(merged, payments_agg, on='order_id', how='left')
    return merged

def get_top_selling_products(items: pd.DataFrame, products: pd.DataFrame, translation: pd.DataFrame, top_n=10) -> pd.DataFrame:
    vendas = items.groupby('product_id')['order_id'].count().reset_index()
    top_vendas = vendas.sort_values(by='order_id', ascending=False).head(top_n)
    merged = pd.merge(top_vendas, products, on='product_id', how='left')
    merged = pd.merge(merged, translation, on='product_category_name', how='left')
    return merged

def merge_reviews_with_delivery(orders: pd.DataFrame, reviews: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(orders[['order_id', 'delivery_days']], reviews, on='order_id', how='inner')
