# src/config.py
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_RAW_PATH = ROOT_DIR / 'data' / 'raw'
DATA_PROCESSED_PATH = ROOT_DIR / 'data' / 'processed'
