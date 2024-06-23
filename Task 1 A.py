import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'A': [1, 2, np.nan, 4, 5, np.nan, 7],
    'B': [np.nan, 2, 3, 4, np.nan, 6, 7],
    'C': [1, np.nan, np.nan, 4, 5, 6, 7],
    'D': [1, 2, 3, 4, 5, 6, 7]
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Identify missing data
print("\nMissing data (True indicates missing):")
print(df.isna())

# Drop rows with any missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Drop columns with any missing values
df_dropped_cols = df.dropna(axis=1)
print("\nDataFrame after dropping columns with missing values:")
print(df_dropped_cols)

# Fill missing values with a specific value (e.g., 0)
df_filled = df.fillna(0)
print("\nDataFrame after filling missing values with 0:")
print(df_filled)

# Fill missing values using a method (e.g., forward fill)
df_filled_ffill = df.fillna(method='ffill')
print("\nDataFrame after forward filling missing values:")
print(df_filled_ffill)

# Fill missing values using a method (e.g., backward fill)
df_filled_bfill = df.fillna(method='bfill')
print("\nDataFrame after backward filling missing values:")
print(df_filled_bfill)

# Create a DataFrame with duplicates
data_with_duplicates = {
    'A': [1, 2, 2, 4, 5, 5, 7],
    'B': [1, 2, 2, 4, 5, 5, 7],
    'C': [1, 2, 2, 4, 5, 5, 7],
    'D': [1, 2, 3, 4, 5, 6, 7]
}

df_with_duplicates = pd.DataFrame(data_with_duplicates)
print("\nDataFrame with duplicates:")
print(df_with_duplicates)

# Identify duplicate rows
print("\nDuplicate rows (True indicates duplicate):")
print(df_with_duplicates.duplicated())

# Remove duplicate rows
df_no_duplicates = df_with_duplicates.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_no_duplicates)
