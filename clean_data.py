import pandas as pd

def clean_telco_data(input_csv: str, output_csv: str) -> None:
    """Clean Telco churn dataset:
       - Convert Yes/No columns to 1/0
       - Fix TotalCharges as numeric
       - Drop rows with missing TotalCharges
       - Drop duplicate rows
    """
    df_raw = pd.read_csv(input_csv)
    df = df_raw.copy()

    # ---- Yes/No conversion ----
    def norm(v):
        return v.strip().lower() if isinstance(v, str) else v

    mapping = {"yes": 1, "no": 0}
    yes_no_columns = ["Partner", "PaperlessBilling", "Churn"]

    for col in yes_no_columns:
        if col not in df.columns:
            continue
        s = df[col].map(norm)
        mapped = s.map(mapping)
        df.loc[mapped.notna(), col] = mapped[mapped.notna()]
        df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    # ---- TotalCharges fix ----
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna(subset=["TotalCharges"])
    df = df.drop_duplicates()

    # ---- Save ----
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    input_file = "telco_customer_churn.csv"
    output_file = "telco_customer_churn_cleaned.csv"
    clean_telco_data(input_file, output_file)
    print(f"✅ Cleaned data saved to {output_file}")
