#!/usr/bin/env python
# coding: utf-8

#http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/how-pandas-uses-matplotlib-plus-figures-axes-and-subplots/
#gute Erklärungen zu plots
#weitere matplotlib beispiele https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots.html

get_ipython().run_line_magic('matplotlib', 'inline')
#%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Seaborn visualization library
import seaborn as sns
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import pycountry_convert as pc

df=pd.read_excel('https://github.com/EnergizedTechLabsDo/energized/raw/master/All_Data_final.xlsx')
df.head()

df["Entity"].drop_duplicates()


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
ax.set_title('World average CO2 per capita in [t]')
plt.show()

# ## line plot
#durchschnittlicher hydro power production per capita über alle Jahre
ax=df.groupby('Year')['Hydro power production per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("Hydro power production per capita [?]")
ax.set_title('Hydro power production per capita in [?]')
plt.show()

#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['Energy use per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("Energy use per capita in [?]")
ax.set_title('Energy use per capita in [?]')
plt.show()

#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['Oil consumption per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("Oil consumption per capita in [?]")
ax.set_title('World average oil consumption per capita in [?]')
plt.show()


df.boxplot(column=['CO2e per capita'], by=['Year'],figsize=(15,10))
plt.show()


#country_code = pc.country_name_to_country_alpha2("Sweden", cn_name_format="default")
#print(country_code)
#continent_name = pc.country_alpha2_to_continent_code(country_code)
#print(continent_name)


#hinzufügen von continent codes
codes=[]

for value in df["Entity"]:
    country_code = pc.country_name_to_country_alpha2(value, cn_name_format="default")
    continent_name = pc.country_alpha2_to_continent_code(country_code)
    codes.append(continent_name)


df["Continent Code"]=codes
df['Continent Code'].unique()
continente=df.groupby(['Continent Code','Year'])['CO2e per capita'].mean()
test=continente.to_frame()
test.reset_index(inplace=True)

# erstelung des area plots und der dfs für die darstellung

x=df['Year'].unique()

dfeu=test.loc[test['Continent Code'] == "EU"]
dfaf=test.loc[test['Continent Code'] == 'AF']
dfsa=test.loc[test['Continent Code'] == "SA"]
dfoc=test.loc[test['Continent Code'] == 'OC']
dfas=test.loc[test['Continent Code'] == "AS"]
dfna=test.loc[test['Continent Code'] == "NA"]

dfeu.index=dfeu['Year']
dfaf.index=dfaf['Year']
dfsa.index=dfsa['Year']
dfoc.index=dfoc['Year']
dfas.index=dfas['Year']
dfna.index=dfna['Year']

yeu=dfeu['CO2e per capita']
yaf=dfaf['CO2e per capita']
ysa=dfsa['CO2e per capita']
yoc=dfoc['CO2e per capita']
yas=dfas['CO2e per capita']
yna=dfna['CO2e per capita']

yeu = np.array(yeu)
yaf= np.array(yaf)
ysa = np.array(ysa)
yoc= np.array(yoc)
yas = np.array(yas)
yna= np.array(yna)


#https://www.geeksforgeeks.org/matplotlib-pyplot-stackplot-in-python/ #infos zu stackplots
plt.stackplot(x,yeu,yaf,ysa,yoc,yas,yna, labels=['South America','Africa','Europe','Asia','Oceania','North America'],colors=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'],baseline='zero')
plt.legend(loc='upper left')
plt.show()



#ranking der länder nach co2 per capita im jahr 2014
test1=test['Year']==2014
test[test1]

df14=df.loc[df['Year'] == 2014]
df14=df14.set_index("Entity")
#durchschnittlicher co2 per capita über alle Jahre
ax=df14['CO2e per capita'].sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("CO2 per capita in [t]")
ax.set_title("Ranking CO2 per capita in 2014")
ax.set_ylabel("Country")
plt.show()

#durchschnittlicher co2 per capita über alle Jahre
#ax=df14.groupby('Entity')['CO2e per capita'].mean().sort_values().plot(kind='barh', figsize=(10,12))
#ax.set_xlabel("CO2 per capita in [t]")
#ax.set_title("Ranking CO2 per capita in 2014")
#ax.set_ylabel("Country")



#durchschnittlicher co2 per capita über alle Jahre
#ax=df.groupby('Continent Code')['CO2e per capita'].mean().sort_values().plot(kind='barh', figsize=(10,12))
#ax.set_xlabel("CO2 per capita in [t]")
#ax.set_title("Ranking CO2 per capita in 2014")
#ax.set_ylabel("Country")



#dftest=df.loc[df['Year']==i,['CO2e per capita','Entity','Continent Code']]
#

#plots der co2 per capita nach kontinenten für jedes jahr 1990-2014
for i in range(1990,2015):
    dftest=df.loc[df['Year']==i,['CO2e per capita','Entity','Continent Code']]
    ax=dftest.groupby('Continent Code')['CO2e per capita'].mean().sort_values().plot(kind='barh',color=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'])#, figsize=(10,12))
    ax.set_xlabel("CO2 per capita in [t]")
    ax.set_title("Ranking CO2 per capita in "+str(i))
    ax.set_ylabel("Country")
    #plt.savefig(str(i)+'.png')
    plt.show()
