Microsoft Windows [Version 10.0.26100.4946]
(c) Microsoft Corporation. All rights reserved.

C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql -u root -h localhost -p
Enter password: **************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 49
Server version: 8.0.43 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> use victus;
Database changed
mysql> show tables;
+------------------+
| Tables_in_victus |
+------------------+
| empid            |
| employ           |
| employees        |
+------------------+
3 rows in set (0.10 sec)

mysql> select * from empid;
+------+---------+
| id   | name    |
+------+---------+
|    1 | nithin  |
|    2 | charan  |
|    3 | pablo   |
|    4 | durva   |
|    5 | teja    |
|    6 | tarun   |
|    7 | varun   |
|    8 | ajay    |
|    9 | taja    |
|   10 | hemanth |
|   11 | sudheer |
+------+---------+
11 rows in set (0.00 sec)

mysql> select * from employ;
+---------+--------+----------------+
| name    | salary | dep            |
+---------+--------+----------------+
| charan  |  55000 | developer      |
| nithin  |  58000 | trainer        |
| tarun   |  60000 | bank employ    |
| pablo   |  66000 | python devop   |
| varun   |  71000 | java devop     |
| durva   |  92000 | developer      |
| teja    | 100000 | data Scientist |
| ajay    | 110000 | trainer        |
| taja    |  99999 | developer      |
| hemanth | 100000 | developer      |
| sudheer | 100000 | QA             |
+---------+--------+----------------+
11 rows in set (0.00 sec)

mysql> select employ.salary,empid.name from employ inner join empid on empid.name=employ.name;
+--------+---------+
| salary | name    |
+--------+---------+
|  58000 | nithin  |
|  55000 | charan  |
|  66000 | pablo   |
|  92000 | durva   |
| 100000 | teja    |
|  60000 | tarun   |
|  71000 | varun   |
| 110000 | ajay    |
|  99999 | taja    |
| 100000 | hemanth |
| 100000 | sudheer |
+--------+---------+
11 rows in set (0.00 sec)

mysql> select employ.salary,empid.name from employ inner join empid on empid.name=employ.name order by salary;
+--------+---------+
| salary | name    |
+--------+---------+
|  55000 | charan  |
|  58000 | nithin  |
|  60000 | tarun   |
|  66000 | pablo   |
|  71000 | varun   |
|  92000 | durva   |
|  99999 | taja    |
| 100000 | teja    |
| 100000 | hemanth |
| 100000 | sudheer |
| 110000 | ajay    |
+--------+---------+
11 rows in set (0.02 sec)

mysql> select id.empid,name.empid,salary.employ from employ inner join empid on empid.name=employ.name;
ERROR 1054 (42S22): Unknown column 'id.empid' in 'field list'
mysql> select id.empid from empid;
ERROR 1054 (42S22): Unknown column 'id.empid' in 'field list'
mysql> select id from empid;
+------+
| id   |
+------+
|    1 |
|    2 |
|    3 |
|    4 |
|    5 |
|    6 |
|    7 |
|    8 |
|    9 |
|   10 |
|   11 |
+------+
11 rows in set (0.00 sec)

mysql> select id.empid,name.employ from employ inner join empid on empid.name=employ.name;
ERROR 1054 (42S22): Unknown column 'id.empid' in 'field list'
mysql> select empid.id,employ.name from employ inner join empid on empid.name=employ.name;
+------+---------+
| id   | name    |
+------+---------+
|    1 | nithin  |
|    2 | charan  |
|    3 | pablo   |
|    4 | durva   |
|    5 | teja    |
|    6 | tarun   |
|    7 | varun   |
|    8 | ajay    |
|    9 | taja    |
|   10 | hemanth |
|   11 | sudheer |
+------+---------+
11 rows in set (0.00 sec)

mysql> select empid.id,employ.name,employ.salary from employ inner join empid on empid.name=employ.name;
+------+---------+--------+
| id   | name    | salary |
+------+---------+--------+
|    1 | nithin  |  58000 |
|    2 | charan  |  55000 |
|    3 | pablo   |  66000 |
|    4 | durva   |  92000 |
|    5 | teja    | 100000 |
|    6 | tarun   |  60000 |
|    7 | varun   |  71000 |
|    8 | ajay    | 110000 |
|    9 | taja    |  99999 |
|   10 | hemanth | 100000 |
|   11 | sudheer | 100000 |
+------+---------+--------+
11 rows in set (0.00 sec)

mysql> select empid.id,employ.name,employ.salary from employ inner join empid on empid.name=employ.name order by salary;
+------+---------+--------+
| id   | name    | salary |
+------+---------+--------+
|    2 | charan  |  55000 |
|    1 | nithin  |  58000 |
|    6 | tarun   |  60000 |
|    3 | pablo   |  66000 |
|    7 | varun   |  71000 |
|    4 | durva   |  92000 |
|    9 | taja    |  99999 |
|    5 | teja    | 100000 |
|   10 | hemanth | 100000 |
|   11 | sudheer | 100000 |
|    8 | ajay    | 110000 |
+------+---------+--------+
11 rows in set (0.00 sec)

mysql> select empid.name,employ.salary from employ left join empid on employ.name=empid.name;
+---------+--------+
| name    | salary |
+---------+--------+
| charan  |  55000 |
| nithin  |  58000 |
| tarun   |  60000 |
| pablo   |  66000 |
| varun   |  71000 |
| durva   |  92000 |
| teja    | 100000 |
| ajay    | 110000 |
| taja    |  99999 |
| hemanth | 100000 |
| sudheer | 100000 |
+---------+--------+
11 rows in set (0.00 sec)

mysql> select empid.name,employ.salary from employ right join empid on employ.name=empid.name;
+---------+--------+
| name    | salary |
+---------+--------+
| nithin  |  58000 |
| charan  |  55000 |
| pablo   |  66000 |
| durva   |  92000 |
| teja    | 100000 |
| tarun   |  60000 |
| varun   |  71000 |
| ajay    | 110000 |
| taja    |  99999 |
| hemanth | 100000 |
| sudheer | 100000 |
+---------+--------+
11 rows in set (0.00 sec)

mysql> select * from employ left join empid on employ.name=empid.name;
+---------+--------+----------------+------+---------+
| name    | salary | dep            | id   | name    |
+---------+--------+----------------+------+---------+
| charan  |  55000 | developer      |    2 | charan  |
| nithin  |  58000 | trainer        |    1 | nithin  |
| tarun   |  60000 | bank employ    |    6 | tarun   |
| pablo   |  66000 | python devop   |    3 | pablo   |
| varun   |  71000 | java devop     |    7 | varun   |
| durva   |  92000 | developer      |    4 | durva   |
| teja    | 100000 | data Scientist |    5 | teja    |
| ajay    | 110000 | trainer        |    8 | ajay    |
| taja    |  99999 | developer      |    9 | taja    |
| hemanth | 100000 | developer      |   10 | hemanth |
| sudheer | 100000 | QA             |   11 | sudheer |
+---------+--------+----------------+------+---------+
11 rows in set (0.00 sec)

mysql> select * from employ right join empid on employ.name=empid.name;
+---------+--------+----------------+------+---------+
| name    | salary | dep            | id   | name    |
+---------+--------+----------------+------+---------+
| nithin  |  58000 | trainer        |    1 | nithin  |
| charan  |  55000 | developer      |    2 | charan  |
| pablo   |  66000 | python devop   |    3 | pablo   |
| durva   |  92000 | developer      |    4 | durva   |
| teja    | 100000 | data Scientist |    5 | teja    |
| tarun   |  60000 | bank employ    |    6 | tarun   |
| varun   |  71000 | java devop     |    7 | varun   |
| ajay    | 110000 | trainer        |    8 | ajay    |
| taja    |  99999 | developer      |    9 | taja    |
| hemanth | 100000 | developer      |   10 | hemanth |
| sudheer | 100000 | QA             |   11 | sudheer |
+---------+--------+----------------+------+---------+
11 rows in set (0.00 sec)

mysql> show tables;
+------------------+
| Tables_in_victus |
+------------------+
| empid            |
| employ           |
| employees        |
+------------------+
3 rows in set (0.02 sec)

mysql> select * from employees;
+----------+-------+-----+--------+------------+
| emp_name | empId | age | salary | doj        |
+----------+-------+-----+--------+------------+
| frank    |     1 |  31 |  40000 | 2025-08-23 |
| pablo    |     2 |  22 |  60000 | 2025-08-30 |
| durva    |     3 |  21 |  61000 | 2025-08-31 |
+----------+-------+-----+--------+------------+
3 rows in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| class              |
| classtime          |
| employ_details     |
| information_schema |
| jobs               |
| mydatabase         |
| mysql              |
| performance_schema |
| sys                |
| teja               |
| victus             |
+--------------------+
11 rows in set (0.02 sec)

mysql> use teja;
Database changed
mysql> show tables;
Empty set (0.00 sec)

mysql> use class;
Database changed
mysql> show tables;
+-----------------+
| Tables_in_class |
+-----------------+
| airforce        |
| detail          |
| employ_det      |
+-----------------+
3 rows in set (0.00 sec)

mysql> select * from airforce;
+-----------+----------+--------+------------+------+
| pilotname | location | salary | doj        | City |
+-----------+----------+--------+------------+------+
| tejaaa    | annaram  |  35000 | 2004-07-31 | NULL |
| ravi      | bvv      |  38000 | 2009-07-25 | NULL |
+-----------+----------+--------+------------+------+
2 rows in set (0.03 sec)

mysql> select * from detail;
+------------+--------------+------------+--------------+------------+----------+--------+
| customerid | CustomerName | surname    | Address_city | postalCode | country  | salary |
+------------+--------------+------------+--------------+------------+----------+--------+
|    9391254 | Raviteja     | botsa      | nyc          |     124863 | usa      |   NULL |
|   21829516 | ganesh       | Gangadhara | bamini       |     535589 | india    |   NULL |
|   21829524 | Durvasulu    | kancharana | palasa       |     535580 | india    |   NULL |
|   21829530 | tarun        | lekkala    | vizianagaram |     535563 | canada   |   NULL |
|   21829532 | pablo        | MP         | IT colony    |     535579 | india    |   NULL |
|   21829544 | charan       | panchiredy | gmvalasa     |     532410 | srilanka |   NULL |
|   21829552 | sudheer      | sunkari    | madugula     |     534400 | uae      |   NULL |
+------------+--------------+------------+--------------+------------+----------+--------+