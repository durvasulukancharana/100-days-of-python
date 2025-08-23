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


'''pop'''
x=[1,2,3,4,5]
x.pop()
print(x)

x=[1,2,3,4,5]
x.pop(2)
print(x)

x=['ajay','vijy','vamsi','ravi']
x.pop()
print(x)

x=['ajay','vijy','vamsi','ravi']
x.pop(2)
print(x)


'''clear'''
x=[1,2,3,4,5]
x.clear()
print(x)

x=['apple','cat','ball']
x.clear()
print(x)


'''index'''
x=[1,2,3,4,5,6,7,8]
print(x.index(5))

x=(10,20,30)
print(x.index(30))

x=['vamsi','ravi','ajay','kumar']
print(x.index('ajay'))

x=('vamsi','ravi','ajay')
print(x.index('ravi'))

x='vamsi'
print(x.index('m'))


'''count'''
x=[1,2,3,4,1,2,3,1,1]
print(x.count(1))

x='palavalasapeta'
print(x.count('a'))

x=('palavalasapeta')
print(x.count('p'))


'''reverse'''
x=[1,2,3,4,5]
x.reverse()
print(x)

x=['palasa','bobbili','p_puram']
x.reverse()
print(x)


'''copy'''
x=[1,2,3]
print(x.copy())

x=['vamsi','ravi','kumar']
print(x.copy())


'''shallowcopy'''
original = [1, 2, 3]
shallow = original.copy() 
# print(shallow)
shallow.append(4)
print("Original:", original) 
print("Shallow:", shallow)   

x=[1,2,3,4,5]
shallow=x.copy()
shallow.append(6)
print(shallow)
print(x)
print(id(shallow))

original = [1, [2, 3], 4]
shallow = original.copy()
shallow[1][0] = 99  # Change inside nested list
print("Original:", original)  # [1, [99, 3], 4]
print("Shallow:", shallow)    # [1, [99, 3], 4]


x=[1,2,[1,2],[1,2]]
shallow=x.copy()
shallow[3][0]=9
shallow[3][1]=25
print(shallow)
print(x)

x=['vamsi','ravi','ganesh']
shallow=x.copy()
shallow[2]='ravi'
print(shallow)
print(x)