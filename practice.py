import math as m
from math import *
from sys import *
#print(sqrt(16))
#print(pi)
#r=5


#r=int((input("Enter radius of circle:")))
#print("Area of Circle is :", pi*(pow(r,2)))


#a,b=[int (x) for x in input("Enter 2 Numbers:").split(sep=',')]
#print("Sum of 2 numbers is :", a+b)

#x=eval("10+13+12")
#print(x)

#ex=input("enter a expression:")
#result=eval(ex)
#print("The result:",result)


#a=eval(input("Enter the data:"))
#print(type(a))
#print(a)

#a,b,c=[eval(x) for x in input("enter 3 args:").split()]
#print(type(a))
#print(type(b))
#print(type(c))
#print(type(argv))

print("length of command line arguements:",len(argv))
print(argv[0])


def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

#l=[10,20,50]
#print(510 not in l)

#s="Hellow learning python is easy"
#print ("Hellow" in s )

#a,b=[int(x) for x in input("Enter 2 numbers:").split()]
#
#print("The product of 2 numbers is:", a*b)

#print("Hello",end=' ')
#print("Hello",end=' ')
#print("Hello",end='...')
#print(10,30,50,15,sep='-')

l=[1,20,40]
t=(10,50,20)
s={10,50,20}
#print(l)
#print(t)
#print(s)
a=10

#print("a value is %i" %a)

name='mokshit' 
salary=1000
gf='shamili'
#Replacement operator
#print("Hello {0} your gf {1} is waiting for salary {2}".format(name,gf,salary))
#print("Hello {} your gf {} is waiting for salary {}".format(name,gf,salary))
#print("Hello {n1} your gf {n2} is waiting for salary {n3}".format(n1=name,n2=gf,n3=salary))

number=int(input("Enter a number:"))
a=number
for num in range(1,number+1):
  print(' '*(a-2),'*'*(num))
  for num1 in range(2,number+1):
    print(' '*(num1-1),num1*" *")

