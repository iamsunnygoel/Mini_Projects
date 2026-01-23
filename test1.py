import pandas as pd

# Replace this path with the actual path to your CSV file
file_path = '/Users/goels2/Downloads/Mutual_Fund_performances_22_06_2025.csv'

# Load the CSV into a DataFrame
df = pd.read_csv(file_path)

# Print the first 5 rows
#print(df.head())

print(df.info())
#print(df.describe())
