a , b , c=map(int ,input("Enter three numbers:").split())
if(a>b) &(a>c):
    print("a is greatest")
elif(b>a)&(b>c):
    print("b is greatest")
else:
    print("c is greatest")


import math
x=int(input("Enter the number"))
flag=1
if (x==0 )or (x==1):
    print("Not a prime number")
limit = int(math.sqrt(x))
for i in (2,limit+1):
    if x% i==0:
        print("not Prime")
        flag=0
        break
if(flag==1):
    print("Prime")
num=int(input("Enter the number"))
sum=0
for i in range(1,num+1,2):
    sum+=i
print(sum)
l1,l2=int(input(""))


        