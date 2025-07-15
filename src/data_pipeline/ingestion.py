import pandas as pd
from pathlib import Path
from typing import Optional, Union
import json
import logging

logger = logging.getLogger(__name__)

class DataIngestor:
    """Handles data ingestion from various file formats"""
    
    @staticmethod
    def ingest(file_path: Union[str, Path]) -> Optional[pd.DataFrame]:
        """Ingest data from file"""
        file_path = Path(file_path)
        try:
            if file_path.suffix == '.csv':
                return pd.read_csv(file_path)
            elif file_path.suffix == '.json':
                return pd.read_json(file_path, orient='records')
            elif file_path.suffix == '.parquet':
                return pd.read_parquet(file_path)
            else:
                logger.error(f"Unsupported file format: {file_path.suffix}")
                return None
        except Exception as e:
            logger.error(f"Failed to ingest {file_path}: {str(e)}")
            return None
