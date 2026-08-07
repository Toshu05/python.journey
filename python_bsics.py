a,b=10,20
print(a+b)#same for other operator
print(a==b)
print(a>b)#same for other operators
print(a|a)#same for other opertors
str1="Rohit"
print(str1)
str2="What to do" \
"I am so stressed " \
"these days."
print(str2)
print(str2[0])
print(str1[-1])
print(str2[5:11])#leaves 11 index
#Basic string functions
print(len(str1))
print(str1.upper())
print(str2.replace('am','are'))
str_new="sparta sparta 300 300 300"
print(str_new.count('sparta'))
print(str_new.find('300'))
#another functions like endsWith(),startsWith(),tite(),replace(),split()

#data structures tuple,list,dictionary,set
#Tuple
tup1=(1,'a',"True",True)
print(type(tup1))
#indexing
print(tup1[0])
print(tup1[-1])
print(tup1[1:3])
print(len(tup1))
tup2=(3,4,5)
print(tup1+tup2)
print(tup2*3)
print(min(tup2))
print(max(tup2))
#List
l1=[1,'sparta',3.14,True]
print(type(l1))
print(l1[1])
print(l1[1:3])
#List functions
l1.append("eren")
l1.pop()
l1.reverse()
l1.insert(1,False)
print(l1)
#other functions append,insert,extend,count,sum,max,min,search,sort,index

#dictionary
fruit={"Apple":10,"orange":20}
print(type(fruit))
print(fruit.keys())
print(fruit.values())
print(fruit["Apple"])
fruit["Apple"]=100
#update function to assign one dict to another

#sets
s=(10,"3.14",False)
#add ,update,remove,union,intersection

#Conditional Statements
a,b=10,20
if(a>b):
    print("A")
else:
    print("B")

tup3=('a','b','c')
if('a' in tup3):
   print("Value is present")
else:
    print("Not present")

#looping
i=1
while(i<=10):
    print(i)
    i=i+1

for k in tup3:
    print(k)



