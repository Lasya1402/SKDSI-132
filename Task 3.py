import pandas as pd
import numpy as np

# Task i: Create time series using datetime object in pandas indexed by timestamps
dates = pd.date_range(start='2023-01-01', periods=10, freq='D')
data = np.random.randn(10)
time_series = pd.Series(data, index=dates)
print("Time Series Indexed by Timestamps:")
print(time_series)

# Task ii: Use pandas.date_range to generate a DatetimeIndex with an indicated length
date_index = pd.date_range(start='2023-01-01', periods=5, freq='h')
print("\nDatetimeIndex with Indicated Length:")
print(date_index)

# Task iii: Time zone operations
# Generate a DatetimeIndex and set time zone
date_index_tz = pd.date_range(start='2023-01-01', periods=5, freq='D', tz='UTC')
print("\nDatetimeIndex with Time Zone (UTC):")
print(date_index_tz)

# Localize time zone
localized_time_series = time_series.tz_localize('UTC')
print("\nLocalized Time Series to UTC:")
print(localized_time_series)

# Convert to a different time zone
converted_time_series = localized_time_series.tz_convert('US/Eastern')
print("\nTime Series Converted to US/Eastern Time Zone:")
print(converted_time_series)

# Combine two different time zones
combined = pd.concat([localized_time_series, converted_time_series], axis=1)
combined.columns = ['UTC', 'US/Eastern']
print("\nCombined Time Series with Different Time Zones:")
print(combined)

# Task iv: Period arithmetic
# Create a Period object
period = pd.Period('2023-01', freq='M')

# Add and subtract integers from periods
added_period = period + 1
subtracted_period = period - 2
print("\nOriginal Period:")
print(period)
print("Period After Adding 1 Month:")
print(added_period)
print("Period After Subtracting 2 Months:")
print(subtracted_period)

# Construct a range of periods using period_range
period_range = pd.period_range(start='2023-01', periods=5, freq='M')
print("\nRange of Periods:")
print(period_range)
