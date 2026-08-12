import pathlib
import pandas as pd
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

# Load Temperature Data
csv_path = pathlib.Path(__file__).parent / 'temperature_data.csv'
data = pd.read_csv(csv_path, parse_dates=['Date'])
print(data.head())


# Identify Anomalies
mean_temp = data["Temperature"].mean()
std_temp = data["Temperature"].std()
data["Anomaly"] = (data["Temperature"] > mean_temp + 2 * std_temp) | (data["Temperature"] < mean_temp - 2 * std_temp)

# Plot with Anomalies 
plt.plot(data["Date"], data["Temperature"], label=" Daily Temperature", color="blue")
anomalies = data[data["Anomaly"]]
plt.scatter(anomalies["Date"], anomalies["Temperature"], label="Anomaly", color="red")
plt.title("Temperature Trend with Anomalies")
plt.xlabel("Date")
plt.ylabel("Temperature (C)")
plt.legend()
plt.grid(True)
plt.show()