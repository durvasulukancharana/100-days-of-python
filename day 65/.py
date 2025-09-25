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
    role=input('enter your role (user/admin) : ')
    cursorobj.execute('insert into bank(user_name,password,role) values(%s,%s,%s)',(name,password,role))
    data.commit()
    print('your data added successfull...')

    cursorobj.execute('select * from bank where user_name=%s',(name,))
    x=cursorobj.fetchone()
    user_id,user_name,password,role=x
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
    user_id,user_name,password,role=x
    if role=='user':
        if user_name==name and password==user_password:
            print('welcome to our bank...')
        
            print('1.check balance')
            print('2.withdraw')
            print('3.deposite')
            print('4.request')

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

            if choose=='4':
                print('1.loan  2.atm_card  3.check_book  4.net_banking')
                req_type=int(input('enter your req number : '))
                if req_type==1:
                    req='loan'
                    from request import requestRaise
                    requestRaise(user_id,req)

                if req_type==2:
                    req='atm_card'
                    from request import requestRaise
                    requestRaise(user_id,req)

                if req_type==3:
                    req='check_book'
                    from request import requestRaise
                    requestRaise(user_id,req)

    if role=='admin':
        print('--- admin menu ---')
        print('1.delete account')
        print('2.search customer')
        print('3.view all request')
        print('4.view accounts')
        print('5.managing request')
        select=input('choose one from above : ')
        if select=='2':
            from search import searchCustomer
            searchCustomer()
        
        if select=='1':
            from delete import deleteCustomer
            deleteCustomer()

        if select=='3':
            from all_requests import viewallrequest
            viewallrequest()

        if select=='5':
            from managereq import manageRequest
            manageRequest()


import mysql.connector
from all_requests import viewallrequest

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()

def manageRequest():
    allreq=viewallrequest()
    print(allreq,'all_requests')
    name,req_type,bal,status=allreq 
    inp=input('enter your request type pending , approved , accepted: ')
    if status == inp:
        print(' already approved ')


import mysql.connector

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()

def viewallrequest():
    # inp=input('enter your request type (loan,atm_card,check_book,net_banking) : ')
    cursorobj.execute('''
    select bank.user_name,request.req_type,request.req_bal,request.req_status
    from bank left join request using(user_id)
    ''')
    allreq=cursorobj.fetchall()
    print(allreq)
    return allreq


import mysql.connector

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()

def deleteCustomer():
    enter_user_id=int(input('enter user id for delete account : '))
    cursorobj.execute('delete from request where user_id=%s',(enter_user_id,))
    cursorobj.execute('delete from accounts where user_id=%s',(enter_user_id,))
    cursorobj.execute('delete from bank where user_id=%s',(enter_user_id,))    
    data.commit()
    print('deleted successfully...')
    

import mysql.connector

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()


def searchCustomer():
    cursorobj.execute('select * from bank inner join accounts using(user_id) inner join request using(user_id)')
    id=int(input('enter user_id : '))
    x=(cursorobj.fetchall())
    for i in x:
        if i[0]==id:
            print(i)


import mysql.connector

data=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='banking'
)

cursorobj=data.cursor()

def requestRaise(user_id,req):
    amount=int(input('enter your amount how much you want : '))
    cursorobj.execute('insert into request(user_id,req_type,req_bal) values(%s,%s,%s)',(user_id,req,amount))
    data.commit() 