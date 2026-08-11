from pathlib import Path
import pandas as pd

# Load sales data
file_path = Path(__file__).parent / 'sales_data.csv'
data = pd.read_csv(file_path)
print(data.head())

