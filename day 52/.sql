create database my_employes; 

use employe;

create table employes_details(id int ,name varchar(50),salary int);

desc employes_details;

insert into employes_details values (1,'m.ganesh',23000),
(2,'teja',25000),
(3,'dushyanth',24000),
(4,'charan',22000),
(5,'tarun','20000'),
(6,'sudheer',27000),
(7,'yugandhar',30000),
(8,'v.prasanna',40000),
(9,'p.prasanna',35000),
(10,'g.ganesh',23000),
(11,'guna',18500),
(12,'hemanth',19000);

select * from employes_details;

alter table employes_details add gender varchar(20);

set sql_safe_updates=0;

update employes_details set gender=case 
when id=1 then 'male'
when id=2 then 'male'
when id=3 then 'male'
when id=4 then 'male'
when id=5 then 'male'
when id=6 then 'male'
when id=7 then 'male'
when id=8 then 'female'
when id=9 then 'female'
when id=10 then 'male'
when id=11 then 'male'
when id=12 then 'male' 
end 
where id in (1,2,3,4,5,6,7,8,9,10,11,12);

select * from employes_details;

insert into employes_details values(13,'jahnavi',33000,'female');

select * from employes_details;

alter table employes_details add role varchar(40);

update employes_details set role=case 
when id=1 then 'developer'
when id=2 then 'developer'
when id=3 then 'trainee'
when id=4 then 'trainee'
when id=5 then 'trainee'
when id=6 then 'trainer'
when id=7 then 'manager'
when id=8 then 'ceo'
when id=9 then 'hr'
when id=10 then 'trainer'
when id=11 then 'finance'
when id=12 then 'finance' 
when id=13 then 'tester'
end 
where id in (1,2,3,4,5,6,7,8,9,10,11,12,13);

select * from employes_details;

update employes_details set role='tester' where name='tarun';

select * from employes_details;




										 -- operators --


select * from employes_details where role='ceo';


-- and 

select * from employes_details where salary>25000 and salary<40000;


-- or

select * from employes_details where salary<20000 or salary>30000;


-- not

select * from employes_details where not salary>20000 and salary<30000;


-- like

select * from employes_details where name like '%a';

select * from employes_details where name like '%a%';


-- in

select * from employes_details where id in (1,2,3,4,5);

select * from employes_details where name in ('teja','p.prasanna');

select * from employes_details order by salary desc;

select * from employes_details order by salary;

select * from employes_details limit 2;

select * from employes_details limit 2 offset 3;

select * from employes_details where id between 5 and 9;

select count(role),role from employes_details group by role;

select count(gender),gender from employes_details group by gender;




-- nested query:

select name, salary ,role ,case
 when salary <=23000 then 'low_salary'
 when salary between 24000 and 35000 then 'medium_salary'
 else 'high_salary'
 end as sal
 from employes_details;
 

select * from employes_details where salary = (select max(salary) from employes_details where salary <
 (select max(salary) from employes_details where salary < 
 (select max(salary) from employes_details)));


select * from employes_details where salary > (select avg(salary) from employes_details); 




-- rank and dense_rank

select name,salary, rank() over(order by salary desc) from employes_details;

select name,salary, dense_rank() over(order by salary desc) from employes_details;

select name,gender , rank() over(order by gender asc) from employes_details;

select name,gender , dense_rank() over (order by gender) from employes_details;

select name,gender , dense_rank() over (order by name) from employes_details;

select name,gender , dense_rank() over (order by name desc) from employes_details;

select name,id,salary, rank() over(partition by name order by salary desc) from employes_details;

select name,id,salary, rank() over(partition by name order by salary desc) ,
 dense_rank() over (partition by name order by salary desc) from employes_details;


-- views 
create view new_table as select name,salary from employes_details;

select * from new_table;

create or replace view new_table as select name,salary,role from employes_details;

select * from new_table;


-- index
create index new_index on employes_details(salary);

show index from employes_details;




-- triggers

select * from employes_details;

create table emp_login(id int ,action_name varchar(50),login_time datetime);

delimiter $$ 

create trigger hara_kumar_insert after insert on employes_details for each row begin insert into
emp_login(id,action_name,login_time) values(concat('new employe added:',new.id,new.name,new.salary),now());
end $$
delimiter ;

insert into employes_details(id,name,role) values(14,'harakumar','entreprenuer');
desc employes_details;


-- store procedure


delimiter $$
create procedure pablo()
begin 
select * from employes_details;
end $$
delimiter ;
call pablo();


delimiter $$
create procedure hello(in xy int)
begin
select * from employes_details where id=xy;
end $$
delimiter ;
call hello(3);
