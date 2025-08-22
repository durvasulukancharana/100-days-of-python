'''dictionary'''

info={
    'name':'apna college',
    'sub':['python','c','c++'],'topics':('dict','list'),
    'age': 35,'is adult':True,
    12.9:0.09
}

info['name']='vamsi'
info['surname']='enduri'
print(info)

student={
    'name':'rahul',
    'subjects':['phy=90','chem=40','eng=99']
}
print(student['subjects'])


'''nested dict'''

student={
    'name':'rahul',
    'subjects':{
        'phy':'99',
        'eng':'90',
        'chem':'98'
    }
}
print(student['subjects']['eng'])

student={
    'name':'rahul',
    'subjects':{
        'phy':'99',
        'eng':'90',
        'chem':'98'
    }
}
print(student.values())
print(len(student))

info={
    'name':'apna college',
    'sub':['python','c','c++'],'topics':('dict','list'),
    'age': 35,'is adult':True,
    12.9:0.09
}
# print(info.values())
print(info.keys()) 
print(len(info))

student={
    'name':'rahul',
    'subjects':{
        'phy':'99',
        'eng':'90',
        'chem':'98'
    }
}
pairs=tuple(student.items())
print(pairs[0])
print(student.items())

student={
    'name':'rahul',
    'subjects':{
        'phy':'99',
        'eng':'90',
        'chem':'98'
    }
}
print(student.get('name1'))

student={
    'name':'rahul',
    'subjects':{
        'phy':'99',
        'eng':'90',
        'chem':'98'
    }
}
print(student['name1'])

student={
    'name':'rahul',
    'subjects':{
        'phy':'99',
        'eng':'90',
        'chem':'98'
    }
}
new_dict={'name':'prasanna','age':16}
student.update(new_dict)
print(student)


'''hash values in set'''

dictionary={
    'table':['a piece of furniture','list of facts'],
    'cat':'a small animal',
    'virat':83
}
print(dictionary)


marks={}
x=int(input('physics marks:'))
marks.update({'physics':x})

y=int(input('math marks:'))
marks.update({'math':y})

z=int(input('chem marks:'))
marks.update({'chem':z})

marks.update({'all pass':'yess'})

print(marks)

values ={(9.0),('9')}
print(values)

values={9,'9.0'}
print(values)


# Create a dictionary to store names of 3 friends and their ages.
friends={
    'teja':23,
    'ganesh':23,
    'charan':23
}
print(friends)


# Access the value of a given key in a dictionary.
value={'name':'vamsi','age':28,'from':'ongole'}
print(value.get('class'))

value={'name':'vamsi','age':28,'from':'ongole'}
print(value.get('name'))


# Add a new key–value pair to an existing dictionary.
new={
    'name':'vamsi',
    'age':29
}
new.update({'name':"ajay"})
print(new)

new={
    'name':'vamsi',
    'age':29
}
new['sex']='male'
print(new)


# Update the value of an existing key.
name={'hii':123}
name.update({'hii':321})
print(name)


# Remove a key–value pair using pop().
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli'
}
key.pop('village')
print(key)


# Remove the last inserted key–value pair using popitem().
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli',
    'lover':'sailu'
}
key.popitem()
print(key)


# Check if a key exists in a dictionary using in.
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli',
    'lover':'sailu'
}
x='name' in key
print(x)


# Get all keys from a dictionary using keys().
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli',
    'lover':'sailu'
}
print(key.keys())


# Get all values from a dictionary using values().
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli',
    'lover':'sailu'
}
print(key.values())


# Get all items (key–value pairs) using items().
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli',
    'lover':'sailu'
}
print(key.items())


# Merge two dictionaries into one.
key={
    'name': 'pablo',
    'age':23
}
value={
    'village':'bobbli',
    'lover':'sailu'
}
key.update(value)
print(key)


# Create a dictionary from two lists using zip().
x={'name','age'}
y={'ganesh',22}
z=dict(zip(x,y))
print(z)

x={'name','age'}
y={'ganesh',22}
z=dict(zip(x,y))
print(z.items())


# Create a dictionary using dict() constructor.
new=dict(name='vamsi',age=29,to='ongole')
print(new)


# Use get() to safely retrieve a value without an error.
key={
    'name': 'pablo',
    'age':23,
    'village':'bobbli',
    'lover':'sailu'
}
print(key.get('age'))


# Iterate through a dictionary’s keys and values.
x={'name':'ganesh','age':23}
for key,values in x.items():
    print(key, "-" ,values)


#  Find the key with the maximum value in a dictionary.
scores={'name':'markonda_patnaikuniganesh','name2':'botsa_raviteja','name3':'panchireddy_charan_kumar'}
max_key = max(scores, key=scores.get)
print("Key with maximum value:", max_key)
print("Maximum value:", scores[max_key])

scores={'name':'markonda_patnaikuniganesh','name2':'botsa_raviteja','name3':'panchireddy_charan_kumar'}
# for x,y in scores.items():
min_value=min(scores,key=scores.get)
print(min_value)
print(scores[min_value])



# Find the key with the maximum value in a dictionary.
keys={
    'name': 5,
    'age':18,
    'village':30
}
max_key=min(keys,key=keys.get)
print(max_key)
print(keys[max_key])


# Count the frequency of each character in a string using a dictionary.
x='hello world'
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1
print(y)

x='palavalasapeta'
y={}
for i in x:
    if i not in y:
        y[i]=i
    else:
        y[i]+=i        
print(y)

x='palavalasapeta'
y={}
for i in x:
    if i not in y:
        y[i]=1
    else:
        y[i]+=1       
print(y)


# Swap keys and values in a dictionary.
x={'a':1,'b':2,'c':3}
swap={value:key for key,value in x.items()}
print(swap)

x={'name':'vamsi','age':28,'village':'ongole'}
y={value:key for key,value in x.items()}
print(y)


# Create a dictionary comprehension to square numbers from 1 to 5.
x={i**2 for i in range(1,6)}
print(x)


#  Remove all items from a dictionary using clear().
x={'name':'vamsi','age':28,'village':'ongole'}
print(x.clear)



max=-float('inf')
max=-float('inf')
x={
    'vamsi':50,
    'ajay':90,
    'kumar':55
}
for i,j in x.items():
    if j>max:
        max=j
# print(max)
for i,j in x.items():
    if j==max:
        print(i,j)

max=-float('inf')
x={
    'a':'vamsi',
    'b':'ajay',
    'c':'kumar',
    'd':'ganesh'
}
for i,j in x.items():
    if len(j)>max:
        max=len(j)
print(max)
for i,j in x.items():
    if len(j)==max:
        print(i,j)
