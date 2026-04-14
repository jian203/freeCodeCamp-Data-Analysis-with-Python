import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # Create first line of best fit
    # Calculate regression for all data (1880 - most recent)
    res_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Create predicted x values from 1880 to 2050
    x_pred_1 = pd.Series(range(1880, 2051))
    # Calculate predicted y values
    y_pred_1 = res_1.intercept + res_1.slope * x_pred_1
    plt.plot(x_pred_1, y_pred_1, color='red')

    # Create second line of best fit
    # Filter data for years 2000 and beyond
    df_2000 = df[df['Year'] >= 2000]
    # Calculate new regression for data >= 2000
    res_2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    # Create predicted x values from 2000 to 2050
    x_pred_2 = pd.Series(range(2000, 2051))
    # Calculate predicted y values for the second line
    y_pred_2 = res_2.intercept + res_2.slope * x_pred_2
    plt.plot(x_pred_2, y_pred_2, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
