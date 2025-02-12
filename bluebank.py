import pandas as pd
import json
import numpy as np
import matplotlib.pyplot as plt

#1 method
json_file = open('loan_data_json.json')
data = json.load(json_file)

#2nd method
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    print(data)
    

loandata = pd.DataFrame(data)


loandata['purpose'].unique()

loandata['log.annual.inc'] = np.exp(loandata['log.annual.inc'])

arr = np.array([1,2,3,4])

np.linspace(0,1,25)

fico = int(input("Enter a number :"))
ficoscore = int(input("Enter a number :"))


if fico >=300  and fico <400:
    print("very poor")
elif fico >=400 and ficoscore < 600:
    print("Poor")
elif fico >=601 and ficoscore < 660:
    print("Fair")
elif fico >=660 and ficoscore <780:
    print("good")
elif fico >= 780:
    print("Excellent")
    

length = len(loandata)
ficodata = []
for i in range(0,length):
    category  = loandata['fico'][i]
    if category >= 300 and category < 400:
        cat = 'Very poor'
    elif category >= 400 and category < 600:
        cat = 'poor'
    elif category >= 600 and category < 660:
        cat = 'Fair'
    elif category >= 660 and category < 700:
        cat = 'Good'
    elif category >= 700 :
        cat = 'Excellent'
    else:
        cat = "unknown"
    ficodata.append(cat)
    
    
length = len(loandata)
ficodata = []
for i in range(0,length):
    category  = 'red'
    try:
        if category >= 300 and category < 400:
            cat = 'Very poor'
        elif category >= 400 and category < 600:
            cat = 'poor'
        elif category >= 600 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700 :
            cat = 'Excellent'
        else:
            cat = "unknown"
    except:
        cat = 'error'
    ficodata.append(cat)
    

ficocat = pd.Series(ficodata)

loandata['fico.category'] = ficocat

loandata.loc[loandata['int.rate']>0.12 ,'int.rate.type']='High'
loandata.loc[loandata['int.rate']<0.12,'int.rate.type']='Low'

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='red')
plt.show()

purplot = loandata.groupby(['purpose']).size()

plt.hist(x = catplot,y= purplot)    
    
plt.scatter(x='log.annual.inc',y='dti',data=loandata)

loandata.to_csv("Newloan.csv")    
    
    
    