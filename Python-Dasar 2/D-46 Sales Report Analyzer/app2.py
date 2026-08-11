from pathlib import Path
import pandas as pd

# Load Sales Data
file_path = Path(__file__).parent / 'sales_data.csv'
data = pd.read_csv(file_path)
print(data.head())

# Summary Data
print("\n=== Summary Statistics ===\n")
print(data.info())

# Statistical Data
print("\nStatistical Data")
print(data.describe())

# Check for Missing Values
print(data.isnull().sum())

# Fill Missing Values
data["product"] = data["product"].fillna("Unknown")

# Drop Rows with Missing Values
data = data.dropna()

# Fill Missing Values with 0
data = data.fillna(0)
print(data.isnull().sum())

# Convert Data Coloumn to Dateline
data["date"] = pd.to_datetime(data["date"])
print(data.info())

data["total_price"] = pd.to_numeric(data["total_price"])
print(data.info())

# Get Total Sales Data
total_sales = data["total_price"].sum()
print(f"Total Sales: Rp{total_sales:,}")

# Get Average Sales Data
average_sales = data["total_price"].mean()
print(f"Average Sales: Rp{average_sales:,}")

# Get Max Sales Data
max_sales = data["total_price"].max()
print(f"Max Sales: Rp{max_sales:,}")

# Get Min Sales Data
min_sales = data["total_price"].min()
print(f"Min Sales: Rp{min_sales:,}")

# Get Total Quantity
total_quantity = data["quantity"].sum()
print(f"Total Quantity: {total_quantity:,}")

# Get Average Quantity
average_quantity = data["quantity"].mean()
print(f"Average Quantity: {average_quantity:,}")

# Get Max Quantity
max_quantity = data["quantity"].max()
print(f"Max Quantity: {max_quantity:,}")

# Get Min Quantity
min_quantity = data["quantity"].min()
print(f"Min Quantity: {min_quantity:,}")

# Get Total Revenue
total_revenue = data["total_price"].sum()
print(f"Total Revenue: Rp{total_revenue:,}")

# Get Average Revenue
average_revenue = data["total_price"].mean()
print(f"Average Revenue: Rp{average_revenue:,}")

# Get Max Revenue
max_revenue = data["total_price"].max()
print(f"Max Revenue: Rp{max_revenue:,}")

# Get Min Revenue
min_revenue = data["total_price"].min()
print(f"Min Revenue: Rp{min_revenue:,}")

# Get Total Revenue
total_revenue = data["total_price"].sum()
print(f"Total Revenue: Rp{total_revenue:,}")