#imports matplot and pandas modules
#sets aliases for each module for easy coding
import matplotlib.pyplot as plt
import pandas as pd

#creates 'dates' variable and assigns the value of the 'dates' 
#variable to be the dates in range of 04/24 to 14 days later
#periods=how often and freq=sets the period to days
dates = pd.date_range(start='2025-04-24', periods=14, freq='D')

#calculated temperatures from timeanddate.com
texas_temps = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
calif_temps = [1,3,5,7,9,11,13,15,17,19,21,23,25,27]

#creates a variable with the value of a pandas DataFrame that has it's value parameter set to
#the dictionary we created, the dictionary is the key-value pairs included in the {} brackets
df = pd.DataFrame({
    'Date': dates,
    'Texas': texas_temps,
    'California': calif_temps
})

#variable df is set to the DataFrame created above, the set_index() function
#assigns the index column as the date column
#inplace=True edits the original dataframe and does not create a new dataframe
df.set_index('Date', inplace=True)

#sets the size of the plot being created
plt.figure(figsize=(10, 5))

#assigns the dataframe index as the x axis and the state temps as the y axis
#label and color are keyword arguments
plt.plot(df.index, df['Texas'], label='Texas', color='red')
plt.plot(df.index, df['California'], label='California', color='blue')

#describes title, x label, y label, legend, and shows horizontal and vertical grid of plot
plt.title('Temperature Comparison: Texas vs. California')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.legend()
plt.grid(True)

#shows the plot
plt.show()