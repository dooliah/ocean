# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 11:32:37 2024

@author: dalia
"""
#library imported
import pandas as pd

#dfworking is the dataframe, which I copied from my file list into python here
dfworking = pd.read_csv('C:/Users/dalia/OneDrive/CHARACTER TIME OC/Dalia Fixed Time Sheets.csv')

print(dfworking)

#to look at columns in my dfworking 
dfworking.columns

#look at values in the character column
print(dfworking['Character'])


#to drop the NaN column in my dfworking, kept original and made new cleaned df, need axis = 1 to identify only column being removed
dfworking1 = dfworking.drop('Good_clip', axis = 1)

#to check the new columns in new df
dfworking1.columns

#isolate characters into their own df for manipulation
ryandf = dfworking1[dfworking1["Character"] == "Ryan"]

sandydf = dfworking1[dfworking1['Character'] == "Sandy"]

kirstendf = dfworking1[dfworking1['Character'] == "Kirsten"]

marissadf = dfworking1[dfworking1['Character'] == "Marissa"]

lukedf = dfworking1[dfworking1['Character'] == "Luke"]

summerdf = dfworking1[dfworking1['Character'] == "Summer"]

jimmydf = dfworking1[dfworking1['Character'] == "Jimmy"]

sethdf = dfworking1[dfworking1['Character'] == "Seth"]

juliedf = dfworking1[dfworking1['Character'] == "Julie"]

#calculate sum total of clip length for each character

ryan_total = sum(ryandf['Clip_length'])

julie_total = sum(juliedf['Clip_length'])

marissa_total = sum(marissadf['Clip_length'])

luke_total = sum(lukedf['Clip_length'])

summer_total = sum(summerdf['Clip_length'])

jimmy_total = sum(jimmydf['Clip_length'])

seth_total = sum(sethdf['Clip_length'])

sandy_total = sum(sandydf['Clip_length'])

kirsten_total = sum(kirstendf['Clip_length'])


#make bar plot 
import matplotlib.pyplot as plt

categories = ['Ryan','Sandy','Kirsten','Marissa','Luke','Summer','Jimmy','Seth','Julie']
values = ['ryan_total','sandy_total','kirsten_total','marissa_total','luke_total','summer_total','jimmy_total','seth_total','julie_total']


clip_bar = plt.bar(categories, values)

plt.show(clip_bar)

#sort columns in the data set before, need to create a df for the values before making bar plot 
df_bar = pd.DataFrame({'Character': ['Ryan','Sandy','Kirsten','Marissa','Luke','Summer','Jimmy','Seth','Julie'],'Seconds': [ryan_total,sandy_total,kirsten_total,marissa_total,luke_total,summer_total,jimmy_total,seth_total,julie_total]})

df_bar = df_bar.sort_values(by = 'Seconds', ascending = False)

df_bar1 = plt.bar(df_bar['Character'],df_bar['Seconds'])

#adding labels to sorted bar plot

df_bar1 = plt.xlabel('Character')
df_bar1 = plt.ylabel('Seconds')
df_bar1 = plt.title('ScreenTime of Each Character')

#attempting a for loop to sum screen time for all characters using my df_bar dataset

x= sum(df_bar['Seconds'])

for y in df_bar['Character']:
    if y == 'Ryan':
        clip_sum = sum(df_bar.iloc[:,1])
    if y == 'Marissa':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Sandy':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Seth':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Luke':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Summer':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Jimmy':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Julie':
        clip_sum + sum(df_bar.iloc[:,1])
    if y == 'Kirsten': 
        clip_sum + sum(df_bar.iloc[:,1])



        


