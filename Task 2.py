import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure matplotlib uses a compatible backend
import matplotlib
matplotlib.use('TkAgg')  # or 'Agg' for non-GUI backend

# Task i: Histogram and Density Plot
# Sample data for plotting
data = np.random.randn(1000)  # Generate 1000 random numbers from a normal distribution

# Create a histogram
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, edgecolor='black', alpha=0.7)
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Create a density plot
plt.figure(figsize=(10, 5))
sns.kdeplot(data, fill=True)  # Updated to use fill=True instead of shade=True
plt.title('Density Plot of Data')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# Task ii: Scatter Plot
# Sample data for scatter plot
x = np.random.rand(100)
y = 2 * x + np.random.normal(0, 0.1, 100)

# Create a scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(x, y, alpha=0.7, edgecolors='w', linewidth=0.5)
plt.title('Scatter Plot of X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

# Task iii: Box Plots
# Sample data for box plots
data = {
    'Category': np.random.choice(['A', 'B', 'C', 'D'], size=100),
    'Value': np.random.randn(100)
}
df = pd.DataFrame(data)

# Create box plots
plt.figure(figsize=(10, 5))
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Box Plots of Value by Category')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()
