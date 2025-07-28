import pandas as pd

# Load CSV
df = pd.read_csv("sales_data.csv")

# First 5 rows
print("First 5 rows of the dataset:\n", df.head())

# Total sales
total_sales = df['Sales'].sum()
print("\nTotal Sales Amount:", total_sales)

# Average sales per region
avg_sales_region = df.groupby('Region')['Sales'].mean()
print("\nAverage Sales per Region:\n", avg_sales_region)

# Region with highest average sales
top_region = avg_sales_region.idxmax()
top_value = avg_sales_region.max()
print(f"\nRegion with Highest Average Sales: {top_region} (${top_value})")
