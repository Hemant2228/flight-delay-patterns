import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('flight_data.csv')  # Replace with your dataset path

# Data Cleaning
df = df.dropna(subset=['DepartureDelay', 'ScheduledDeparture', 'Airline', 'Distance'])  # Drop missing values
df['ScheduledDeparture'] = pd.to_datetime(df['ScheduledDeparture'])  # Convert to datetime
df = df[(df['DepartureDelay'] >= 0) & (df['DepartureDelay'] <= 500)]  # Filter unreasonable delays

# Add Hour Column
df['Hour'] = df['ScheduledDeparture'].dt.hour

# Average Delay by Hour of Day
hourly_avg_delay = df.groupby('Hour')['DepartureDelay'].mean()

# Plot 1: Average Delay by Hour of Day
plt.figure(figsize=(12, 6))
plt.plot(hourly_avg_delay, marker='o', color='blue')
plt.title('Average Departure Delay by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Delay (minutes)')
plt.grid()
plt.xticks(range(0, 24))
plt.show()

# Average Delay by Airline
airline_avg_delay = df.groupby('Airline')['DepartureDelay'].mean()

# Plot 2: Average Delay by Airline
plt.figure(figsize=(12, 6))
airline_avg_delay.sort_values().plot(kind='bar', color='skyblue')
plt.title('Average Delay by Airline')
plt.xlabel('Airline')
plt.ylabel('Average Delay (minutes)')
plt.xticks(rotation=45)
plt.grid()
plt.show()

# Delay vs Distance Scatter Plot
plt.figure(figsize=(12, 6))
plt.scatter(df['Distance'], df['DepartureDelay'], alpha=0.5, color='red')
plt.title('Departure Delay vs Distance')
plt.xlabel('Distance (miles)')
plt.ylabel('Departure Delay (minutes)')
plt.grid()
plt.show()

# Additional Analysis: Weather and Holiday (if applicable)
if 'WeatherCondition' in df.columns:
    weather_delay = df.groupby('WeatherCondition')['DepartureDelay'].mean()
    plt.figure(figsize=(8, 5))
    weather_delay.plot(kind='bar', color='orange')
    plt.title('Average Delay by Weather Condition')
    plt.xlabel('Weather Condition')
    plt.ylabel('Average Delay (minutes)')
    plt.grid()
    plt.show()

if 'Holiday' in df.columns:
    holiday_delay = df.groupby('Holiday')['DepartureDelay'].mean()
    plt.figure(figsize=(8, 5))
    holiday_delay.plot(kind='bar', color=['green', 'red'])
    plt.title('Average Delay: Holidays vs Non-Holidays')
    plt.xlabel('Holiday')
    plt.ylabel('Average Delay (minutes)')
    plt.grid()
    plt.show()

print("Analysis Complete!")
