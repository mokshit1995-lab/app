def my_func(number):
  for num in range(1,number,1):
    if num % 2 == 0:
        print(num)
        num =+num
    



my_func(5)

a=0o23335
print((a))

b=0b11010
a=str(b)
print("Binary number for",a, "is",b)

a='mokshit'
print(a[:])

name = "Alex"
s = f"Hello, {name}!"
print(s)


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
print(txt1 is txt2)

print(int(123.412))
print(int(0Xafcef))
s='mokshit'
print(len(s))
a=0o12421
print(int(a))
b=[10,20,24,5]
c=bytes(b)
print(c)

m=(10,20,10,40) #tuple
l=[10,20,10,50] #List
n={10,20,30,10,50} #set
print(type(m))
print(type(l))
print(type(n))
l.append(10)
l.append(20)
l.append(40)
l.append(10)
l.append('mokshit')
l.append(None) 
l.remove(10)
l1=l*3
print(l1[-1])

r=range(10,30,5)
for i in r:
   print (i)
print(r[0:3])
print(r[2])
print(n)

s={10,20,50,20}
fs=frozenset(s)
#fs.add(50) not allowed immutable
#fs[2:3] frozenset is not subscriptable
#fs[3] not allowed
print(fs)

#Dictionary
d={100:'mokshit',200:'gunti',300:'king'}
print(d)
d1={}
d1[100]='sunny'
d1[200]='bunny'
d1[300]='dummy'
print(type(d1))
print(d1)

for i in d1:
   print("key={0}, value={1}".format(i,d1[i]))

for key in d1:
   print("key={key}, value={value}".format(key=key,value=d1[key]))
  
x=5
a='*'
b=' '
#for i in range(1,x+1):
#   print(b*(x-i) ,a*i)

def f1():
   print("hello world!!")
  
f1()

def f2():
   a=10

print(f2())
s='mokshit\ngunti' 
print(s)

a=10
b=2
print("a+b=",a+b)
print("a-b=",a-b)
print("a*b=",a*b) 
print("a/b=",a/b) #return float value
print("a%b=",a%b) #returns reminder
print("a//b=",a//b) #if arguments are int then returns int value
print("a**b=",a**b)

#import keyword
#print(keyword.kwlist)