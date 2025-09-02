MySQL Shell 8.0.43

Copyright (c) 2016, 2025, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
 MySQL  JS > \sql
Switching to SQL mode... Commands end with ;
 MySQL  SQL > \c root@localhost
Creating a session to 'root@localhost'
Fetching global names for auto-completion... Press ^C to stop.
Your MySQL connection id is 20 (X protocol)
Server version: 8.0.43 MySQL Community Server - GPL
No default schema selected; type \use <schema> to set one.
 MySQL  localhost:33060+ ssl  SQL > create database telugu;
Query OK, 1 row affected (0.0227 sec)
 MySQL  localhost:33060+ ssl  SQL > use telugu;
Default schema set to telugu.
Fetching global names, object names from telugu for auto-completion... Press ^C to stop.
 MySQL  localhost:33060+ ssl  telugu  SQL > create table employe(id int,name varchar(30),salary int,role char(20));
Query OK, 0 rows affected (0.0544 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > desc employe;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | YES  |     | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| role   | char(20)    | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.0050 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe add id primary key;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primary key' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe add id int primary key;
ERROR: 1060: Duplicate column name 'id'
 MySQL  localhost:33060+ ssl  telugu  SQL > desc employe;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | YES  |     | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| role   | char(20)    | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.0028 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe add primary key(id);
Query OK, 0 rows affected (0.1448 sec)

Records: 0  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  telugu  SQL > desc employe;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| role   | char(20)    | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.0029 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe drop index(primary key);
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(primary key)' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe drop index();
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '()' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe drop index primary key;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'primary key' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe drop index id;
ERROR: 1091: Can't DROP 'id'; check that column/key exists
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe drop primary key;
Query OK, 0 rows affected (0.1173 sec)

Records: 0  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe modify id int not null;
Query OK, 0 rows affected (0.0228 sec)

Records: 0  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  telugu  SQL > desc employe;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   |     | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| role   | char(20)    | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.0029 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > alter table employe add unique(id);
Query OK, 0 rows affected (0.0908 sec)

Records: 0  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  telugu  SQL > desc employe;
+--------+-------------+------+-----+---------+-------+
| Field  | Type        | Null | Key | Default | Extra |
+--------+-------------+------+-----+---------+-------+
| id     | int         | NO   | PRI | NULL    |       |
| name   | varchar(30) | YES  |     | NULL    |       |
| salary | int         | YES  |     | NULL    |       |
| role   | char(20)    | YES  |     | NULL    |       |
+--------+-------------+------+-----+---------+-------+
4 rows in set (0.0028 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into employe values(1,'ajay',25000,'trainer'),(2,'vamsi',27000,'hr'),(3,'manoj',20000,'trainer'),(4,'sravan',20000,'trainer'),(5,'ganesh',15000,'trainee'),(6,'ravi',15000,'trainee'),(7,'dhruva',15000,'trainee'),(8,'tarun',20000,'sales');
Query OK, 8 rows affected (0.0094 sec)

Records: 8  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe;
+----+--------+--------+---------+
| id | name   | salary | role    |
+----+--------+--------+---------+
|  1 | ajay   |  25000 | trainer |
|  2 | vamsi  |  27000 | hr      |
|  3 | manoj  |  20000 | trainer |
|  4 | sravan |  20000 | trainer |
|  5 | ganesh |  15000 | trainee |
|  6 | ravi   |  15000 | trainee |
|  7 | dhruva |  15000 | trainee |
|  8 | tarun  |  20000 | sales   |
+----+--------+--------+---------+
8 rows in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > create table emp_detail(id int,place varchar(30),join_date date,foreign key id references employe(id));
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'references employe(id))' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > create table emp_detail(id int,place varchar(30),join_date date,foreign key (id) references employe(id));
Query OK, 0 rows affected (0.0763 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > desc emp_detail;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| id        | int         | YES  | MUL | NULL    |       |
| place     | varchar(30) | YES  |     | NULL    |       |
| join_date | date        | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
3 rows in set (0.0034 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(1,'hyd',now);
ERROR: 1054: Unknown column 'now' in 'field list'
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(1,'hyd','now');
ERROR: 1292: Incorrect date value: 'now' for column 'join_date' at row 1
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(1,'hyd',now());
Query OK, 1 row affected, 1 warning (0.0106 sec)
Note (code 1292): Incorrect date value: '2025-09-01 22:31:35' for column 'join_date' at row 1
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from emp_detail;
+----+-------+------------+
| id | place | join_date  |
+----+-------+------------+
|  1 | hyd   | 2025-09-01 |
+----+-------+------------+
1 row in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL >
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(2,'ongole',before now());
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'before now())' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(2,'ongole',after now());
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'now())' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(2,'ongole',2025-01-03);
ERROR: 1292: Incorrect date value: '2021' for column 'join_date' at row 1
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(2,'ongole','2025-01-03');
Query OK, 1 row affected (0.0109 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(3,'kadapa','2025-05-03');
Query OK, 1 row affected (0.0098 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(4,'vizag','2025-06-23');
Query OK, 1 row affected (0.0104 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(5,'bobbili','2025-06-12');
Query OK, 1 row affected (0.0085 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(6,'bobbili','2025-06-12');
Query OK, 1 row affected (0.0105 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(7,'palasa','2025-06-05');
Query OK, 1 row affected (0.0075 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > insert into emp_detail values(8,'s_kota',now());
Query OK, 1 row affected, 1 warning (0.0547 sec)
Note (code 1292): Incorrect date value: '2025-09-01 22:37:51' for column 'join_date' at row 1
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from emp_detail;
+----+---------+------------+
| id | place   | join_date  |
+----+---------+------------+
|  1 | hyd     | 2025-09-01 |
|  2 | ongole  | 2025-01-03 |
|  3 | kadapa  | 2025-05-03 |
|  4 | vizag   | 2025-06-23 |
|  5 | bobbili | 2025-06-12 |
|  6 | bobbili | 2025-06-12 |
|  7 | palasa  | 2025-06-05 |
|  8 | s_kota  | 2025-09-01 |
+----+---------+------------+
8 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > desc emp_detail;
+-----------+-------------+------+-----+---------+-------+
| Field     | Type        | Null | Key | Default | Extra |
+-----------+-------------+------+-----+---------+-------+
| id        | int         | YES  | MUL | NULL    |       |
| place     | varchar(30) | YES  |     | NULL    |       |
| join_date | date        | YES  |     | NULL    |       |
+-----------+-------------+------+-----+---------+-------+
3 rows in set (0.0032 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe innerjoin emp_detail on employe.id=emp_detail.id;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'emp_detail on employe.id=emp_detail.id' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe inner join emp_detail on employe.id=emp_detail.id;
+----+--------+--------+---------+----+---------+------------+
| id | name   | salary | role    | id | place   | join_date  |
+----+--------+--------+---------+----+---------+------------+
|  1 | ajay   |  25000 | trainer |  1 | hyd     | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  2 | ongole  | 2025-01-03 |
|  3 | manoj  |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  4 | sravan |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  5 | ganesh |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  8 | tarun  |  20000 | sales   |  8 | s_kota  | 2025-09-01 |
+----+--------+--------+---------+----+---------+------------+
8 rows in set (0.0030 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe left join emp_detail on employe.id=emp_detail.id;
+----+--------+--------+---------+----+---------+------------+
| id | name   | salary | role    | id | place   | join_date  |
+----+--------+--------+---------+----+---------+------------+
|  1 | ajay   |  25000 | trainer |  1 | hyd     | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  2 | ongole  | 2025-01-03 |
|  3 | manoj  |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  4 | sravan |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  5 | ganesh |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  8 | tarun  |  20000 | sales   |  8 | s_kota  | 2025-09-01 |
+----+--------+--------+---------+----+---------+------------+
8 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe right join emp_detail on employe.id=emp_detail.id;
+----+--------+--------+---------+----+---------+------------+
| id | name   | salary | role    | id | place   | join_date  |
+----+--------+--------+---------+----+---------+------------+
|  1 | ajay   |  25000 | trainer |  1 | hyd     | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  2 | ongole  | 2025-01-03 |
|  3 | manoj  |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  4 | sravan |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  5 | ganesh |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  8 | tarun  |  20000 | sales   |  8 | s_kota  | 2025-09-01 |
+----+--------+--------+---------+----+---------+------------+
8 rows in set (0.0019 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe cross join emp_detail;
+----+--------+--------+---------+----+---------+------------+
| id | name   | salary | role    | id | place   | join_date  |
+----+--------+--------+---------+----+---------+------------+
|  8 | tarun  |  20000 | sales   |  1 | hyd     | 2025-09-01 |
|  7 | dhruva |  15000 | trainee |  1 | hyd     | 2025-09-01 |
|  6 | ravi   |  15000 | trainee |  1 | hyd     | 2025-09-01 |
|  5 | ganesh |  15000 | trainee |  1 | hyd     | 2025-09-01 |
|  4 | sravan |  20000 | trainer |  1 | hyd     | 2025-09-01 |
|  3 | manoj  |  20000 | trainer |  1 | hyd     | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  1 | hyd     | 2025-09-01 |
|  1 | ajay   |  25000 | trainer |  1 | hyd     | 2025-09-01 |
|  8 | tarun  |  20000 | sales   |  2 | ongole  | 2025-01-03 |
|  7 | dhruva |  15000 | trainee |  2 | ongole  | 2025-01-03 |
|  6 | ravi   |  15000 | trainee |  2 | ongole  | 2025-01-03 |
|  5 | ganesh |  15000 | trainee |  2 | ongole  | 2025-01-03 |
|  4 | sravan |  20000 | trainer |  2 | ongole  | 2025-01-03 |
|  3 | manoj  |  20000 | trainer |  2 | ongole  | 2025-01-03 |
|  2 | vamsi  |  27000 | hr      |  2 | ongole  | 2025-01-03 |
|  1 | ajay   |  25000 | trainer |  2 | ongole  | 2025-01-03 |
|  8 | tarun  |  20000 | sales   |  3 | kadapa  | 2025-05-03 |
|  7 | dhruva |  15000 | trainee |  3 | kadapa  | 2025-05-03 |
|  6 | ravi   |  15000 | trainee |  3 | kadapa  | 2025-05-03 |
|  5 | ganesh |  15000 | trainee |  3 | kadapa  | 2025-05-03 |
|  4 | sravan |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  3 | manoj  |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  2 | vamsi  |  27000 | hr      |  3 | kadapa  | 2025-05-03 |
|  1 | ajay   |  25000 | trainer |  3 | kadapa  | 2025-05-03 |
|  8 | tarun  |  20000 | sales   |  4 | vizag   | 2025-06-23 |
|  7 | dhruva |  15000 | trainee |  4 | vizag   | 2025-06-23 |
|  6 | ravi   |  15000 | trainee |  4 | vizag   | 2025-06-23 |
|  5 | ganesh |  15000 | trainee |  4 | vizag   | 2025-06-23 |
|  4 | sravan |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  3 | manoj  |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  2 | vamsi  |  27000 | hr      |  4 | vizag   | 2025-06-23 |
|  1 | ajay   |  25000 | trainer |  4 | vizag   | 2025-06-23 |
|  8 | tarun  |  20000 | sales   |  5 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  5 | ganesh |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  4 | sravan |  20000 | trainer |  5 | bobbili | 2025-06-12 |
|  3 | manoj  |  20000 | trainer |  5 | bobbili | 2025-06-12 |
|  2 | vamsi  |  27000 | hr      |  5 | bobbili | 2025-06-12 |
|  1 | ajay   |  25000 | trainer |  5 | bobbili | 2025-06-12 |
|  8 | tarun  |  20000 | sales   |  6 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  5 | ganesh |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  4 | sravan |  20000 | trainer |  6 | bobbili | 2025-06-12 |
|  3 | manoj  |  20000 | trainer |  6 | bobbili | 2025-06-12 |
|  2 | vamsi  |  27000 | hr      |  6 | bobbili | 2025-06-12 |
|  1 | ajay   |  25000 | trainer |  6 | bobbili | 2025-06-12 |
|  8 | tarun  |  20000 | sales   |  7 | palasa  | 2025-06-05 |
|  7 | dhruva |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  6 | ravi   |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  5 | ganesh |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  4 | sravan |  20000 | trainer |  7 | palasa  | 2025-06-05 |
|  3 | manoj  |  20000 | trainer |  7 | palasa  | 2025-06-05 |
|  2 | vamsi  |  27000 | hr      |  7 | palasa  | 2025-06-05 |
|  1 | ajay   |  25000 | trainer |  7 | palasa  | 2025-06-05 |
|  8 | tarun  |  20000 | sales   |  8 | s_kota  | 2025-09-01 |
|  7 | dhruva |  15000 | trainee |  8 | s_kota  | 2025-09-01 |
|  6 | ravi   |  15000 | trainee |  8 | s_kota  | 2025-09-01 |
|  5 | ganesh |  15000 | trainee |  8 | s_kota  | 2025-09-01 |
|  4 | sravan |  20000 | trainer |  8 | s_kota  | 2025-09-01 |
|  3 | manoj  |  20000 | trainer |  8 | s_kota  | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  8 | s_kota  | 2025-09-01 |
|  1 | ajay   |  25000 | trainer |  8 | s_kota  | 2025-09-01 |
+----+--------+--------+---------+----+---------+------------+
64 rows in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe left join emp_detail on employe.id=emp_detail.id union select * from employe rightjoin emp_detail on employe.id=emp_detail.id;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'emp_detail on employe.id=emp_detail.id' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe left join emp_detail on employe.id=emp_detail.id union (select * from employe rightjoin emp_detail on employe.id=emp_detail.id);
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'emp_detail on employe.id=emp_detail.id)' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe left join emp_detail on employe.id=emp_detail.id union (select * from employe right join emp_detail on employe.id=emp_detail.id);
+----+--------+--------+---------+----+---------+------------+
| id | name   | salary | role    | id | place   | join_date  |
+----+--------+--------+---------+----+---------+------------+
|  1 | ajay   |  25000 | trainer |  1 | hyd     | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  2 | ongole  | 2025-01-03 |
|  3 | manoj  |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  4 | sravan |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  5 | ganesh |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  8 | tarun  |  20000 | sales   |  8 | s_kota  | 2025-09-01 |
+----+--------+--------+---------+----+---------+------------+
8 rows in set (0.0039 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select * from employe left join emp_detail on employe.id=emp_detail.id union select * from employe right join emp_detail on employe.id=emp_detail.id;
+----+--------+--------+---------+----+---------+------------+
| id | name   | salary | role    | id | place   | join_date  |
+----+--------+--------+---------+----+---------+------------+
|  1 | ajay   |  25000 | trainer |  1 | hyd     | 2025-09-01 |
|  2 | vamsi  |  27000 | hr      |  2 | ongole  | 2025-01-03 |
|  3 | manoj  |  20000 | trainer |  3 | kadapa  | 2025-05-03 |
|  4 | sravan |  20000 | trainer |  4 | vizag   | 2025-06-23 |
|  5 | ganesh |  15000 | trainee |  5 | bobbili | 2025-06-12 |
|  6 | ravi   |  15000 | trainee |  6 | bobbili | 2025-06-12 |
|  7 | dhruva |  15000 | trainee |  7 | palasa  | 2025-06-05 |
|  8 | tarun  |  20000 | sales   |  8 | s_kota  | 2025-09-01 |
+----+--------+--------+---------+----+---------+------------+
8 rows in set (0.0022 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select count(name) from employe;
+-------------+
| count(name) |
+-------------+
|           8 |
+-------------+
1 row in set (0.0041 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select sum(salary) from employe;
+-------------+
| sum(salary) |
+-------------+
|      157000 |
+-------------+
1 row in set (0.0445 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select max(salary) from employe;
+-------------+
| max(salary) |
+-------------+
|       27000 |
+-------------+
1 row in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select min(salary) from employe;
+-------------+
| min(salary) |
+-------------+
|       15000 |
+-------------+
1 row in set (0.0025 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select avg(salary) from employe;
+-------------+
| avg(salary) |
+-------------+
|  19625.0000 |
+-------------+
1 row in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary count(salary) from employe group by salary;
ERROR: 1064: You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'count(salary) from employe group by salary' at line 1
 MySQL  localhost:33060+ ssl  telugu  SQL > select count(salary) from employe group by salary;
+---------------+
| count(salary) |
+---------------+
|             1 |
|             1 |
|             3 |
|             3 |
+---------------+
4 rows in set (0.0027 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select count(salary),salary from employe group by salary;
+---------------+--------+
| count(salary) | salary |
+---------------+--------+
|             1 |  25000 |
|             1 |  27000 |
|             3 |  20000 |
|             3 |  15000 |
+---------------+--------+
4 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select count(salary),salary from employe group by salary having count(salary)>2;
+---------------+--------+
| count(salary) | salary |
+---------------+--------+
|             3 |  20000 |
|             3 |  15000 |
+---------------+--------+
2 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary>(select salary from employe where name='ajay');
+--------+
| salary |
+--------+
|  27000 |
+--------+
1 row in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary,name from employe where salary>(select salary from employe where name='ajay');
+--------+-------+
| salary | name  |
+--------+-------+
|  27000 | vamsi |
+--------+-------+
1 row in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary < (select salary from employe where name='vamsi') and salary > (select * from employe where name='tarun');
ERROR: 1241: Operand should contain 1 column(s)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary > (select salary from employe where name='tarun') and salary < (select * from employe where name='vamsi');
ERROR: 1241: Operand should contain 1 column(s)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary > (select salary from employe where name='tarun') and salary < (select salary from employe where name='vamsi');
+--------+
| salary |
+--------+
|  25000 |
+--------+
1 row in set (0.0019 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary > (select salary from employe where name='vamsi') and salary < (select salary from employe where name='tarun');
Empty set (0.0015 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary < (select salary from employe where name='vamsi') and salary < (select salary from employe where name='tarun');
+--------+
| salary |
+--------+
|  15000 |
|  15000 |
|  15000 |
+--------+
3 rows in set (0.0007 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select salary from employe where salary < (select salary from employe where name='vamsi') and salary > (select salary from employe where name='tarun');
+--------+
| salary |
+--------+
|  25000 |
+--------+
1 row in set (0.0013 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select max(salary) from employe;
+-------------+
| max(salary) |
+-------------+
|       27000 |
+-------------+
1 row in set (0.0020 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select max(salary),role from employe group by role;
+-------------+---------+
| max(salary) | role    |
+-------------+---------+
|       25000 | trainer |
|       27000 | hr      |
|       15000 | trainee |
|       20000 | sales   |
+-------------+---------+
4 rows in set (0.0029 sec)
 MySQL  localhost:33060+ ssl  telugu  SQL > select max(salary),role from employe group by role having max(salary);
+-------------+---------+
| max(salary) | role    |
+-------------+---------+
|       25000 | trainer |
|       27000 | hr      |
|       15000 | trainee |
|       20000 | sales   |
+-------------+---------+