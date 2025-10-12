accounts = [
 {"name": "Ravi", "balance": 5000, "pin": 1234, "transactions": []},
 {"name": "Priya", "balance": 7000, "pin": 2345, "transactions": []},
 {"name": "Suresh", "balance": 10000, "pin": 3456, "transactions": []},
 {"name": "Anita", "balance": 3000, "pin": 4567, "transactions": []},
 {"name": "Kiran", "balance": 8500, "pin": 5678, "transactions": []},
 {"name": "Meena", "balance": 12000, "pin": 6789, "transactions": []},
 {"name": "Vamsi", "balance": 4500, "pin": 7890, "transactions": []},
 {"name": "Rohit", "balance": 6000, "pin": 8901, "transactions": []},
 {"name": "Sonia", "balance": 9000, "pin": 9012, "transactions": []},
 {"name": "Neha", "balance": 11000, "pin": 1122, "transactions": []}
]


# check balance :
def check_balance(name,pin):
    for i in range(len(accounts)):
        if accounts[i]['name']==name and accounts[i]['pin']==pin:
            print(accounts[i]['balance'])
            break
        else:
            print('wrong data entered...')


# deposite money
def depo_amount(name,pin,amount):
    for i in range(len(accounts)):
        if accounts[i]['name']==name and accounts[i]['pin']==pin:
            accounts[i]['balance']+=amount
            accounts[i]['transactions'].insert(0,amount)
            print(accounts[i]['balance'])
            print(accounts[i]['transactions'])
            print('deposite successfully')


# withdraw amount
def withdraw_amount(name,pin,amount):
    for i in range(len(accounts)):
        if accounts[i]['name']==name and accounts[i]['pin']==pin and accounts[i]['balance']>=accounts[i]['balance']:
            accounts[i]['balance']-=amount
            accounts[i]['transactions'].insert(0,amount)
            print(accounts[i]['balance'])
            break
        #     x=i
        #     break
        # else:
        #     print('invalid data')

        # if accounts[x]['balance']>amount:
        #     accounts[x]['balance']-=amount
        #     print(accounts[x]['balance'])
        #     print('withdraw successfully...')

        else:
            print('insufficient balance...')


# transaction history
def history(name,pin):
    for i in range(len(accounts)):
        if accounts[i]['name']==name and accounts[i]['pin']==pin:
            print(accounts[i]['transactions'])
            break
        else:
            print('invalid info')

while True:
    print('===== ATM Machine ===== ')
    print('1. Check Balance') 
    print('2. Deposit Money')
    print('3. Withdraw Money') 
    print('4. Transaction History') 
    print('5. Exit\n')

    option=int(input('select one number from above : '))

    if option==1:
        name=input('enter your name : ').capitalize().strip()
        pin=int(input('enter your pin here : '))
        check_balance(name,pin)

    if option==2:
        name=input('enter your name : ').capitalize().strip()
        pin=int(input('enter your pin here : '))
        amount=int(input('enter your depo amount : '))
        depo_amount(name,pin,amount)

    if option==3:
        name=input('enter your name : ').capitalize().strip()
        pin=int(input('enter your pin here : '))
        amount=int(input('enter your withdraw amount : '))
        withdraw_amount(name,pin,amount)

    if option==4:
        name=input('enter your name : ').capitalize().strip()
        pin=int(input('enter your pin here : '))
        history(name,pin)

    if option==5:
        print('thank you for visiting...')
        break

