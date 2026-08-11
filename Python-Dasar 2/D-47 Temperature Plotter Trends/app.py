import pandas as pd

# Load Temperature Data
data = pd.read_csv('temperature.csv', parse_dates=['Date'])
print(data.head())
