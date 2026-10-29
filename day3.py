
#Arithmetic operators
x=10
y=100
print(x+y,x-y,x*y,x/y,x//y,x%y,x**y)

#assignment operators 
x=200
print(x)
x+=100
print(x)
x-=200
print(x)
x*=10
print(x)
x/=10
print(x)
x//=2
print(x)
x%=2
print(x)
x**=2
print(x)

#comparision operators
x=26
y=14
print(x>y,x<y,x==y,x!=y,x>=y,x<=y)

#logical operators
print((x>y) and (x==y))
print((x>y) or (x==y))
print((x>y) and ( x!=y))

#bitwise operators 
num1=45
num2=4
print(num1&num2)
print(num1|num2)
print(num1^num2)
print(~num2)
print(num2<<2)
print(num2>>1)

#membership operators
l =[10,2,3,4,5,]
print(100 in l)
print(4 in l)
print(5 not in l)

#identity operators
x=5
y=5
print(x is y)
print(x is not y)
a=[1,2,3]
b=[1,2,3]
print(a is b)
print(a is not b)
