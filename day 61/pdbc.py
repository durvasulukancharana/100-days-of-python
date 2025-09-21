import mysql.connector

data_base=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Durvasulu@25',
    database='bcci'
)
print('databse created successfully...')

x=data_base.cursor()

print('1.add')
print('2.update')
print('3.view')
print('4.delete')

choose=input('choose your option : ')


if choose=='1':
    name=input('enter player name : ')
    role=input('enter player role : ')
    x.execute('insert into players(player_name,player_role) values(%s,%s)',(name,role))
    data_base.commit()

if choose=='2':
    role=input('enter player role : ')
    name=input('enter player name : ')
    x.execute('update players set player_role=%s where player_name=%s',(role,name))
    data_base.commit()
    print('update ')

if choose=='4':
    name=input('enter player name : ')
    x.execute('delete from players where player_name=%s',(name,))
    data_base.commit()
    print('deleted successfully...')

if choose=='3':
    x.execute('select * from players')
    y=x.fetchall()
    print(y)