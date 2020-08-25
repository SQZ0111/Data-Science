#!/usr/bin/env python
# coding: utf-8

# In[89]:


#http://jonathansoma.com/lede/algorithms-2017/classes/fuzziness-matplotlib/how-pandas-uses-matplotlib-plus-figures-axes-and-subplots/
#gute Erklärungen zu plots
#weitere matplotlib beispiele https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots.html

get_ipython().run_line_magic('matplotlib', 'inline')
#%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# In[90]:


# Seaborn visualization library
import seaborn as sns
from pylab import plot, show, savefig, xlim, figure, ylim, legend, boxplot, setp, axes
import pycountry_convert as pc


# In[91]:


df=pd.read_excel('https://github.com/EnergizedTechLabsDo/energized/raw/master/All_Data_final.xlsx')


# In[92]:


df.head()

df["Entity"].drop_duplicates()
# In[93]:


# exploratory plots; is data complete?
plt.figure(figsize=(12, 4))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
plt.show()
sns.distplot(df["GDP"], color="purple", bins=10)
plt.show()


# In[102]:


df['Overall energy use in [kwh]']=df['Population']*df['Energy use per capita']
df['Overall CO2e']=df['Population']*df['CO2e per capita']


# In[103]:


df.head()


# ## line plot 

# In[111]:


#neue Spalte hinzufügen, um Werte mit populationsgröße zu gewichten 
df_line_plot=df.groupby('Year')['Overall energy use in [kwh]'].sum()
df_line_plot=df_line_plot.to_frame()
df_line_plot['Overall CO2e']=df.groupby('Year')['Overall CO2e'].sum()


# In[112]:


df_line_plot.head()


# In[ ]:





# In[113]:


cap=[]
for i in range(1990,2015):
    testdf=df.loc[df['Year'] == i] 
    cap.append(testdf["Population"].sum())
df_line_plot["sum of pop"]=cap
df_line_plot["energy use per cap"]=df_line_plot["Overall energy use in [kwh]"]/df_line_plot['sum of pop']
df_line_plot["overall co2e per cap"]=df_line_plot["Overall CO2e"]/df_line_plot['sum of pop']


# In[114]:


#df_line_plot.head()
df_line_plot.head()
df_line_plot["overall co2e"]=df.groupby('Year')['Overall CO2e'].sum()
df_line_plot["Pop in Milliards"]=df_line_plot['sum of pop']/1000000000
df_line_plot["overall co2e per cap"]=df_line_plot["overall co2e"]/df_line_plot['sum of pop']


# In[115]:


df_line_plot.head()


# In[116]:


#durchschnittlicher co2 per capita über alle Jahre
fig=plt.subplots()
ax1=plt.axes()
ax1=df_line_plot['energy use per cap'].plot()#.sort_values().plot(kind='barh', figsize=(10,12))
ax1.set_xlabel("Year")
ax1.set_ylabel("energy use in [kwh]")
ax1.set_title('Average energy use per capita in [kwh]')
#ax1.tick_params
ax1.set_ylim(ymin=0)
ax1.set_ylim(ymax=30000)

color='tab:blue'
ax1.tick_params(axis='y',labelcolor=color)


# In[117]:


#df_line_plot['overall co2e per cap'].min()


# In[118]:


# create figure and axis objects with subplots()
fig,ax = plt.subplots(figsize=(15,12))

# make a plot
ax.plot(df_line_plot['energy use per cap'], color="red")
# set x-axis label
ax.set_xlabel("year",fontsize=10)
# set y-axis label
ax.set_ylabel("energy consumption per capita [kwh]",fontsize=10)
ax.set_ylim(ymin=df_line_plot['energy use per cap'].min())
#ax.set_ylim(ymin=0)
ax.set_ylim(ymax=df_line_plot['energy use per cap'].max())
color='tab:red'
ax.tick_params(axis='y',labelcolor=color)
ax.set_title('Comparison of energy consumption and CO2 emissions')

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(df_line_plot['overall co2e per cap'])
ax2.set_ylabel("CO2 emissions per capita [t]",fontsize=10)
ax2.set_ylim(ymin=df_line_plot['overall co2e per cap'].min())
#ax2.set_ylim(ymin=0)
ax2.set_ylim(ymax=df_line_plot['overall co2e per cap'].max())
color='tab:blue'
ax2.tick_params(axis='y',labelcolor=color)
plt.show()


# In[119]:


df_line_plot.head()


# In[ ]:


#df_log.boxplot(column=['HDI'], by=['Entity'])


# ## boxplots 

# In[ ]:


ax=df.boxplot(column=['CO2e per capita'], by=['Year'],figsize=(20,20))
ax.set_xlabel("Year")
ax.set_title("CO2 emissions per capita in [t]")
ax.set_ylabel("CO2 emissions per capita in [t]")


# In[ ]:





# ## area plot

# In[ ]:


#country_code = pc.country_name_to_country_alpha2("Sweden", cn_name_format="default")
#print(country_code)
#continent_name = pc.country_alpha2_to_continent_code(country_code)
#print(continent_name)


# In[120]:


codes=[]
ccodes=[]
alpha3=[]


# In[121]:


for value in df["Entity"]:
    country_code = pc.country_name_to_country_alpha2(value, cn_name_format="default")
    continent_name = pc.country_alpha2_to_continent_code(country_code)
    alpha=pc.country_name_to_country_alpha3(value, cn_name_format="default")
    codes.append(continent_name)
    ccodes.append(country_code)
    alpha3.append(alpha)


# In[122]:


df["Continent Code"]=codes
df["Country Code"]=ccodes
df['Country Code Alpha3']=alpha3


# In[123]:


df['Continent Code'].unique()


# In[124]:


df['Overall CO2 consumption in [t]']=df['Population']*df['CO2e per capita']
df['Overall CO2 consumption in Mio']=df['Overall CO2 consumption in [t]']/1000000
continente=df.groupby(['Continent Code','Year']).sum()
#continente2=df.groupby(['Continent Code','Year']).sum()


# In[125]:


continente.reset_index(inplace=True)


# In[126]:


df.loc[(df["Continent Code"]=="OC")&(df["Year"]==2014)]["Entity"]


# In[127]:


continente['CO2e per capita in Mio']=(continente['Overall CO2 consumption in [t]']/continente["Population"])/1000000


# In[128]:


continente.loc[continente['Continent Code']=="NA"]


# In[129]:


continente.head()


# In[ ]:


#continentedf=continente.to_frame()
#test2=continente2.to_frame()
#testpop=continente2.to_frame()

#test.reset_index(inplace=True)
#testpop.reset_index(inplace=True)  


# In[ ]:


#continente.loc[continente["Continent Code"]=="AS"]


# In[ ]:


#df.loc[df["Entity"]=='Canada']


# In[ ]:


#testpop.loc[testpop["Continent Code"]=='AS']


# In[ ]:


#test2.loc[test2['Continent Code'] == "EU"]


# In[ ]:


#dfoc['CO2e per capita']


# In[ ]:


#df.loc[df(['Year']==2014)&(df["Continent Code"]=="OC")]


# In[ ]:


#test.reset_index(inplace=True)  
#test2.reset_index(inplace=True)


# In[130]:


x=df['Year'].unique()

dfeu=continente.loc[continente['Continent Code'] == "EU"]
dfaf=continente.loc[continente['Continent Code'] == 'AF']
dfsa=continente.loc[continente['Continent Code'] == "SA"]
dfoc=continente.loc[continente['Continent Code'] == 'OC']
dfas=continente.loc[continente['Continent Code'] == "AS"]
dfna=continente.loc[continente['Continent Code'] == "NA"]

dfeu.index=dfeu['Year']
dfaf.index=dfaf['Year']
dfsa.index=dfsa['Year']
dfoc.index=dfoc['Year']
dfas.index=dfas['Year']
dfna.index=dfna['Year']

yeu=dfeu['Overall CO2 consumption in Mio']
yaf=dfaf['Overall CO2 consumption in Mio']
ysa=dfsa['Overall CO2 consumption in Mio']
yoc=dfoc['Overall CO2 consumption in Mio']
yas=dfas['Overall CO2 consumption in Mio']
yna=dfna['Overall CO2 consumption in Mio']

yeu = np.array(yeu)
yaf= np.array(yaf)
ysa = np.array(ysa)
yoc= np.array(yoc)
yas = np.array(yas)
yna= np.array(yna)

#https://www.geeksforgeeks.org/matplotlib-pyplot-stackplot-in-python/
## gesamt CO2 betrachtung 

plt.figure(figsize=(10,7))
plt.suptitle('Yearly overall CO2 emissions in million tonnes by continent')
plt.xlabel('Year')
plt.ylabel('Emissions in million tonnes')
#plt.stackplot(x,yeu,yaf,ysa,yoc,yas,yna, labels=['Europe','Arfica','South America','Oceania','Asia','North America'],colors=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'],baseline='zero')
plt.stackplot(x,yoc,yaf,ysa,yeu,yna,yas, labels=['Oceania','Arfica','South America','Europe','North America','Asia'],colors=['cadetblue','powderblue','thistle','turquoise','lightseagreen','lightsteelblue'],baseline='zero')
plt.legend(loc='upper left')


# In[ ]:





# In[ ]:


#dfas
#continente.loc[continente["Year"]==2014].sort_values(by="Overall CO2 consumption in [t]")


# In[131]:


x=df['Year'].unique()

dfeu=continente.loc[continente['Continent Code'] == "EU"]
dfaf=continente.loc[continente['Continent Code'] == 'AF']
dfsa=continente.loc[continente['Continent Code'] == "SA"]
dfoc=continente.loc[continente['Continent Code'] == 'OC']
dfas=continente.loc[continente['Continent Code'] == "AS"]
dfna=continente.loc[continente['Continent Code'] == "NA"]

dfeu.index=dfeu['Year']
dfaf.index=dfaf['Year']
dfsa.index=dfsa['Year']
dfoc.index=dfoc['Year']
dfas.index=dfas['Year']
dfna.index=dfna['Year']

#yeu=dfeu['CO2e per capita']
#yaf=dfaf['CO2e per capita']
#ysa=dfsa['CO2e per capita']
#yoc=dfoc['CO2e per capita']
#yas=dfas['CO2e per capita']
#yna=dfna['CO2e per capita']

yeu=dfeu['Overall CO2 consumption in [t]']/dfeu['Population']
yaf=dfaf['Overall CO2 consumption in [t]']/dfaf['Population']
ysa=dfsa['Overall CO2 consumption in [t]']/dfsa['Population']
yoc=dfoc['Overall CO2 consumption in [t]']/dfoc['Population']
yas=dfas['Overall CO2 consumption in [t]']/dfas['Population']
yna=dfna['Overall CO2 consumption in [t]']/dfna['Population']

yeu = np.array(yeu)
yaf= np.array(yaf)
ysa = np.array(ysa)
yoc= np.array(yoc)
yas = np.array(yas)
yna= np.array(yna)

#https://www.geeksforgeeks.org/matplotlib-pyplot-stackplot-in-python/
plt.figure(figsize=(10,7))
plt.suptitle('Yearly CO2 emissions per capita in tonnes by continent')
plt.xlabel('Year')
plt.ylabel('Emissions in tonnes')
#plt.stackplot(x,yeu,yaf,ysa,yoc,yas,yna, labels=['Europe','Africa','South America','Oceania','Asia','North America'],colors=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'],baseline='zero')
plt.stackplot(x,ysa,yas,yaf,yeu,yna,yoc,labels=['South America','Asia','Africa','Europe','North America','Oceania'],colors=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'],baseline='zero')
plt.legend(loc='upper left')


# In[ ]:


x=df['Year'].unique()

dfeu=continente.loc[continente['Continent Code'] == "EU"]
dfaf=continente.loc[continente['Continent Code'] == 'AF']
dfsa=continente.loc[continente['Continent Code'] == "SA"]
dfoc=continente.loc[continente['Continent Code'] == 'OC']
dfas=continente.loc[continente['Continent Code'] == "AS"]
dfna=continente.loc[continente['Continent Code'] == "NA"]

dfeu.index=dfeu['Year']
dfaf.index=dfaf['Year']
dfsa.index=dfsa['Year']
dfoc.index=dfoc['Year']
dfas.index=dfas['Year']
dfna.index=dfna['Year']

#yeu=dfeu['CO2e per capita']
#yaf=dfaf['CO2e per capita']
#ysa=dfsa['CO2e per capita']
#yoc=dfoc['CO2e per capita']
#yas=dfas['CO2e per capita']
#yna=dfna['CO2e per capita']

yeu=dfeu['Overall CO2 consumption in [t]']/dfeu['Population']
yaf=dfaf['Overall CO2 consumption in [t]']/dfaf['Population']
ysa=dfsa['Overall CO2 consumption in [t]']/dfsa['Population']
yoc=dfoc['Overall CO2 consumption in [t]']/dfoc['Population']
yas=dfas['Overall CO2 consumption in [t]']/dfas['Population']
yna=dfna['Overall CO2 consumption in [t]']/dfna['Population']

yeu = np.array(yeu)
yaf= np.array(yaf)
ysa = np.array(ysa)
yoc= np.array(yoc)
yas = np.array(yas)
yna= np.array(yna)


#https://www.geeksforgeeks.org/matplotlib-pyplot-stackplot-in-python/
plt.figure(figsize=(10,7))
plt.suptitle('Yearly CO2 emissions per capita in tonnes by continent')
plt.xlabel('Year')
plt.ylabel('Emissions in tonnes')
plt.stackplot(x,yeu,yaf,ysa,yoc,yas,yna, labels=['Europe','Africa','South America','Oceania','Asia','North America'],colors=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'],baseline='zero')
plt.legend(loc='upper left')


# In[ ]:


#co2=continente.loc[continente["Year"]==2014].sort_values(by="CO2e per capita")
#co2.loc[co2["Year"]==2014][(["Continent Code","CO2e per capita"])]


# In[ ]:





# In[ ]:





# In[ ]:





# In[132]:


continente.loc[continente["Year"]==2009].sort_values(by="CO2e per capita")


# In[133]:


continente.loc[continente["Year"]==2014].sort_values(by="CO2e per capita")


# ## ranking (nicht in blog) 

# In[134]:


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


# In[183]:


#dftest=df.loc[df['Year']==i,['CO2e per capita','Entity','Continent Code']]
df14n=df14.nlargest(5,'CO2e per capita')
auswahl=['China','Germany','United States','France','United Kingdom','Russia']
df14n=df14n.append(df14[df14.Entity.isin(auswahl)]).sort_values(by='CO2e per capita')


# In[184]:


df14n=df14n.set_index("Entity")
ax=df14n['CO2e per capita'].sort_values().plot(kind='barh', figsize=(7,2))
ax.set_xlabel("CO2 per capita in [t]")
ax.set_title("Ranking CO2 per capita in 2014")
ax.set_ylabel("Country")


# In[171]:





# In[ ]:





# In[137]:


for i in range(1990,2015):
    dftest=df.loc[df['Year']==i,['CO2e per capita','Entity','Continent Code']]
    ax=dftest.groupby('Continent Code')['CO2e per capita'].mean().sort_values().plot(kind='barh',color=['thistle','lightsteelblue','powderblue','turquoise','lightseagreen','cadetblue'])#, figsize=(10,12))
    ax.set_xlabel("CO2 per capita in [t]")
    ax.set_title("Ranking CO2 per capita in "+str(i))
    ax.set_ylabel("Contient")
    plt.show()


# In[138]:


#df.head()


# In[139]:


df14=df.loc[df['Year']==2014]


# ## Berechnung Jahre bis 2° bzw. 1,5° Ziel erreicht 

# In[140]:


#ger_pop=83020000
world_pop=7821701978
grad2=1058865080000
grad1_5=310011059305


# In[141]:


jahre2=[]
for j in df14["Entity"]:
    co2=df14.loc[(df['Entity']==j)&(df["Year"]==2014),['CO2e per capita']]
    co2=co2['CO2e per capita'].values[0]
    jahre2.append(grad2/(co2*world_pop))

jahre1_5=[]
for j in df14["Entity"]:
    co2=df14.loc[(df['Entity']==j)&(df["Year"]==2014),['CO2e per capita']]
    co2=co2['CO2e per capita'].values[0]
    jahre1_5.append(grad1_5/(co2*world_pop))
    
summenprodukt=0
for j in df14["Entity"]:
    co2=df14.loc[(df['Entity']==j)&(df["Year"]==2014),['CO2e per capita']]
    pop=df14.loc[(df['Entity']==j)&(df["Year"]==2014),['Population']]
    co2=co2['CO2e per capita'].values[0]
    pop=pop['Population'].values[0]
    summenprodukt=summenprodukt+co2*pop
    #jahre1_5.append(grad1_5/(co2*world_pop))    


# In[142]:


ziel1_5=grad1_5/summenprodukt
ziel2=grad2/summenprodukt


# In[143]:


df14["Years to 2°"]=jahre2
df14["Years to 1,5°"]=jahre1_5


# In[144]:


#df14["Years to 2"]=jahre


# In[145]:


#df14=df14.drop(columns=["Coutry Code"])
df14.head(100)


# In[146]:


#dfsort=df14.sort_values(by=['Years to 2°'])
#sns.set(style="whitegrid")
#size=(10,15)
#fig, ax=plt.subplots(figsize=size)
#sns.barplot(ax=ax,data=dfsort,x="Years to 2°", y="Entity",color="b",hue="Continent Code")#label="???")
#sns.barplot(ax=ax,data=dfsort,x="Years to 2°", y="Entity",hue="Continent Code",dodge=False,palette={'NA':'b', 'AS':'g', 'OC':'r','EU':'c', 'AF':'y', 'SA':'k'})


# In[147]:


#df14=df14.set_index("Entity")
#ax=df14['Years to 2°'].sort_values().plot(kind='barh', figsize=(10,12),color=)
#ax.set_xlabel("???[t]")
#ax.set_title("??? "+str(i))
#ax.set_ylabel("Country")
#plt.show()


# ## visualisierung der Jahre bis 2° farblich mit folium (nicht im blog)

# In[148]:


import json
import requests
import folium


# In[149]:


json_url="https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson"
geo_json_data = json.loads(requests.get(json_url).text)


# In[150]:


#df14['Years to 2°'].sort_values().unique()


# In[151]:


data_to_plot=df14[['Country Code','CO2e per capita']]


# In[152]:


m = folium.Map()

#farbspektrum nach Population -weiß sind länder die nicht in geojson enthalten waren
folium.Choropleth(
    geo_data=geo_json_data,
    name="choropleth",
    data=data_to_plot,
    columns=['Country Code', 'CO2e per capita'],
    key_on='properties.ISO_A2',
    #fill_color='YlGn',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.2,
    #bins=[0,5, 10,20, 30, 50,80,300],
    bins = list(data_to_plot['CO2e per capita'].quantile([0,0.2,0.4, 0.5,0.6, 1])),
    reset=True
).add_to(m)


# In[153]:


m


# In[ ]:





# In[ ]:





# In[ ]:


#df14.loc[(df14["Years to 2°"]<=10)&(df14["Years to 2°"]>5)].sort_values(by="Years to 2°")


# In[ ]:


#df14.loc[df14["Entity"]=='China',]


# In[154]:


df14


# In[155]:


df14[(df14["Years to 1,5°"]<30)]


# In[156]:


auswahl=['China','Germany','United States','France','United Kingdom','Qatar']


# In[157]:


df14[df14.Entity.isin(auswahl)]


# ## histogramme

# In[158]:


df_hist=df14[['Years to 1,5°']]
#df_hist=df14['Years to 1,5°']


# In[ ]:


#df_hist


# In[ ]:





# In[159]:


#https://www.mcc-berlin.net/forschung/co2-budget.html
ax=df_hist.plot.hist(bins=30,alpha=0.5,figsize=(12,8),weights = np.ones_like(df_hist.index) / len(df_hist.index),cumulative=1)
ax.grid(True)
ax.set_title('Histogram - Years to achieve 1,5°C goal')
ax.set_xlabel('Years from 2014')
ax.set_ylabel('cumulated relative frequency')
plt.legend(loc='upper right')
ax=ax.set_ylim(ymax=1)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.axvline(x=ziel1_5)
#plt.axvline(x=ziel2,color='k')


# In[163]:


ax=df_hist.plot.hist(bins=20,alpha=0.5,figsize=(12,8),weights = np.ones_like(df_hist.index) / len(df_hist.index))
ax.grid(True)
ax.set_title('Histogram - Years to achieve 1,5°C and 2°C goal')
ax.set_xlabel('Years from 2014')
ax.set_ylabel('relative frequency')
plt.legend(loc='upper right')
ax=ax.set_ylim(ymax=1)
plt.xticks([0,25,50,75,100])#,125,150,175,200,250,300])


# In[ ]:





# In[ ]:




