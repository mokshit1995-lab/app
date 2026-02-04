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

l=[]
print(type(l))
l.append(10)
l.append(20)
l.append(40)
l.append(10)
l.append('mokshit')
l.append(None)
l.remove(10)
print(l)
#import keyword
#print(keyword.kwlist)