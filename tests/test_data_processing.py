import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

import pandas as pd
from src.data_processing import (
    add_delivery_days,
    filter_valid_deliveries,
    merge_orders_customers
)

def test_add_delivery_days():
    df = pd.DataFrame({
        'order_purchase_timestamp': pd.to_datetime(['2021-01-01']),
        'order_delivered_customer_date': pd.to_datetime(['2021-01-05'])
    })
    result = add_delivery_days(df.copy())
    assert 'delivery_days' in result.columns
    assert result['delivery_days'].iloc[0] == 4

def test_filter_valid_deliveries():
    df = pd.DataFrame({'delivery_days': [5, -1, None]})
    filtered = filter_valid_deliveries(df)
    assert len(filtered) == 1
    assert filtered['delivery_days'].iloc[0] == 5

def test_merge_orders_customers():
    orders = pd.DataFrame({'order_id': [1], 'customer_id': ['c1']})
    customers = pd.DataFrame({'customer_id': ['c1'], 'customer_state': ['SP']})
    merged = merge_orders_customers(orders, customers)
    assert 'customer_state' in merged.columns
    assert merged.iloc[0]['customer_state'] == 'SP'
