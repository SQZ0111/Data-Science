import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data import
#df = pd.read_excel('all_data.xlsx')
df=pd.read_excel('https://github.com/EnergizedTechLabsDo/energized/raw/master/All_Data_final.xlsx')

# Adding new column 'Overall CO2 emissions' to the DataFrame
df['Overall CO2 emissions in [t]']=df['Population']*df['CO2e per capita']

# new Dataframes for the needed Years
df_Year = df
df_Year = df_Year.set_index(['Year'])

df_1990 = df_Year.loc[1990]
df_2014 = df_Year.loc[2014]

#Variablen für Schriftgrößen
fontsize_title = 15
fontsize_axis = 12
#Farbpalette
colors = ["#527BAB", "#164278" , "#81DCDE", "#F7BC8D" , "#E67350", "#AB5A52"]
palette = sns.color_palette(colors)
# Plot HDI and CO2 emissions
# Plot of 1990 and 2013 in the same subplot

fig = plt.figure(figsize=(10,7))
# Only for the legend (scatter points won't appear in plot due to the used coordinates of China)
huge_pop = plt.scatter(0.723,7.37,color='grey',s = 200)
medium_pop = plt.scatter(0.723,7.37,color='grey',s = 40)
small_pop = plt.scatter(0.723,7.37,color='grey',s = 5)
# Plot of 1990
plt.subplot(1,2,1)
legend_2 = plt.scatter(df_1990['HDI'], df_1990['CO2e per capita'], alpha= 0.5, s=df_1990['Population']/5000000,c='#164278')
# Plot of 2013
plt.subplot(1,2,1)
legend_1 = plt.scatter(df_2014['HDI'], df_2014['CO2e per capita'], s=df_2014['Population']/5000000,c='#AB5A52')

# labels and title
plt.xlabel('Human Development Index (HDI)', fontsize=fontsize_axis)
plt.ylabel('CO2e per capita [t]',fontsize=fontsize_axis)
#plt.title('Does rising prosperity lead to rising CO2 emissions?', fontsize=fontsize_title)
plt.yticks([0,df_2014['Overall CO2 emissions in [t]'].sum()/df_2014['Population'].sum(),10,20,30,40])
plt.xticks([0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

# including average CO2 emissions and average HDI
plt.axvline(df_2014['HDI'].mean(),ls = ':', color='k',  linewidth=1)
plt.axhline((df_2014['Overall CO2 emissions in [t]'].sum())/df_2014['Population'].sum(), ls = ':', color='k', linewidth=1)
plt.text(0.3,6,'  average CO2e',fontsize=6)
plt.text(0.3,4.5,'  per capita 2014 [t]',fontsize=6)
plt.text(0.81,-1.5,' average HDI 2014',fontsize=6)
#labeling specific countries in plot
plt.annotate('Qatar',(0.841,43.9),(0.75,32),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})
plt.annotate('Qatar',(0.754,24.7),(0.75,32),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})
plt.annotate('USA',(0.865,19.3),(0.92,20),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->' , 'linewidth':'0.5'})
plt.annotate('USA',(0.92,16.9),(0.92,20),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})
plt.annotate('China',(0.507,2.45),(0.58,8),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->'  , 'linewidth':'0.5'})
plt.annotate('China',(0.72,7.4),(0.58,8),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})
plt.annotate('Germany',(0.8,12.8),(0.83,14),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->'  , 'linewidth':'0.5'})
plt.annotate('Germany',(0.93,8.84),(0.83,14),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})
plt.annotate('Russia',(0.733,15.7),(0.73,13),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->'  , 'linewidth':'0.5'})
plt.annotate('Russia',(0.807,11.8),(0.73,13),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})
plt.annotate('India',(0.436,0.63),(0.56,-1),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->'  , 'linewidth':'0.5'})
plt.annotate('India',(0.605,1.53),(0.56,-1),fontsize = 6, arrowprops = {'color': 'black', 'arrowstyle': '->', 'linewidth':'0.5'})


# legend
lgnd = plt.legend([legend_1, legend_2, huge_pop, medium_pop, small_pop],['2014', '1990', 'big population', 'medium population', 'small population'],loc='upper left', title= 'Legend')
lgnd.legendHandles[0]._sizes = [30]
lgnd.legendHandles[1]._sizes = [30]

#plt.tight_layout()
plt.show()

fig.savefig('CO2e HDI', dpi=300)
