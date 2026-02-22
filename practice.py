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

#number=int(input("Enter a number:"))
#a=number+1
#for num in range(1,number+1):
#  print(' '*(a-2),'*'*(num))
#  for num1 in range(2,number+1):
#    print(' '*(num1-1),num1*" *")

""" x=int(input("Enter a number:"))
c=2
for a in range(1,x+1):
  d=x-c
  if a == x: d=a-x
  print((d)*' ',' *'*a)
  c=c+1 """
""" 
brand=input("Enter brand:")

if brand=="KF":
  print("Its too light")
elif brand=="KO":
  print("Its to strong")
elif brand=="BD":
  print("Recommended")
else:
  print("Other brands not recomended")
   """
""" n1=eval(input("Enter 1st number:"))
n2=eval(input("Enter 2nd number:"))
n3=eval(input("Enter 3nd number:"))
if n1>n2 and n1>n3:
  print("Bigger number is:",n1)
elif n2>n1 and n2>n3:
  print("Bigger number is:",n2)
else:
  print("Bigger number is:",n3) """


""" n=input("Enter string:")
i=0
for a in n:
  if i!=0:
    print("The character present at {0} index is {1}".format(i,a))
  i+=1 """

""" for x in range(10,0,-1):
    print(x) """

""" l=eval(input("Enter some list:"))
sum=0
for x in l:
  sum=sum+x
print("Sum of list is:",sum)
 """

