medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
urlretrieve(medical_charges_url,'medical.csv')
import pandas as pd
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

medical_df=pd.read_csv('medical.csv')
#picking data on non-smokers
non_smokers_df=medical_df[medical_df.smoker=='no']
sns.scatterplot(data=non_smokers_df,x='age',y='charges',alpha=0.7,s=15)
plt.show()
#we get a line here by formula y=wx+b 
#we are saying charges=w*charges +b because we are to get some trends here,not complete dependancy on each other due to other dependancy
#here w and b are weight and bias whereas in mathematics its called slpe and intercept
#shows linear regression model
#we are using to fits points near to the lines
def estimate_charges(age,w,b):
    return w*age+b
w,b=50,100
print(estimate_charges(30,50,100))
#now let's take all the ages 
ages=non_smokers_df.age
estimated_charges=estimate_charges(ages,w,b)
plt.plot(ages,estimated_charges,'r-o')
plt.xlabel('age')
plt.ylabel('Estimated_charges')
plt.show()
target=non_smokers_df.charges
plt.plot(ages,estimated_charges,'r')
plt.scatter(ages,target,s=8)
plt.xlabel('age')
plt.ylabel('charges')
plt.legend(['Estimate','Actual'])
plt.show()
#now we change the values of w and b to best fit the lines
def try_parameter(w,b):
    ages=non_smokers_df.age
    target=non_smokers_df.charges
    estimated_charges=estimate_charges(ages,w,b)
    plt.plot(ages,estimated_charges,'r',)
    plt.scatter(ages,target,s=8)
    plt.xlabel('age')
    plt.ylabel('charges')
    plt.legend(['Estimate','Actual'])
    plt.show()
try_parameter(340,-5100)