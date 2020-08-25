import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression

filename_energy = 'additional_data/energy_use_per_person.csv'
energy = pd.read_csv(filename_energy, header = 0, index_col = 0)
energy.drop(columns = '2015', axis = 1, inplace = True)
energy = energy.reset_index(drop = True).transpose()
energy.columns = energy.iloc[0]
energy = energy[1:-1]

filename_co2 = 'additional_data/co2_emissions_tonnes_per_person.csv'
co2 = pd.read_csv(filename_co2, header = 0, index_col = 0)
co2 = co2.reset_index().transpose()
co2.columns = co2.iloc[0]
co2 = co2[1:-1]

# Setting up a unique color palette for plotting
colors = ["#527BAB", "#164278" , "#81DCDE", "#F7BC8D" , "#E67350", "#AB5A52"]
palette = sns.color_palette(colors)

slopes = []
r_val = []

# Plotting
timerange = range(1960, 2013)
for year in timerange:
    year = str(year)
    x_values = energy.loc[year,:]
    x_values.dropna(inplace = True)
    # Adjust the x-scale to have similar x and y-scales and a slope close to 1
    x_values = x_values/1000
    y_values = co2.loc[year, :]
    y_values.dropna(inplace = True)
    # Filter series and keep only values with the same index
    for index in x_values.index:
        if index not in y_values.index:
            x_values.drop(index=index, inplace=True)
    for index in y_values.index:
        if index not in x_values.index:
            y_values.drop(index=index, inplace=True)

    # Creating a plot of each year: energy use per capita vs co2 emissions per capita
    fig = plt.figure(0)
    # Using lists as input, because the dataframe or pandas series do not work for some reason
    reg = sns.regplot(x = list(x_values), y = list(y_values), scatter_kws = {"color": colors[0]}, line_kws = {"color": colors[4]})
    reg.set(xlabel='Energy consumption [MWh/cap]', ylabel='CO2e [t/cap]')
    reg.set_title(str(year))
    reg.axis([0, 250, 0, 100])
    # Automatic annotation of interesting countries
    y_distance = 1
    countries_of_interest = ['Germany', 'Iceland', 'Qatar', 'Trinidad and Tobago']
    for country in countries_of_interest:
        try:
            reg.text(x_values[country], y_values[country] - y_distance, country, horizontalalignment='center', size='small', color='black', weight='normal')
        except:
            continue

    # Finding the slope via RegressionModel
    print('Creating LinearRegressionModel for ' + year + ' ...')
    x_values = np.array(x_values).reshape(-1, 1)
    y_values = np.array(y_values).reshape(-1, 1)
    lr = LinearRegression()
    lr.fit(x_values, y_values)
    # Recieving the specific values of the linear function: slope, y-intercept and mean squarred error
    intercept = lr.intercept_[0]
    slope = lr.coef_[0][0]
    r_sq = lr.score(x_values, y_values)
    equation = "slope : " + str(round(slope,3)) + "\nconfidence : " + str(round(r_sq, 3))
    # Adding the equation of the function to the plot
    reg.text(5, 90, equation, horizontalalignment = 'left', size='medium', color='black', weight='normal')
    # Saving the slope and the MSE for later use
    slopes.append(slope)
    r_val.append(r_sq)
    # Save the figure as a .png
    print('Saving plot of ' + year + '.')
    fig.savefig('plots/energy_use_per_person_vs_co2/energy_use_per_person_vs_co2_' + year + '.png', dpi = 300)
    # Closing the plot to make sure the screen gets not flooded with 53 windows
    plt.close(0)

# Creating a new figure for all determined slope values of the LinearRegression
fig_2 = plt.figure()
lineplot = sns.lineplot(x = timerange, y = slopes, palette = palette)
lineplot.set(xlabel='time [y]', ylabel='CO2e [t/MWh]')
lineplot.set_title("Emitted CO2 per energy unit")
fig_2.savefig('plots/co2_emitted_per_MWh_since_1960.png', dpi = 300)

# Saving the new data as .csv
export = pd.DataFrame({'year': timerange, 't_co2 per MWh world': slopes})
export.to_csv('t_co2_per_MWh_world.csv')
