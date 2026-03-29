#Dictionary
d1= { "brand": "Ford", 
     "Model":"Mustang",
     "year": 1987,
     "year": 1995}

print(d1)

print(d1["year"])

print(len(d1))

d2= { "brand": "Ford", 
     "Model":"Mustang",
     "year": 1987,
     "colour":["yellow","black",'Blue'],
     "year": 1995}

print(d2)

print(d2["colour"])

d=dict(name='Mokshit',age=12,country="India")
print(d)

x=d["name"]
print(type(x))

x=d.get("age")
print(x)

y=d.keys()
print(y)

d['Address'] ='USA'

print(y)

v=d.values()
k=d.keys()
print(f'keys{k} and Values {v}')

s=d.items()
print(s)

if 'country' in d:
    print('Country is in the dictionary')

d['Address']='Koti'
print(d)

d.update({'Address':"LOL"})
print(d)

d['colour']='Fair'
print(d)

d.update({'car':'Yes'})

print(d)

d.pop("Address")
print(d)

d.popitem()
print(d)

del d['colour']
print(d)

del d

d1=dict(name="mokshit",phone=1100,address='Jubliee')
print(d1)

d2={ 'name': "Mokshit", 'class': 'Upper', 'bike':'R1'}
print(d2)

d2['class']='Higher'
d2.update({'car':"Creta"})
d2['House']='Jubliee'
print(d2)