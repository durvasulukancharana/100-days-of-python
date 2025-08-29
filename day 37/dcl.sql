Microsoft Windows [Version 10.0.26100.4946]
(c) Microsoft Corporation. All rights reserved.

C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql -u root -h localhost -p
Enter password: ************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 37
Server version: 8.0.43 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| 51r                |
| 5r                 |
| a                  |
| crex               |
| data               |
| details            |
| emp                |
| employ             |
| employ_details     |
| employ_info        |
| employees          |
| employes           |
| employess          |
| emps               |
| hii                |
| information_schema |
| mine               |
| my_life            |
| my_profile         |
| mysql              |
| patients           |
| performance_schema |
| sai                |
| sys                |
| x                  |
| y                  |
| z                  |
+--------------------+
27 rows in set (0.06 sec)

mysql> use z;
Database changed
mysql> show tables;
+-------------+
| Tables_in_z |
+-------------+
| dept        |
| emp         |
| employ      |
| employes    |
+-------------+
4 rows in set (0.02 sec)

mysql> select * from employes;
+----+--------+--------+------+---------+
| id | name   | salary | age  | depart  |
+----+--------+--------+------+---------+
|  1 | ajay   |  30000 |   27 | boss    |
|  2 | mohan  |  23000 |   25 | trainer |
|  3 | kumar  |  24000 |   28 | trainer |
|  4 | ravi   |  27000 |   22 | trainee |
|  5 | ganesh |  25000 |   23 | employe |
|  6 | teja   |  29000 |   23 | employe |
+----+--------+--------+------+---------+
6 rows in set (0.00 sec)

mysql> create user 'ajay'@'localhost' identified by 'ajay123';
Query OK, 0 rows affected (0.03 sec)

mysql> grant select on employes to 'ajay'@'localhost';
Query OK, 0 rows affected (0.02 sec)

mysql> grant all privileges on employes to 'ajay'@'localhost';
Query OK, 0 rows affected (0.02 sec)

mysql> revoke select,insert on employes from 'ajay'@'localhost';
Query OK, 0 rows affected (0.02 sec)










=====================================================================================================









Microsoft Windows [Version 10.0.26100.4946]
(c) Microsoft Corporation. All rights reserved.

C:\Program Files\MySQL\MySQL Server 8.0\bin>cd ..

C:\Program Files\MySQL\MySQL Server 8.0>cd ..

C:\Program Files\MySQL>cd ..

C:\Program Files>cd ..

C:\>cd 'C:\Program Files\MySQL\MySQL Server 8.0\bin>'
Access is denied.

C:\>cd "C:\Program Files\MySQL\MySQL Server 8.0\bin>"

C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql -u ajay -h localhost -p
Enter password: *******
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 39
Server version: 8.0.43 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
| z                  |
+--------------------+
3 rows in set (0.02 sec)

mysql> use z;
Database changed
mysql> show grants;
+------------------------------------------------------+
| Grants for ajay@localhost                            |
+------------------------------------------------------+
| GRANT USAGE ON *.* TO `ajay`@`localhost`             |
| GRANT SELECT ON `z`.`employes` TO `ajay`@`localhost` |
+------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> select * from employes;
+----+--------+--------+------+---------+
| id | name   | salary | age  | depart  |
+----+--------+--------+------+---------+
|  1 | ajay   |  30000 |   27 | boss    |
|  2 | mohan  |  23000 |   25 | trainer |
|  3 | kumar  |  24000 |   28 | trainer |
|  4 | ravi   |  27000 |   22 | trainee |
|  5 | ganesh |  25000 |   23 | employe |
|  6 | teja   |  29000 |   23 | employe |
+----+--------+--------+------+---------+
6 rows in set (0.00 sec)

mysql> show grants;
+--------------------------------------------------------------+
| Grants for ajay@localhost                                    |
+--------------------------------------------------------------+
| GRANT USAGE ON *.* TO `ajay`@`localhost`                     |
| GRANT ALL PRIVILEGES ON `z`.`employes` TO `ajay`@`localhost` |
+--------------------------------------------------------------+
2 rows in set (0.00 sec)

mysql> desc employes;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| name   | varchar(40) | YES  |     | NULL    |       |
| salary | float       | YES  |     | NULL    |       |
| age    | int         | YES  |     | NULL    |       |
| depart | varchar(20) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
5 rows in set (0.02 sec)

mysql> insert into employes modify salary int;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'modify salary int' at line 1
mysql> alter table employes modify salary int;
Query OK, 6 rows affected (0.18 sec)
Records: 6  Duplicates: 0  Warnings: 0

mysql> desc employes;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| name   | varchar(40) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| age    | int         | YES  |     | NULL    |       |
| depart | varchar(20) | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
5 rows in set (0.00 sec)

mysql> select * from employes;
ERROR 1142 (42000): SELECT command denied to user 'ajay'@'localhost' for table 'employes'
mysql> show grants;
+---------------------------------------------------------------------------------------------------------------------------------------+
| Grants for ajay@localhost                                                                                                             |
+---------------------------------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `ajay`@`localhost`                                                                                              |
| GRANT UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, CREATE VIEW, SHOW VIEW, TRIGGER ON `z`.`employes` TO `ajay`@`localhost` |
+---------------------------------------------------------------------------------------------------------------------------------------+
2 rows in set (0.00 sec)
