import numpy as np
num=np.random.randint(1,100,1)
n= int(input("guess computer's number "))
if(n==num):
    print("win")
else:
    print("lost")
