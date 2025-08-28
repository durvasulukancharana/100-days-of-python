sMySQL Shell 8.0.43

Copyright (c) 2016, 2025, Oracle and/or its affiliates.
Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
Other names may be trademarks of their respective owners.

Type '\help' or '\?' for help; '\quit' to exit.
 MySQL  JS > \sql
Switching to SQL mode... Commands end with ;
 MySQL  SQL > \c root@localhost
Creating a session to 'root@localhost'
Fetching global names for auto-completion... Press ^C to stop.
Your MySQL connection id is 31 (X protocol)
Server version: 8.0.43 MySQL Community Server - GPL
No default schema selected; type \use <schema> to set one.
 MySQL  localhost:33060+ ssl  SQL > create database crex;
Query OK, 1 row affected (0.0318 sec)
 MySQL  localhost:33060+ ssl  SQL > use crex;
Default schema set to `crex`.
Fetching global names, object names from `crex` for auto-completion... Press ^C to stop.
 MySQL  localhost:33060+ ssl  crex  SQL > create table cricketers(jersy_no int,name varchar(50),year_of_captain date,status varchar(50),gender varchar(50));
Query OK, 0 rows affected (0.0667 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > desc cricketers;
+-----------------+-------------+------+-----+---------+-------+
| Field           | Type        | Null | Key | Default | Extra |
+-----------------+-------------+------+-----+---------+-------+
| jersy_no        | int         | YES  |     | NULL    |       |
| name            | varchar(50) | YES  |     | NULL    |       |
| year_of_captain | date        | YES  |     | NULL    |       |
| status          | varchar(50) | YES  |     | NULL    |       |
| gender          | varchar(50) | YES  |     | NULL    |       |
+-----------------+-------------+------+-----+---------+-------+
5 rows in set (0.0177 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > insert into cricketers values(07,'thala','2007-07-07','married','male');
Query OK, 1 row affected (0.0210 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > insert into cricketers values(18,'virat','2017-05-25','married','male'),(45,'rohit','2022-08-15','married','male'),(77,'gill','2025-05-23','unmarried','male');
Query OK, 3 rows affected (0.0427 sec)

Records: 3  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers;
+----------+-------+-----------------+-----------+--------+
| jersy_no | name  | year_of_captain | status    | gender |
+----------+-------+-----------------+-----------+--------+
|        7 | thala | 2007-07-07      | married   | male   |
|       18 | virat | 2017-05-25      | married   | male   |
|       45 | rohit | 2022-08-15      | married   | male   |
|       77 | gill  | 2025-05-23      | unmarried | male   |
+----------+-------+-----------------+-----------+--------+
4 rows in set (0.0015 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > create table info(jersy_no int,wife varchar(50),kids int);
Query OK, 0 rows affected (0.0280 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > desc info;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| jersy_no | int         | YES  |     | NULL    |       |
| wife     | varchar(50) | YES  |     | NULL    |       |
| kids     | int         | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
3 rows in set (0.0049 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > insert into info values(7,'shakshi',1),(18,'anushka sharma',2),(45,'ritika sajdeh',1),(77,'no',0);
Query OK, 4 rows affected (0.0054 sec)

Records: 4  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  crex  SQL > select * from info;
+----------+----------------+------+
| jersy_no | wife           | kids |
+----------+----------------+------+
|        7 | shakshi        |    1 |
|       18 | anushka sharma |    2 |
|       45 | ritika sajdeh  |    1 |
|       77 | no             |    0 |
+----------+----------------+------+
4 rows in set (0.0014 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers inner join info on cricketers.jersy_no=info.jersy;

ERROR: 1054: Unknown column 'info.jersy' in 'on clause'
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers inner join info on cricketers.jersy_no=info.jersy_no;
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
| jersy_no | name  | year_of_captain | status    | gender | jersy_no | wife           | kids |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
|        7 | thala | 2007-07-07      | married   | male   |        7 | shakshi        |    1 |
|       18 | virat | 2017-05-25      | married   | male   |       18 | anushka sharma |    2 |
|       45 | rohit | 2022-08-15      | married   | male   |       45 | ritika sajdeh  |    1 |
|       77 | gill  | 2025-05-23      | unmarried | male   |       77 | no             |    0 |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
4 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers left join info on cricketers.jersy_no=info.jersy_no;
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
| jersy_no | name  | year_of_captain | status    | gender | jersy_no | wife           | kids |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
|        7 | thala | 2007-07-07      | married   | male   |        7 | shakshi        |    1 |
|       18 | virat | 2017-05-25      | married   | male   |       18 | anushka sharma |    2 |
|       45 | rohit | 2022-08-15      | married   | male   |       45 | ritika sajdeh  |    1 |
|       77 | gill  | 2025-05-23      | unmarried | male   |       77 | no             |    0 |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
4 rows in set (0.0016 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > insert into info values(33,'natasha',1),(17,'urvasi',2);
Query OK, 2 rows affected (0.0146 sec)

Records: 2  Duplicates: 0  Warnings: 0
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers right join info on cricketers.jersy_no=info.jersy_no;
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
| jersy_no | name  | year_of_captain | status    | gender | jersy_no | wife           | kids |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
|        7 | thala | 2007-07-07      | married   | male   |        7 | shakshi        |    1 |
|       18 | virat | 2017-05-25      | married   | male   |       18 | anushka sharma |    2 |
|       45 | rohit | 2022-08-15      | married   | male   |       45 | ritika sajdeh  |    1 |
|       77 | gill  | 2025-05-23      | unmarried | male   |       77 | no             |    0 |
|     NULL | NULL  | NULL            | NULL      | NULL   |       33 | natasha        |    1 |
|     NULL | NULL  | NULL            | NULL      | NULL   |       17 | urvasi         |    2 |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
6 rows in set (0.0021 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers left join info on cricketers.jersy_no=info.jersy_no
                                       -> union select * from cricketers right join info on cricketers.jersy_no=info.jersy_no;
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
| jersy_no | name  | year_of_captain | status    | gender | jersy_no | wife           | kids |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
|        7 | thala | 2007-07-07      | married   | male   |        7 | shakshi        |    1 |
|       18 | virat | 2017-05-25      | married   | male   |       18 | anushka sharma |    2 |
|       45 | rohit | 2022-08-15      | married   | male   |       45 | ritika sajdeh  |    1 |
|       77 | gill  | 2025-05-23      | unmarried | male   |       77 | no             |    0 |
|     NULL | NULL  | NULL            | NULL      | NULL   |       33 | natasha        |    1 |
|     NULL | NULL  | NULL            | NULL      | NULL   |       17 | urvasi         |    2 |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
6 rows in set (0.0427 sec)
 MySQL  localhost:33060+ ssl  crex  SQL > select * from cricketers left join info on cricketers.jersy_no=info.jersy_no;
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
| jersy_no | name  | year_of_captain | status    | gender | jersy_no | wife           | kids |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
|        7 | thala | 2007-07-07      | married   | male   |        7 | shakshi        |    1 |
|       18 | virat | 2017-05-25      | married   | male   |       18 | anushka sharma |    2 |
|       45 | rohit | 2022-08-15      | married   | male   |       45 | ritika sajdeh  |    1 |
|       77 | gill  | 2025-05-23      | unmarried | male   |       77 | no             |    0 |
+----------+-------+-----------------+-----------+--------+----------+----------------+------+
4 rows in set (0.0016 sec)
