import pandas as pd

# Load the raw data
df = pd.read_csv('data/raw_data.csv')

# Drop rows with missing values
df = df.dropna()

# Add a column to indicate if the flight occurred during peak hours
def is_peak_hour(hour):
    return 1 if 7 <= hour < 9 or 17 <= hour < 19 else 0

df['Date'] = pd.to_datetime(df['Date'])
df['Hour'] = df['Date'].dt.hour
df['is_peak_hour'] = df['Hour'].apply(is_peak_hour)

# Save the cleaned data
df.to_csv('data/cleaned_data.csv', index=False)
print("Data cleaned and saved to data/cleaned_data.csv")

