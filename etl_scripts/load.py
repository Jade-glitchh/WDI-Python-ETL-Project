from sqlalchemy import create_engine
import pandas as pd

def load_data(df: pd.DataFrame, table_name: str):
    try:
        engine = create_engine(
            "postgresql://postgres@localhost:5432/etl_db"
            )
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace", # dev mode
            index=False
            )
        
        print(f"Loaded into table: {table_name}")
    except Exception as e:
        print(f"Load failed: {e}")
        raise
