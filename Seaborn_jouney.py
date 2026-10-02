import seaborn as sns
from matplotlib import pyplot as plt
#datasets like tips.fmri,iris,titanic,penguin,diamonds,flights etc.
fmri=sns.load_dataset("fmri")
print(fmri.head())
sns.lineplot(x="timepoint",y="signal",data=fmri)
plt.show()
print(fmri.shape)
#gruping data with hue in fmri used to determine color of line
sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event')
plt.show()
#adding style for sytling the line
sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event',style='event')
plt.show()
#adding marker in it too
sns.lineplot(x='timepoint',y='signal',data=fmri,hue='event',style='event',markers=True)
plt.show()
#seaborn bar plot
#->working on dataset of pokemon
import pandas as pd
sns.set(style='whitegrid')
pokemon=pd.read_csv('POKEMON.csv')
sns.barplot(x='Pokemon',y='Speed',data=pokemon)
plt.show()
sns.barplot(x='Pokemon',y='weight',data=pokemon)
plt.show()
sns.barplot(x="Pokemon",y="Speed",hue='level',data=pokemon)
plt.show()
#we can also add palette as attribute or we can also add color attribute here

#Seaborn Scatterplot
iris=sns.load_dataset("iris")
print(iris.head())
sns.scatterplot(x='sepal_length',y='sepal_width',data=iris,hue='sepal_length')
plt.show()
#seaborn Histogram/Distplotor distribution plot
diamonds=sns.load_dataset('diamonds')
print(diamonds.head())
sns.displot(diamonds['price'],color='red',bins=10,kde=False)
plt.show()
#JointPlot
iris=sns.load_dataset('iris')
sns.jointplot(x="sepal_length",y='sepal_width',data=iris,color='olive',kind='reg')
plt.show()
#Seaborn BoxPlot
#Seaborn Pair Plot
df=sns.load_dataset('iris')
sns.pairplot(df,hue='species')
plt.show()