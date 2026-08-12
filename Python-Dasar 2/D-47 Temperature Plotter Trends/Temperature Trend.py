import pathlib
import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

# Load Temperature Data
csv_path = pathlib.Path(__file__).parent / 'temperature_data.csv'
data = pd.read_csv(csv_path, parse_dates=['Date'])
print(data.head())

# Add rolling average coloumn
data["7-Day Average"] = data['Temperature'].rolling(window=7).mean()


plt.plot(data["Date"], data["7-Day Average"], label="7-Day Average", linestyle="--")
plt.title("Temperature Trend with 7-Day Average")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.legend()
plt.grid(True)
plt.show()