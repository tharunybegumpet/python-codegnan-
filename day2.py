# numeric data type 
number=100
print(number,type(number))
#integer
integer=10
print(integer,type(integer))
#float
floatnum=10.5
print(floatnum,type(floatnum))
#complex
complexnum=2+3j
print(complexnum,type(complexnum))

#sequence data type 
s="tharuny"
list11=[1,2,3,4,5,5,"hi"]
tuple22=(1,2,3,4.5,5,"hi")
print(s,type(s),list11,type(list11),tuple22,type(tuple22))

#boolean data type 
boole=True
print(boole,type(boole))
boolean=False
print(boole+boolean)

#dictionary data type 
d={"name":"tharuny",
   "location":"hyderabad",
   "brach":4}
print(d,type(d))

#set data type 
set1=set()
set2={1,1.2,5.5,"7"}
print(set1)
print(set2)

#empty data types 
list1=[] #list()
tuple1=() #tuple()
str1="" #str()
print(list1,type(list1),tuple1,type(tuple1),str1,type(str1))
dict1={} #dict()
set3=set() #set()
print(dict1,type(dict1),set3,type(set3))

#empty data types 
list2=[]#list()
tuple2=()#tuple()
str2=""#str()
dict2={}#dict()
set4=set()#set()
print(list2,type(list2),tuple2,type(tuple2),str2,type(str2),dict2,type(dict2),set4,type(set4))


#conversion of sequence data types 

str1="tharuny"
list1=list(str1)
tuple1=tuple(list1)
set1=set(tuple1)
print(str1)
print(list1)
print(tuple1)
print(set1)

#type casting and input function
num1=int(input("enter the number1:"))  #type casting explicit type casting
print(num1,type(num1))
num3=float(input("enter the number3:"))
num4=num1+num3
print(num4,type(num4)) #implicit type casting 3

#input function for sequence data types 

list18=list(map(int,input("enter the list values:").split(",")))
print(list18)
tuple18=tuple(map(int,input("enter the list values:").split(",")))
print(tuple18)
set18=set(map(int,input("enter the list values:").split(",")))
print(set18)



