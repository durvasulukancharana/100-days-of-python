# 10.Convert a string to title case without using .title().

name='we are learning python'
name=name.split(' ')
new=''
for i in name:
    new+=i[0].upper()+i[1:len(i)]+' '
print(new)

name='we are learning python'
name=name.split(' ')
new=''
for i in name:
    new+=i.capitalize()+' '
print(new)