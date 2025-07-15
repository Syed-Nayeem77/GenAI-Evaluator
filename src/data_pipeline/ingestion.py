import pandas as pd
from pathlib import Path
from typing import Optional
from src.utils.logging import get_logger

logger = get_logger(__name__)

class DataIngestor:
    def __init__(self, raw_data_dir: Path):
        self.raw_data_dir = raw_data_dir
        
    def ingest_json(self, file_path: Path) -> Optional[pd.DataFrame]:
        try:
            logger.info(f"Ingesting JSON file: {file_path}")
            df = pd.read_json(file_path, orient='records')
            logger.info(f"Successfully ingested {len(df)} records")
            return df
        except Exception as e:
            logger.error(f"Failed to ingest {file_path}: {str(e)}")
            return None
            
    def ingest_csv(self, file_path: Path) -> Optional[pd.DataFrame]:
        try:
            logger.info(f"Ingesting CSV file: {file_path}")
            df = pd.read_csv(file_path)
            logger.info(f"Successfully ingested {len(df)} records")
            return df
        except Exception as e:
            logger.error(f"Failed to ingest {file_path}: {str(e)}")
            return None
