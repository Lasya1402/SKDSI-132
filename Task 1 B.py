import pandas as pd
import numpy as np

# Define multi-level index (list of lists)
index = [['A', 'A', 'A', 'B', 'B', 'C', 'C', 'C'], [1, 2, 3, 1, 2, 1, 2, 3]]

# Create the Series
data = [1, 2, 3, 4, 5, 6, 7, 8]
multi_index = pd.MultiIndex.from_arrays(index, names=('outer', 'inner'))
series = pd.Series(data, index=multi_index)

print("Series with hierarchical indexing:")
print(series)

# Select data at the outer level
subset_outer_A = series['A']
print("\nSubset of data at outer level 'A':")
print(subset_outer_A)

subset_outer_B = series['B']
print("\nSubset of data at outer level 'B':")
print(subset_outer_B)

# Select data at the inner level for a specific outer level
subset_outer_A_inner_1 = series['A', 1]
print("\nData at outer level 'A' and inner level 1:")
print(subset_outer_A_inner_1)

subset_outer_B_inner_2 = series['B', 2]
print("\nData at outer level 'B' and inner level 2:")
print(subset_outer_B_inner_2)

# Select data using slicing
# Note: Slicing should be on sorted indices, ensure that the index is sorted
series = series.sort_index()

subset_outer_A_slice = series.loc['A'].loc[1:2]
print("\nData at outer level 'A' and inner levels 1 to 2:")
print(subset_outer_A_slice)

subset_outer_slice = series.loc['A':'B']
print("\nData at outer levels 'A' to 'B' and all inner levels:")
print(subset_outer_slice)
