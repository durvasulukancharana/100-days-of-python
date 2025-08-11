'''append'''
fruit=['mango','banana']
fruit.append('apple')
print(fruit)

fruit=['mango','banana']
fruit.append(['apple','goa'])
print(fruit)

fruit=['mango','banana']
fruit.append(['apple','goa',['musk melon',['wter melon']]])
print(fruit)

'using tuple in append'
fruit=['mango','banana']
fruit.append(('apple',('goa',('grape',('musk melon')))))
print(fruit)

num=[1,2,3,4]
num.append(5)
print(num)

num=[1,2,3,4]
num.append([5,6])
print(num)


'''extend'''
x=[1,2,3,4]
y=[5,6,7]
x.extend(y)
print(x)

x=[1,2,3,4]
y=[5,6,7]
y.extend(x)
print(y)

x=[1,2,3,4]
x.extend([5,6,7])
print(x)

x=[1,2]
y=['a','b']
x.extend(y)
print(x)

x=['vamsi','ravi']
y=['kumar','ajay']
x.extend(y)
print(x)

x=['x','y','z']
y=['a','b','c']
x.extend(y)
print(x)

x=['x','y','z']
x.extend(['a','b','c'])
print(x)

x=['x','y','z']
x.extend('a')
print(x)


'''insert'''
x=[1,2,3,4]
x.insert(0,0)
print(x)

x=['ajay','vijay','kumar']
x.insert(1,'ravi')
print(x)

x=[1,2,3,4]
x.insert(0,'ajay')
print(x)

x=['ajay','vijay','kumar']
x.insert(1,25)
print(x)

x=['ajay','vijay','kumar']
x.insert(1,25.0)
print(x)


'''remove'''
x=[1,2,3,4,5,1]
x.remove(1)
print(x)

x=['ajay','vijay','kumar','kumar']
x.remove('kumar')
print(x)

x=[1,2,'ajay','vijay',True,25.09]
x.remove('ajay')
x.remove(25.09)
print(x)