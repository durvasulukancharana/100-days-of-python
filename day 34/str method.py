'''lower'''
x='VAMSI'
y=x.lower()
print(y)

x='vamsi'
print(x.lower())


'''upper'''
y='ganesh'
x=y.upper()
print(x)

x='ganesh'
print(x.upper())


'''strip'''
x='   hello   '
y=x.strip()
print(y)

x='  hii  '
print(x.strip())


'''replace'''
x='i like apple'
y=x.replace('apple','water_melon')
print(y)

x='i like apple'
print(x.replace('apple','banana'))


'''split'''
x='apple,banana,grapes'
y=x.split(',')
print(y)

x='apple,banana,grapes'
print(x.split(','))


'''join'''
x='i','love','my','parents'
y=' '.join(x)
print(y)

x='i','love','my','parents'
print(' '.join(x))

x='hi hello how are you'
y=x.split()
print(y)
z=''.join(y)
print(z)
a='-'.join(z)
print(a)


'''find'''
x='hi hello how are you'
y=x.find('are')
print(y)

x='hi hello how are you'
print(x.find('hello'))

'''startswith'''
x='hello'
y=x.startswith('h')
print(y)

x='hello'
print(x.startswith('h'))

x='hello'
y=x.startswith('H')
print(y)


'''endswith'''
x='vamsi'
y=x.endswith('v')
print(y)

x='vamsi'
print(x.endswith('i'))


'''isdigit'''
num='10'
x=num.isdigit()
print(x)

num='x'
print(num.isdigit())


'''isalpha'''
x='vamsi'
y=x.isalpha()
print(y)

x='vamsi'
print(x.isalpha())


'''isalnum'''
y='5'
print(y.isalnum())

x='x'
print(x.isalnum())

z='*'
print(z.isalnum())


'''isspace'''
x=' '
print(x.isspace())

x=' x '
print(x.isspace())


'''title'''
x='iam learning python'
print(x.title())

x=['i','am','ok']
y=(' '.join(x))
print(y.title())


'''capitalize'''
x='yeah im okay'
print(x.capitalize())

x=['yeah im okay']
y=' '.join(x)
print(y.title())


'''count'''
x='banana'
print(x.count('a'))

x='banana'
print(x.count('x'))
        

'''len'''
x='hello'
print(len(x))


'''swapcase'''
x='hELlo WOrlD'
print(x.swapcase())