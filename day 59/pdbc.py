import mysql.connector

def db_connection():
    return mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='empmansys'
)

print('database is connected successfully...')


from crudoperation import add_employe
print('1.add_employe')
print('2.view_employe')
print('3.delete_employe')
print('4.update_employe')
print('5.exit_employe')

choose_option=int(input('choose one option to proceed... : '))

if choose_option==1:
    emp_name=input('enter emp_name : ').strip()
    emp_sal=float(input('enter emp_sal : '))
    emp_dept=input('enter emp_dept : ').strip()
    emp_loc=input('enter emp_loc : ').strip()
    add_employe(emp_name,emp_sal,emp_dept,emp_loc)


    from dbconnection import db_connection
def add_employe(n,s,d,l):
    # print('emp added successfully...')
    db_connect=db_connection()
    # print(db_connect)
    cur = db_connect.cursor() # ---> it wil helps us to communicate with database in our workbench
    cur.execute('insert into employees(emp_name,emp_sal,emp_dept,emp_loc) values(%s,%s,%s,%s)',(n,s,d,l))
    db_connect.commit()
    db_connect.close()
    print(f'{n} employee added successfullyyy..')