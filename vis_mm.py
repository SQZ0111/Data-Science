#http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/how-pandas-uses-matplotlib-plus-figures-axes-and-subplots/
#gute Erklärungen zu plots
#weitere matplotlib beispiele https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots.html

#%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Seaborn visualization library
import seaborn as sns
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import pycountry_convert as pc

df=pd.read_excel('https://github.com/EnergizedTechLabsDo/energized/raw/master/All_Data_final.xlsx')

df.head()

# exploratory plots; is data complete?
plt.figure(figsize=(12, 4))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
plt.show()
sns.distplot(df["GDP"], color="purple", bins=10)
plt.show()

#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['CO2e per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("CO2 per Capita in t")
ax.set_title('World average CO2 per capita')
