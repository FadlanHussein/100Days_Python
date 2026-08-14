import pathlib
import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

# Load Temperature Data
csv_path = pathlib.Path(__file__).parent / 'temperature_data.csv'
data = pd.read_csv(csv_path, parse_dates=['Date'])
# print(data.head())

# Plot Temperature Trend
plt.plot(data['Date'], data['Temperature'],label="temperature", marker='o')
plt.title('Temperature Trend')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.grid(True)
plt.legend()
plt.show()
