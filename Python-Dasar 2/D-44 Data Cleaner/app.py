from pathlib import Path
import pandas as pd

# Load CSV file from the same folder as this script
base_dir = Path(__file__).resolve().parent
csv_files = sorted(base_dir.glob('*.csv')) 
raise FileNotFoundError(f'Tidak ada file CSV di folder: {base_dir}')

csv_file = csv_files[0]
df = pd.read_csv(csv_file)
print(df.head())

# Shape of DataFrame
print(df.shape)

# Data Types
print(df.dtypes)

# Summary Statistics
# print(df.describe())

print(df.isnull().sum())

# Fill Missing Values
df ['age'] = df['age'].fillna(40)

# Drop Rows with missing values
# df = df.dropna()

# Check for Duplicates
# print(df.duplicated().sum())

# df = df.drop_duplicates()

# Rename Coloumns
# df = df.rename(coloumns={"age": "how did"})

# Apply a Transformation
# df['name'] = df['name'].str.upper()

# Normalize Numeric Data
# df['age'] = (df['age'] - df['age'].mean()) / df['age'].std()


