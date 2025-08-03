# patterns:

for i in range(5):
    for j in range(i+1):
        print('*',end='')
    print()
    
    
for i in range(5):
    for k in range(5-i):
        print('',end='')
    for j in range(i):
        print('*',end='')
    print(end='\n')


n=int(input("enter a num:"))
for i in range(n+1):
    for j in range(i):
        print(j+1,end=" ")
    print()
        

n=int(input("enter a num:"))
for i in range(n+1):
    for j in range(i):
        print(i,end=" ")
    print()  


n=int(input("enter a num :"))
for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print()
    

for i in range(5):
    for j in range(i+1):
        print(j+1,end=' ')
    print()
    

for i in range(5):
    for j in range(i+1):
        print(i+1,end=' ')
    print()


for i in range(5):
    for j in range(i,-1,-1):
        print(j+1,end=' ')
    print()
    

for i in range(5):
    for j in range(i,-1,-1):
        print(5-i,end=' ')
    print()


for i in range(5):
    for j in range(i+1):
        print(5-j,end=' ')
    print()


for i in range(5):
    for j in range(i,-1,-1):
        print(5-j,end=' ')
    print()
    

for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print(i+1,end='')
    print()
    

for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print(j+1,end='')
    print()

    
for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print(k+1,end='')
    print()


for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print(5-i,end='')
    print()

    
for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print(5-j,end='')
    print()
    

for i in range(5):
    for j in range(5-i):
        print('',end=' ')
    for k in range(i+1):
        print(5-k,end='')
    print()
    

x=int(input("enter a num :"))
for i in range(1,x):
    for j in range(i):
        print(i,end=' ')
    print()