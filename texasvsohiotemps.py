import matplotlib.pyplot as plt
import pandas as pd

# Example date range
dates = pd.date_range(start='2025-04-24', periods=14, freq='D')

# Example temperatures
texas_temps = [72, 77, 81, 79, 79, 82, 72, 79, 68, 73, 75, 64, 70, 75]
ohio_temps = [84, 75, 66, 66, 79, 81, 73, 77, 75, 63, 63, 55, 70, 73]

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Texas': texas_temps,
    'Ohio': ohio_temps
})

# Set Date as index
df.set_index('Date', inplace=True)

plt.figure(figsize=(10, 5))

# Plot Texas
plt.plot(df.index, df['Texas'], label='Texas', color='red')

# Plot Ohio
plt.plot(df.index, df['Ohio'], label='Ohio', color='blue')

# Add labels and legend
plt.title('Temperature Comparison: Texas vs. Ohio')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()