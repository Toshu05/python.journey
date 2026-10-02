medical_charges_url = 'https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv'
from urllib.request import urlretrieve
urlretrieve(medical_charges_url,'medical.csv')
import pandas as pd
medical_df=pd.read_csv('medical.csv')
print(medical_df)
print(medical_df.shape)
print(medical_df.columns)
print(medical_df.info())#shows no null columns which means good data
print(medical_df.describe())#we get mean,std,min,25%,50%,75%,max of all columns 

#we are doing exploratory analysis now which means getting explanations and hypothesis
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
matplotlib.rcParams['font.size']=14
matplotlib.rcParams['figure.figsize']=(10,6)
matplotlib.rcParams['figure.facecolor']='#00000000'
"""
Matplotlib & Seaborn visualization settings:
- sns.set_style('darkgrid') → Sets a dark grid background for plots.
- font.size = 14 → Sets the default font size.
- figure.figsize = (10, 6) → Sets the default plot size.
- figure.facecolor = '#00000000' → Makes the figure background transparent.
"""
print(medical_df.age.describe())
fig=px.histogram(medical_df,
                 x='age',
                 marginal='box',
                 nbins=47,
                 title="Distribution of Age")
fig.update_layout(bargap=0.1)
fig.show()
fig1=px.histogram(medical_df,
                 x='bmi',
                 marginal='box',
                 color_discrete_sequence=['red'],
                 title="Distribution of BMI")
fig1.update_layout(bargap=0.1)
fig1.show()
#shows gaussian distribution of bmi where mostly people lie in noraml to overweight categories
fig2=px.histogram(medical_df,
                 x='charges',
                 marginal='box',
                 color='smoker',
                 color_discrete_sequence=['grey','black'],
                 title="Distribution of Charges")
fig2.update_layout(bargap=0.1)
fig2.show()
"""we see people who smoke have a higher medical bills
median of non smokers is approx 7900 whereas of that of smokers it's about 35000"""

#we can now visulaize the distribution of smokers 
print(medical_df.smoker.value_counts())
fig3=px.histogram(medical_df,x='smoker',color='sex',title='Smoker')
fig3.show()
#number of smokers is about 20%
#percentage should be in proportion to populations



#age and charges corelation
fig4=px.scatter(medical_df,
                 x='age',
                 y='charges',
                 color='smoker',
                 title="age vs charges")
fig4.update_traces(marker_size=5)
fig4.show()
fig5=px.scatter(medical_df,
                 x='bmi',
                 y='charges',
                 color='smoker',
                 opacity=0.6,
                 title="BMI vs charges")
fig5.update_traces(marker_size=5)
fig5.show()
#here seems to be less relation between bmi and charges


#corr is a method to compute relationship between age and charges and others using corr method
print(medical_df.charges.corr(medical_df.age))
print(medical_df.charges.corr(medical_df.bmi))
#higher corelation between age and charges than corelation between bmi and charges

#if we have categorical data than we need to convert it into numerical data
smoker_values={'no':0,'yes':1}
smoker_numeric=medical_df.smoker.map(smoker_values)
print(medical_df.charges.corr(smoker_numeric))#highest corelation

#stronger the value stronger the relationship
#direction tends to tell sthe proportionality of one w.r.t to another 
#if one increases what happens to other


#corelation with the heatmap
sns.heatmap(medical_df.corr(),cmap='Reds',annot=True)
plt.title('Corelation Matrix')
#corelation doesn't tell cause-effect realtionship

