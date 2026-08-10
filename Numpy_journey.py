import numpy as np
n1=np.array([[10,20,30,40],[34,7,8,9]])
print(type(n1))
#same number of elements not jacked array
n2=np.array([[10,2,3,4],[1,5,6,7,]])
print(n2)
n3=np.zeros((1,2))
print(n3)
n4=np.full((2,2),10)
print(n4)
n5=np.arange(10,20)
print(n5)
n6=np.arange(10,50,3)
print(n6)
n7=np.random.randint(1,100,1)
print(n7)
print(n2.shape)
#vstack,hstack,column_stack require compatible dimensions
print(np.vstack((n1,n2)))
print(np.hstack((n1,n2)))
print(np.column_stack((n1,n2)))
#other array functions
n8=np.array([5,7,4,3,4])
n9=np.array([1,2,3,4,5])
print(np.intersect1d(n8,n9))
print(np.setdiff1d(n8,n9))
print(np.setdiff1d(n9,n8))
#mathematics for numpy
print(np.sum([n1,n2]))
print(np.sum([n1,n2],axis=0))
print(np.sum([n1,n2],axis=1))
n1=n1+1
n2=n2-1
print(n1)
print(n2)
#mean median s.d
print(np.mean(n1))
print(np.median(n1))
print(np.std(n1))
np.save('my',n1)
n10=np.load('my.npy')



