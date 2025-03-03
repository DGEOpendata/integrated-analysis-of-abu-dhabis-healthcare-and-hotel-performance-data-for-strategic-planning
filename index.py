python
import pandas as pd

# Load healthcare dataset
healthcare_data = pd.read_csv('Abu_Dhabi_Healthcare_Utilization_2020_2023.csv')

# Load hotel performance dataset
hotel_data = pd.read_excel('Abu_Dhabi_Hotel_Performance_2019_2021.xlsx')

# Example analysis: Correlate hospital visits with hotel occupancy rates
healthcare_monthly = healthcare_data.groupby(['Year', 'Month']).agg({'PatientVisits': 'sum'}).reset_index()
hotel_monthly = hotel_data.groupby(['Year', 'Month']).agg({'OccupancyRate': 'mean'}).reset_index()

# Merge datasets on Year and Month
merged_data = pd.merge(healthcare_monthly, hotel_monthly, on=['Year', 'Month'])

# Correlation analysis
correlation = merged_data['PatientVisits'].corr(merged_data['OccupancyRate'])
print(f'Correlation between patient visits and hotel occupancy rates: {correlation}')

# Visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(merged_data['Month'], merged_data['PatientVisits'], label='Patient Visits', marker='o')
plt.plot(merged_data['Month'], merged_data['OccupancyRate'], label='Hotel Occupancy Rate', marker='x')
plt.title('Healthcare Utilization vs Hotel Occupancy Rates')
plt.xlabel('Month')
plt.ylabel('Count/Rate')
plt.legend()
plt.show()
