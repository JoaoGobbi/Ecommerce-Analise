import sys
from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT_DIR))

from src.data_loader import load_raw_data

def test_load_raw_data():
    base_path = ROOT_DIR / 'data' / 'raw'
    data = load_raw_data(base_path)

    expected_keys = [
        'orders', 'customers', 'items', 'payments',
        'products', 'reviews', 'sellers', 'category_translation'
    ]
    
    for key in expected_keys:
        assert key in data
        assert not data[key].empty
