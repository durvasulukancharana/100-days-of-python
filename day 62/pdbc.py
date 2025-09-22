print('1.signup')
print('2.login')
print('3.exit')

choose=input('choose your option : ')


if choose=='1':
    from signup import signup
    signup()

if choose == '2':
    from login import login
    login()

import mysql.connector

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()

def signup():
    name=input('enter your name : ')
    password=input('enter your password here : ')
    cursorobj.execute('insert into bank(user_name,password) values(%s,%s)',(name,password))
    data.commit()
    print('your data added successfull...')

    cursorobj.execute('select * from bank where user_name=%s',(name,))
    x=cursorobj.fetchone()
    user_id,user_name,password=x
    bal=int(input('enter balance : '))
    cursorobj.execute('insert into accounts(user_id,account_bal) values(%s,%s)',(user_id,bal))
    data.commit()
    print('your account is created...')


import mysql.connector

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()

def login():
    name=input('enter your name : ')
    user_password=input('enter your password here : ')
    cursorobj.execute('select * from bank where user_name=%s',(name,))
    x=cursorobj.fetchone()
    # print(x)
    user_id,user_name,password=x
    if user_name==name and password==user_password:
        print('welcome to our bank...')
    
        print('1.check balance')
        print('2.withdraw')
        print('3.deposite')

        choose=input('choose your option : ')

        if choose=='1':
            cursorobj.execute('select * from accounts where user_id=%s',(user_id,))
            y=cursorobj.fetchone()
            id,num,bal=y
            print(f'your balance id {bal}')
        
        if choose=='2':
            cursorobj.execute('select * from accounts where user_id=%s',(user_id,))
            z=cursorobj.fetchone()
            id,num,bal=z
            money=int(input('enter your money : '))
            if money>bal:
                print('insufficient balance please check once...')
            if money<=bal:
                cursorobj.execute('update accounts set account_bal=account_bal-%s where user_id=%s',(money,id))
                data.commit()
                cursorobj.execute('select * from accounts where user_id=%s',(user_id,))
                z=cursorobj.fetchone()
                id,num,bal=z
                print(f'your remaining balance is {bal}')

        if choose=='3':
            cursorobj.execute('select * from accounts where user_id=%s',(user_id,))
            a=cursorobj.fetchone()
            id,num,bal=a
            amount=int(input('enter your deposite amount : '))
            cursorobj.execute('update accounts set account_bal=account_bal+%s where user_id=%s',(amount,user_id))
            data.commit
            cursorobj.execute('select * from accounts where user_id=%s',(user_id,))
            a=cursorobj.fetchone()
            id,num,bal=a
            print(f'your total balance is {bal}')
  