
from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    file_path = "C:/Users/DELL/Documents/Python_ETL_mini_project/WDIData.csv"
    db_url = "postgresql://postgres@localhost:5432/etl_db"
    
    raw_df = extract_data(file_path)
    clean_df = transform_data(raw_df)
    load_data(clean_df, db_url)

if __name__ == "__main__":
    main()
