#!/usr/bin/env python
# coding: utf-8

# In[112]:


#http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/how-pandas-uses-matplotlib-plus-figures-axes-and-subplots/
#gute Erklärungen zu plots
#weitere matplotlib beispiele https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots.html

get_ipython().run_line_magic('matplotlib', 'inline')
#%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# In[21]:


# Seaborn visualization library
import seaborn as sns
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import pycountry_convert as pc


# In[22]:


df=pd.read_excel('https://github.com/EnergizedTechLabsDo/energized/raw/master/All_Data_final.xlsx')


# In[23]:


df.head()

df["Entity"].drop_duplicates()
# In[24]:


# exploratory plots; is data complete?
plt.figure(figsize=(12, 4))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
plt.show()
sns.distplot(df["GDP"], color="purple", bins=10)
plt.show()


# In[25]:


#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['CO2e per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("CO2 per Capita in t")
ax.set_title('World average CO2 per capita')


# ## line plot

# In[26]:


#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['Hydro power production per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("Hydro power production per capita [?]")
ax.set_title('Hydro power production per capita in [?]')


# In[37]:


#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['Energy use per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("Energy use per capita in [?]")
ax.set_title('Energy use per capita in [?]')


# In[38]:


#durchschnittlicher co2 per capita über alle Jahre
ax=df.groupby('Year')['Oil consumption per capita'].mean().plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("Year")
ax.set_ylabel("Oil consumption per capita in [?]")
ax.set_title('World average oil consumption per capita in [?]')


# In[34]:


#df_log.boxplot(column=['HDI'], by=['Entity'])


# In[43]:


df.boxplot(column=['CO2e per capita'], by=['Year'],figsize=(15,10))


# In[ ]:





# In[ ]:


#country_code = pc.country_name_to_country_alpha2("Sweden", cn_name_format="default")
#print(country_code)
#continent_name = pc.country_alpha2_to_continent_code(country_code)
#print(continent_name)


# In[45]:


codes=[]


# In[46]:


for value in df["Entity"]:
    country_code = pc.country_name_to_country_alpha2(value, cn_name_format="default")
    continent_name = pc.country_alpha2_to_continent_code(country_code)
    codes.append(continent_name)


# In[47]:


df["Continent Code"]=codes


# In[48]:


df['Continent Code'].unique()


# In[49]:


continente=df.groupby(['Continent Code','Year'])['CO2e per capita'].mean()


# In[50]:


test=continente.to_frame()


# In[51]:


test.reset_index(inplace=True)


# In[74]:





# In[ ]:





# In[78]:


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


# In[157]:


#https://www.geeksforgeeks.org/matplotlib-pyplot-stackplot-in-python/
plt.stackplot(x,yeu,yaf,ysa,yoc,yas,yna, labels=['South America','Africa','Europe','Asia','Oceania','North America'],colors=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'],baseline='zero')
plt.legend(loc='upper left')
plt.show()


# In[ ]:





# In[80]:


test1=test['Year']==2014


# In[81]:


test[test1]


# In[159]:


df14=df.loc[df['Year'] == 2014]
df14=df14.set_index("Entity")
#durchschnittlicher co2 per capita über alle Jahre
ax=df14['CO2e per capita'].sort_values().plot(kind='barh', figsize=(10,12))
ax.set_xlabel("CO2 per capita in [t]")
ax.set_title("Ranking CO2 per capita in 2014")
ax.set_ylabel("Country")

#durchschnittlicher co2 per capita über alle Jahre
#ax=df14.groupby('Entity')['CO2e per capita'].mean().sort_values().plot(kind='barh', figsize=(10,12))
#ax.set_xlabel("CO2 per capita in [t]")
#ax.set_title("Ranking CO2 per capita in 2014")
#ax.set_ylabel("Country")


# In[143]:


#durchschnittlicher co2 per capita über alle Jahre
#ax=df.groupby('Continent Code')['CO2e per capita'].mean().sort_values().plot(kind='barh', figsize=(10,12))
#ax.set_xlabel("CO2 per capita in [t]")
#ax.set_title("Ranking CO2 per capita in 2014")
#ax.set_ylabel("Country")


# In[98]:


#dftest=df.loc[df['Year']==i,['CO2e per capita','Entity','Continent Code']]
#

# In[147]:


for i in range(1990,2015):
    dftest=df.loc[df['Year']==i,['CO2e per capita','Entity','Continent Code']]
    ax=dftest.groupby('Continent Code')['CO2e per capita'].mean().sort_values().plot(kind='barh',color=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'])#, figsize=(10,12))
    ax.set_xlabel("CO2 per capita in [t]")
    ax.set_title("Ranking CO2 per capita in "+str(i))
    ax.set_ylabel("Country")
    plt.savefig(str(i)+'.png')
    #plt.show()


# In[ ]:
