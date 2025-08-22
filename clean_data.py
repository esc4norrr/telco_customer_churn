import pandas as pd

def clean_yes_no_columns(input_csv: str, output_csv: str | None = None) -> None:
    """Convert Yes/No values in select columns to 1/0 integers.

    Parameters
    ----------
    input_csv : str
        Path to the input CSV file.
    output_csv : str | None, optional
        Path to the output CSV file. If not provided, the input file is
        overwritten with the cleaned data.
    """
    df = pd.read_csv(input_csv)
    yes_no_columns = ["Partner", "PaperlessBilling", "Churn"]
    mapping = {"Yes": 1, "No": 0}
    df[yes_no_columns] = df[yes_no_columns].replace(mapping).astype(int)
    if output_csv is None:
        output_csv = input_csv
    df.to_csv(output_csv, index=False)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert Yes/No columns to 1/0.")
    parser.add_argument("input_csv", help="Path to input CSV file")
    parser.add_argument("-o", "--output-csv", dest="output_csv", help="Path to output CSV file")
    args = parser.parse_args()
    clean_yes_no_columns(args.input_csv, args.output_csv)
