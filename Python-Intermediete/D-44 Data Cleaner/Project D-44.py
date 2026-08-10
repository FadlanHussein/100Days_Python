from pathlib import Path
import pandas as pd


def find_csv_files(base_dir: Path):
    """Return CSV files in the given folder, including .CSV variants."""
    csv_files = []
    csv_files.extend(sorted(base_dir.glob('*.csv')))
    csv_files.extend(sorted(base_dir.glob('*.CSV')))
    return csv_files


def load_data(file_path):
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully")
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None


def clean_data(df):
    """Clean the data."""
    print("\n---- Cleaning Data ----")
    print("Initial Shape:", df.shape)

    print("\nHandling Missing Values...")
    df = df.dropna()
    print("After removing missing values:", df.shape)
    return df


def save_data(df, output_path):
    """Save the cleaned data to a new CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print("Error saving data:", e)


def main():
    print("Welcome to the Data Cleaner Tool!")

    base_dir = Path(__file__).resolve().parent
    csv_files = find_csv_files(base_dir)

    if not csv_files:
        raise FileNotFoundError(f"Tidak ada file CSV di folder: {base_dir}")

    input_file = input("Enter the path to your CSV File (press Enter to use the default file): ").strip()
    if not input_file:
        input_file = str(csv_files[0])

    df = load_data(input_file)
    if df is None:
        return

    print("\n---- Initial Data ----")
    print(df.head())

    df = clean_data(df)

    output_file = input("\nEnter the path to save the cleaned CSV file: ").strip()
    if not output_file:
        output_file = str(base_dir / "cleaned_data.csv")

    save_data(df, output_file)


if __name__ == "__main__":
    main()