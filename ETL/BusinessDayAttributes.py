import pandas as pd
from datetime import datetime
import os

# Define the dataset folder path
dataset_folder = os.path.join(os.path.dirname(__file__), '..', 'dataset')
csv_file = os.path.join(dataset_folder, 'sales_transactions.csv')

# Read the CSV file
df = pd.read_csv(csv_file)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract day of week (0=Monday, 6=Sunday)
df['day_of_week'] = df['date'].dt.dayofweek

# Get day name (Monday, Tuesday, etc.)
df['day_name'] = df['date'].dt.day_name()

# Capture unique combinations of date and day of week
unique_combinations = df[['date', 'day_of_week', 'day_name']].drop_duplicates().sort_values('date')

# Display the results
print("Unique combinations of date and day of week:")
print(unique_combinations)

# Optionally, save to a new CSV file
output_file = os.path.join(dataset_folder, 'business_day_attributes.csv')
unique_combinations.to_csv(output_file, index=False)
print(f"\nUnique combinations saved to {output_file}")
