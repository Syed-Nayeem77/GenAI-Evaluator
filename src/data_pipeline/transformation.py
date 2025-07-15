import pandas as pd
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class DataTransformer:
    """Transforms raw data into evaluation-ready format"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Basic text cleaning"""
        if not isinstance(text, str):
            return ""
        return text.strip()
    
    def transform(self, df: pd.DataFrame) -> Optional[pd.DataFrame]:
        """Apply transformations to dataframe"""
        try:
            # Example transformations
            if 'text' in df.columns:
                df['text'] = df['text'].apply(self.clean_text)
            return df
        except Exception as e:
            logger.error(f"Transformation failed: {str(e)}")
            return None
