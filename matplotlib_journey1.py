import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,15)
print(x)
y=4*x
print(y)
plt.plot(x,y)
y=2*x
#adding title and labels
plt.title("Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
#changing line asthestics
plt.plot(x,y,color='g',linestyle=':',linewidth=8)
plt.show()
x1=np.arange(1,11)
y1=3*x
plt.plot(x,y,color='g',linestyle=':',linewidth=8)
plt.plot(x,y1,color='r',linestyle='-.',linewidth=5)
plt.title("Two Line Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.grid(True)
plt.show()
#adding sub-plots
plt.subplot(1,2,1)
plt.plot(x,y,color='g',linestyle=':',linewidth=8)
plt.title("Subplots")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.subplot(1,2,2)
plt.plot(x,y1,color='r',linestyle='-.',linewidth=5)
plt.title("Subplots")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()
#working with bar Plot
Student={"Bob":98,"Qop":34,"fty":56}
Names=list(Student.keys())
Values=list(Student.values())
plt.bar(Names,Values,color='y')
plt.title("Bar-Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()
#working with horizontal bar plot
plt.barh(Names,Values,color='g')
plt.title("Horizontal-Bar-Plot")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()
#sactter-plot
x=[10,2,3,4,5,6]
y=[3,6,7,3,5,6]
z=[2,5,7,8,9,2]
plt.scatter(x,y)
plt.show()
#changing mark aesthetics
plt.scatter(x,y,marker="*",c="g",s=100)
plt.scatter(x,z,marker="D",c="r",s=100)#marker color,size
plt.show() 
plt.subplot(1,2,1)
plt.scatter(x,y,marker="*",c="g",s=100)
plt.subplot(1,2,2)
plt.scatter(x,z,marker="D",c="r",s=100)
plt.show()


