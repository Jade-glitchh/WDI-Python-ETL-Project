import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    year_cols = [col for col in df.columns if col.isdigit()]
    df_long = df.melt(
        id_vars=[
            "country_name",
            "country_code",
            "indicator_name",
            "indicator_code"
        ],
        value_vars=year_cols,
        var_name="year",
        value_name="value"
    )
    df_long["year"] = df_long["year"].astype(int)
    df_long["value"] = pd.to_numeric(df_long["value"], errors="coerce")

    df_long = df_long.dropna(subset=["value"])

    df_long = df_long.drop_duplicates()

    print(f"Transformation successful: {df_long.shape}")

    return df_long
