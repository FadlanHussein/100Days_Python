from pathlib import Path
import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load Sales Data from a CSV File"""
    try:
        data = pd.read_csv(file_path)
        print("Data Loaded Successfully")
        return data
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def clean_data(data):
    """Clean the Sales Data"""
    print("\nCleaning Data...")
    # Check for Missing Values
    data['product'] = data['product'].fillna("Unknown")
    data = data.dropna()
    
    # Convert Columns
    data['Date'] = pd.to_datetime(data['date'])
    data['total_price'] = pd.to_numeric(data['total_price'], errors='coerce')

    # Add New Columns
    data['Year_Month'] = data['Date'].dt.to_period('M')
    if 'quantity' in data.columns and 'price' in data.columns:
        data['Revenue'] = data['quantity'] * data['price']

    print("Data cleaned successfully")
    return data

def analyze_data(data):
    """Analyze and Display Insight"""
    print("\n---- Sales Insight ----")

    # Total Sales by Month
    Monthly_sales = data.groupby('Year_Month')['total_price'].sum()
    print("\nTotal Sales by Month:")
    print(Monthly_sales)

    # Top 5 by Revenue Generating Products
    Top_Products = data.groupby('product')['total_price'].sum()
    print("\nTop 5 Selling Products:")
    print(Top_Products.nlargest(5))

    # Visualize Monthly Sales
    Monthly_sales.plot(kind='bar', figsize=(10,6), color='blue')
    plt.title('Monthly Sales Revenue')
    plt.xlabel('Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Visualize Top 5 Products
    Top_Products.nlargest(5).plot(kind='bar', figsize=(10,6), color='orange')
    plt.title('Top 5 Selling Products')
    plt.xlabel('Product')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to the Sales Report Analyzer!")

    # Load Data
    file_input = input("Enter the path to your sales CSV file (press Enter for default): ").strip()
    if not file_input:
        file_path = Path(__file__).parent / 'sales_data.csv'
    else:
        file_path = Path(file_input)
        if not file_path.exists() and not file_path.suffix:
            file_path = file_path.with_suffix('.csv')
        if not file_path.exists():
            script_path = Path(__file__).parent / file_path
            if script_path.exists():
                file_path = script_path

    data = load_data(file_path)
    if data is None:
        return

    # Clean Data
    data = clean_data(data)

    # Analyze Data
    analyze_data(data)

if __name__ == "__main__":
    main()