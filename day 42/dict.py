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
max_key = min(scores, key=scores.get)
print("Key with maximum value:", max_key)
print("Maximum value:", scores[max_key])

scores={'name':'markonda_patnaikuniganesh',
        'name2':'botsa_raviteja',
        'name3':'panchireddy_charan_kumar'
        }
min=float('inf')
for i,j in scores.items():
    if len(j)<min:
        min=len(j)
print(min)
for i,j in scores.items():
    if len(j)==min:
        print(i,j)

scores={'name3':'markonda_patnaikuniganesh',
        'name2':'botsa_raviteja',
        'name':'panchireddy_charan_kumar',
        'name4':'markonda_patnaikuniganesh'
        }
max=0
for i,j in scores.items():
    if len(j)>max:
        max=len(j)
print(max)
for i,j in scores.items():
    if len(j)==max:
        print(i,':',j)