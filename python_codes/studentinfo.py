import pandas as pd

# Read the CSV file
df = pd.read_csv("students.csv")

# Display the first 10 records
print("First 10 Records:")
print(df.head(10))