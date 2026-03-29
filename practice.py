import math as mt
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

""" print("length of command line arguements:",len(argv))
print(argv[0])


def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry')) """

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

#l=[1,20,40]
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

""" n=int(input("Enter a numbder:"))
sum=0
i=1
while i<=n:
  sum=sum+i
  i+=1
print(sum) """

""" name='' 
psd=''
while name!='durga' or pwd!='python':
  name=input("Enter name:")
  pwd=input("Enter pasword:")
print("Hi Durga thanks for confirmation")
 """

#n=int(input("Enter a num:"))
""" for i in range(1,n+1): #i is rows
  for j in range(1,i+1): #j is column
    print("* ",end='') # to print * in same line
  print() # will go to next line at end of j execution """

""" n=int(input("Enter a num:"))
for i in range(1,n+1):
  for j in range(1,n+1):
    print("*",end=' ')
  print() """

#This is for diamond shape
""" for i in range(1,n+1):
  print(" "*(n-i),end='')
  print("* "*i)

for j in range(n-1,0,-1):
  print(" "*(n-j),end='')
  print("* "*j) """


""" for i in range(1,n+1):
 print(" "*(n-i),end="")
 for j in range(i,i+1):
  print("*",end=' ')
  if i>=2:
   print(" "*(2*i-4),end='')
   for k in range(i,i+1):
    print("*",end='')
 print()
 """
""" 
s=input("enter a string:")
rev_str=s[::-1]
print(rev_str)

if rev_str == s:
  print("ITs a palin")
else:
  print("Not Palin")

 """

""" def factorial(n):
  if n == 0:
    return 1
  else :
    return n * factorial(n-1)
  

print(factorial(5)) """


""" def find_largest(n):
  largest=n[0]
  for num in n:
    if num > largest:
      largest = num
  return largest

print(find_largest([10,20,40,20,50,60]))
 """

newlist=[ x for x in range(10) if x % 2 == 0]
print(newlist)
""" 
newlist1=[]

for i in range(len(newlist)):
    if i == 0:
        a=newlist[i]
    elif i == len(newlist) -1 :
        b=newlist[i]

newlist[-1]=a
newlist[0]=b
print(newlist) """


newlist[0],newlist[-1] = newlist[-1],newlist[0]
print(newlist)

sum=0
p=1
for i in newlist:
    sum = sum + i
    p = p * i

print(f"sum is {sum}")
print(f"product is {p}")
print(f"avg is {sum/2}")


l1=[1,2,3,5,6,5,5,3,1,3,5,6]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)

l1=[10,2,25,255,21,2051,521]
largest=l1[0]
sec_larg=0

for i in range(len(l1)):
    if l1[i] > largest:
        largest=l1[i]
print(largest)


l1=[10,2,25,255,21,2051,521]
l1.sort()
print(l1[-2])


l1=[10,2,25,255,21,2051,521,135,356,1010,199,200]
largest = sec_larg = float('-inf')

for num in l1:
    if num > largest:
        largest=num
    elif num > sec_larg and num != largest:
        sec_larg = num
print(sec_larg) 


l1=['p', 'y', 't', 'h', 'o', 'n']
s=''
for i in l1:
   s = s + i 

print(s)

l1=[0,1,500,205,210,505,201,603,954]
even=[]
odd=[]

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)

l1=[ x**2 if x % 2 == 0 else x**3 for x in range(1,21) ]
print(l1)

l1=[[1,2],[3,4]]
l2=[]
for x in l1:
    for y in x:
        l2.append(y)

print(l2)

l1=[5,10,15,20,25,50,20]
c=0
for i in range(len(l1)):
    if l1[i] == 20:
        l1.insert(i,200)
        c=c+1
    if c == 1:
      break
    
print(l1)

l1[l1.index(20)]=200
print(l1)

l1=[10,2,25,255,21,2051,521,135,356,1010,199,200]
largest = float('-inf')
smallest = l1[0]
for i in l1:
    if i > largest:
        largest=i

for i in l1:
    if i < smallest:
        smallest=i

print(largest)
print(smallest)
print(f'Range of min and max is {smallest} - {largest}')

my_list = [100, 4, 200, 1, 3, 2,9,11,12,10,15,13,16,14]
my_list.sort()
print(my_list)
start=0
count=0
l2=[]
for i in my_list:
    if i > start:
      if i == start+1:
          count +=1
          start=i
      else :
          l2.append(count)
          count = 1
          start = i

print(max(l2))


l=[1,3,4,5,1,2,5,2]
newl=[]

for i in l:
    if i not in newl:
        newl.append(i)


print(newl)
new1=list(l)
print(f'Copied list is:{new1}')

def com(a,b):
    for i in a:
        for j in b:
            if i == j:
                print(True)
                break
            
com([1,2,4,5],[2,7,8,10])

from random import shuffle
shuffle(l)
print(l)

import math

def prime(a):
      b=0
      if a <= 1:
        return False
      if a == 2:
        return True
      else:   
        b=int(math.sqrt(a))
        for n in range(3, b+1,2):
            if a % n == 0:
                return False
        return True
            
def test(nums):
    result = [prime(i) for i in nums]
    return all(result)

print(test([5,7,11,17,624]))


""" l1=['Red','Green','Black','White','Pink','Yellow']
l1.pop(0)
print(l1) """

import itertools

print(list(itertools.permutations([1,2,3])))

l1=[1,3,5,7,9]
l2=[1,2,4,6,7,8]

diff_l1_l2 = list(set(l1) - set(l2))
diff_l2_l1 = list(set(l2) - set(l1))

tot_diff= diff_l1_l2 + diff_l2_l1
print(diff_l1_l2)
print(diff_l2_l1)
print(tot_diff)

l1=['asfsf','dgdg','agdgd']
st1=''.join(l1)
print(st1) 

import itertools
l1=[[2,4,5,],[2,5,6,],[9],[0,5,2]]
l2=list(itertools.chain(*l1))
print(l2)

l1=[1,4,5,6]
l2=[6,6,7,1]

l3=list(l1+l2)
print(l3)



def sec_small(l1):
  smallest= sec_small= float('inf')
  for i in l1:
      if i < smallest:
        sec_small=smallest
        smallest = i
      elif i < sec_small and i != smallest:
          sec_small = i 
  return sec_small

l1=[1,4,5,6]
print(sec_small(l1))

l1=[10,50,20,10,50,20,50,60,90]
l2=set(l1)
l3=list(l2)
print(l3)

import collections
l1=[10,50,20,10,50,20,50,60,90]
ctr = collections.Counter(l1)
print(ctr)

l1=[10,50,20,10,50,20,50,60,90]
d=dict()
count=0

for i in l1:
    count=0
    for j in l1:
        if i == j:
            count+=1
            d[i] = count
print(d)

l1=[10,50,20,50,60,10,50,30,52,24,30,64]
count=0
for i in l1:
    if 30 <= i <= 60:
        count+=1
print(count)

l1=['X','Y']
n=5
l2=[]
a=''
for i in range(1,n+1):
    for j in l1:
        k = str(i)
        a = j + k
        l2.append(a)

print(l2)  


a= 'string'
print(id(a))


l1=[1,3,5,7,9]
l2=[1,2,4,6,7,8]
l3=[1,2,125,122,657,124]
common = list((set(l1) & set(l2) & set(l3)))
print(common)

l1=[0,1,2,3,4,5]
l2=[]

for i in range(1,(len(l1)+1),2):
    l2.append(l1[i])
    l2.append(l1[i-1])

print(l2)

l1=[0,1,2,3,4,5]

a= int("".join(map(str,l1)))

print(a)

l1 = [1,2,4,5]
a,b,c,d=l1
print(a)

print(l1[::-1])


l1 = [1,2,4,5]
l2=[10,20,40]
l1[:0]=l2
print(l1)

#Set
s1={'apple','banana',True,1,False,0}
print(s1)

for x in s1:
    print(x)

print('banana' in s1)

s1.add('orange')
print(s1)

s2={'pineapple','mango','papaya'}

s2.update(s1)

print(s2)

l2=['kiwi','watermelon']

s2.update(l2)
print(s2)

s2.remove('kiwi')
print(s2)

#Remove will raise error if item is not present in set

s2.discard('car')
print(s2)

#Discard will not raise error if item is not present in set.

#s2.clear()
print(s2)

#Clear will clear the set and return empty set

del s2

s1={1,2,3,4,5}
s2={6,7,8,9,10}
s3={'a','b','c'}
s4=s1.union(s2,s3)
s4 = s2 | s1 | s3
print(s4)

s1.update(s3)
print(s1)


s1={1,2,3,6,7}
s2={6,7,8,9,10}
s4={6,7,8}
s3=s1.intersection(s2,s4)
s3= s1 & s2 & s4
print(s3)

s1.intersection_update(s2)
print(s1)

s1={1,2,3,6,7}
s2={6,7,8,9,10}
s4={6,7,8}
s3=s1.difference(s2)
s3=s1.symmetric_difference(s2)
s3 = s1 ^ s2
print(s3)

s1=frozenset({'a','b','c'})
print(s1)
print(type(s1))