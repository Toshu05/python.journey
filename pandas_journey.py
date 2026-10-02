import pandas as pd
p1=pd.Series([1,2,3,4,5])
print(type(p1))
print(p1)
#changing index values 
p2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(p2)
p3=pd.Series({'a':10,'b':20,'c':30})
print(p3)
p4=pd.Series({'a':10,'b':20,'c':30},index=['a','b','c','d'])
print(p4)
#extracting values
print(p1[2])
print(p1[1:])
print(p1[-3:])
#arithmetic operations
print(p1+5)
p5=pd.Series([3,53,7,855,88])
print(p5+p1)
#pandas dataframe compromises rows and columns
p6=pd.DataFrame({'Name':['Pandey','Jalan','Purwar'],'Marks':[75,12,82]})
print(p6)
#datadframe functions example:-transaction file
transaction=pd.read_csv('transaction.csv')
print(transaction.head())
print(transaction.tail())
print(transaction.shape)
print(transaction.describe())
#iloc and loc
print(transaction.iloc[2:6,2:])
print(transaction.loc[0:3,("Amount","Notes")])
#to drop or remove column using drop function
transaction.drop('Amount',axis=1)
#some more function like mean,median ,min,max with ending(),apply function:-to apply some user defines dunctions
#more functions like value_counts(),sort_values(by="attribute")
