
import pandas as pd

file_path = "C:/Users/DELL/Documents/Python_ETL_mini_project/WDIData.csv"

def extract_data(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)
        print(f"Extraction successful: {df.shape}")
        return df
    except Exception as e:
        print(f"Extraction failed: {e}")
        raise
