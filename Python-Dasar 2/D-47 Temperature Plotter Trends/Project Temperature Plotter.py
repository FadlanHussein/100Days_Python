import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
import pathlib

# Load Data
def load_data(file_path):
    """Load temperature data from a CSV File."""
    try:
        data = pd.read_csv(file_path, parse_dates=["Date"])
        print("Data Loaded Successfully")
        return data
    except FileNotFoundError:
        print("File not found")
        return None

def plot_temperature(data, save_file=None):
    """Plot temperature trends with options for rolling average and anomalies."""
    # Add Rolling Average
    data["7-Day Average"] = data["Temperature"].rolling(window=7).mean()

    # Identify Anomalies
    mean_temp = data["Temperature"].mean()
    std_temp = data["Temperature"].std()
    data["Anomaly"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)
    
    # Plot Temperature Trend
    plt.style.use("seaborn-v0_8-whitegrid")
    plt.figure(figsize=(12, 6))
    plt.plot(data["Date"], data["Temperature"], label="Temperature", marker="o")
    plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--")
    plt.scatter(data[data["Anomaly"]]["Date"], data[data["Anomaly"]]["Temperature"], label="Anomaly", color="red")
    plt.title("Temperature Trend with Anomalies")
    plt.xlabel("Date")
    plt.ylabel("Temperature (C)")
    plt.legend()
    plt.grid(True)
    

    # Save or Show Plot
    if save_file:
        plt.savefig(save_file)
        print("Plot saved to", save_file)
    else:
        plt.show()

def main():
    print("Temperature Trend Plotter")
    print("=" * 30)

    # Load Data
    file_path = pathlib.Path(__file__).parent / 'temperature_data.csv'
    data = load_data(file_path)
    if data is None:
        return

    analyze_temperature(data)

    # Plot Temperature
    save_choice = input("Do you want to save the plot? (yes/no): ").lower()
    if save_choice == "yes":
        file_name = input("Enter the file name (e.g., temperature_plot.png): ")
        plot_temperature(data, save_file=file_name)
    else:
        plot_temperature(data)
    

def analyze_temperature(data):
    """Performs in-depth analysis of temperature data."""
    print("\n=== Temperature Analysis ===")

    # Calculate basic statistics
    print(data["Temperature"].describe())

if __name__== "__main__":
    main()
    
    