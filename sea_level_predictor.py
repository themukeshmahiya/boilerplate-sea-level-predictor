import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    df.columns = ['year', 'csiro', 'lower-bound', 'upper-bound', 'noaa']


    # Create scatter plot
    df.plot.scatter(x='year', y='csiro', color='black', label='Original data')


    # Create first line of best fit
    line1 = linregress(df['year'], df['csiro'])
    x1 = np.arange(df['year'].min(), 2051)
    plt.plot(x1, (line1.intercept + line1.slope * x1), color='red', label='Line of best fit', linestyle='-', linewidth=3)

    # Create second line of best fit
    sub_df = df[df['year'] >= 2000]
    line2 = linregress(sub_df['year'], sub_df['csiro'])
    x2 = np.arange(2000, 2051)
    plt.plot(x2, (line2.intercept + line2.slope * x2), color='cyan', label='Line of best fit from year 2000', linestyle='--', linewidth=2)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png', dpi=300)
    return plt.gca()