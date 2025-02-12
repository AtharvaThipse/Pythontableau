# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 12:33:09 2025

@author: Athar
"""
 
import pandas as pd

data = pd.read_csv('transaction2.csv')

data = pd.read_csv('transaction2.csv',sep=';')

data.info()

data['total cost'] = data['NumberOfItemsPurchased']*data['CostPerItem']

data.head()



CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

ProfitPerItem = 21.11-11.73
ProfitPerItem = SellingPricePerItem - CostPerItem
#ProfitPerItem = 21.11*11.73
#ProfitPerItem = 21.11/11.73

ProfitPerTransaction = NumberOfItemsPurchased*ProfitPerItem
CostPerTransaction = NumberOfItemsPurchased*CostPerItem
SellingPerTransaction = NumberOfItemsPurchased*SellingPricePerItem

data['SalesPErTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']


data['ProfitPerTransaction'] = data['SalesPErTransaction']-data['total cost']


data['Markup'] = ((data['SalesPErTransaction']-data['total cost'])/data['total cost']).round(2)

data['Day'] = data['Day'].astype(str)
data['Year'] = data['Year'].astype(str)

data['Date'] = data['Day']+'-'+data['Month']+'-'+data['Year']

data.drop(columns=['Day', 'Month', 'Year'], errors='ignore', inplace=True)

data.iloc[0]

data['UserId'].iloc[0]

data.iloc[-5:]

data.iloc[:,2]

data.iloc[4,2]

split_call = (data['ClientKeywords']).str.split(',',expand=True)

data['ClientAge'] = split_call[0]
data['ClientType']=split_call[1]
data['Contract']=split_call[2]

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['Contract']= data['Contract'].str.replace(']','')

data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons = pd.read_csv('value_inc_seasons.csv',sep=';')

data = pd.merge(data,seasons,on='Month')

data.drop('ClientKeywords',axis=1,inplace=True)

