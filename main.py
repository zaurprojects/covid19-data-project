import matplotlib.pyplot as plt
import pandas as pd

# Load the COVID-19 dataset
data = pd.read_csv("owid-covid-data.csv")

# Display basic info about the dataset
print(data.info())
print(data.head())

# Filter data for a specific country (e.g., Germany)
germany_data = data[data['location'] == 'Germany']

# Convert 'date' to a datetime object
germany_data['date'] = pd.to_datetime(germany_data['date'])

# Plot new cases over time
plt.figure(figsize=(10, 6))
plt.plot(germany_data['date'], germany_data['new_cases'], label='New Cases')
plt.title("COVID-19 New Cases in Germany")
plt.xlabel("Date")
plt.ylabel("Number of New Cases")
plt.legend()
plt.grid()
plt.show()
