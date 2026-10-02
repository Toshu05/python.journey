import numpy as np
from matplotlib import pyplot as plt
#histogram creating data
data=[1,2,3,4,4,5,6,7,6,7,8,9]
plt.hist(data)
plt.show()
#changing aesthetics
plt.hist(data,color='r',bins=4)
plt.show()
import pandas as pd
transaction=pd.read_csv('transaction.csv')
print(transaction.head())
plt.hist(transaction['Amount'],bins=15,color='g')
plt.show()
#box plot
one=[1,2,3,4,5,6,7,8,9]
two=[1,2,3,4,5,4,3,2,1]
three=[5,6,7,8,9,1,2,3,4]
data=list([one,two,three])
plt.boxplot(data)
plt.show()
#violin plot
plt.violinplot(data,showmedians=True)
plt.show()
#Pie chart
fruit=['Apple','Orange','Mango','Guava']
quantity=[86,45,89,23]
plt.pie(quantity,labels=fruit)
plt.show()
#to add percentage and specific colors
plt.pie(quantity,labels=fruit,autopct='%0.1f%%',colors=['yellow','black','green','pink'])
plt.show()
#donut chart
plt.pie(quantity,labels=fruit,radius=2)
plt.pie([100],colors=['w'],radius=1)
plt.show()