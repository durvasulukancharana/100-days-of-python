create database emp;

use emp;

CREATE TABLE dept (
    deptno INT PRIMARY KEY,
    dname VARCHAR(20),
    loc VARCHAR(20)
);

INSERT INTO dept (deptno, dname, loc) VALUES
(10, 'ACCOUNTING', 'NEW YORK'),
(20, 'RESEARCH', 'DALLAS'),
(30, 'SALES', 'CHICAGO'),
(40, 'OPERATIONS', 'BOSTON');

select * from dept;

CREATE TABLE emp (
    empno INT PRIMARY KEY,
    ename VARCHAR(20),
    job VARCHAR(20),
    mgr INT,
    hiredate DATE,
    sal DECIMAL(10,2),
    comm DECIMAL(10,2),
    deptno INT,
    FOREIGN KEY (deptno) REFERENCES dept(deptno)
);

INSERT INTO emp VALUES (7369, 'SMITH', 'CLERK', 7902, '1980-12-17', 800, NULL, 20);
INSERT INTO emp VALUES (7499, 'ALLEN', 'SALESMAN', 7698, '1981-02-20', 1600, 300, 30);
INSERT INTO emp VALUES (7521, 'WARD', 'SALESMAN', 7698, '1981-02-22', 1250, 500, 30);
INSERT INTO emp VALUES (7566, 'JONES', 'MANAGER', 7839, '1981-04-02', 2975, NULL, 20);
INSERT INTO emp VALUES (7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30);
INSERT INTO emp VALUES (7698, 'BLAKE', 'MANAGER', 7839, '1981-05-01', 2850, NULL, 30);
INSERT INTO emp VALUES (7782, 'CLARK', 'MANAGER', 7839, '1981-06-09', 2450, NULL, 10);
INSERT INTO emp VALUES (7788, 'SCOTT', 'ANALYST', 7566, '1982-12-09', 3000, NULL, 20);
INSERT INTO emp VALUES (7839, 'KING', 'PRESIDENT', NULL, '1981-11-17', 5000, NULL, 10);
INSERT INTO emp VALUES (7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500, 0, 30);
INSERT INTO emp VALUES (7876, 'ADAMS', 'CLERK', 7788, '1983-01-12', 1100, NULL, 20);
INSERT INTO emp VALUES (7900, 'JAMES', 'CLERK', 7698, '1981-12-03', 950, NULL, 30);
INSERT INTO emp VALUES (7902, 'FORD', 'ANALYST', 7566, '1981-12-03', 3000, NULL, 20);
INSERT INTO emp VALUES (7934, 'MILLER', 'CLERK', 7782, '1982-01-23', 1300, NULL, 10);

select * from emp;

-- 1.CREATE TABLE OF EMPLOYEE COLUMNS_NAME ARE EMPNO,ENAME ,SALARY, JOB,HIREDATE ,COMM AND INSERT VALUE
create table employe(empno int,emp_name varchar(30),salary int);
desc employe;
alter table employe add primary key(empno);
insert into employe values(2,'ajay',27000);
select * from employe;
create table details(empno int,job varchar(20),hiredate date);
alter table details add foreign key(empno) references employe(empno);
insert into details values(1,'developer','2025-12-09');
select * from employe inner join details on employe.empno=details.empno;


-- 2. WAQTD EMPLOYEE DETAILS WHOSE NAME STARTS WITH 'K' AND ENDS WITH 'S'.
select * from emp where ename like 'k%' and '%s';


-- 3. WAQTD EMPLOYEE NUMBER AND NAME WHO'S EARNING COMMISSION.
select empno , ename from emp where comm>0;


-- 4.DISPLAY THE LIST OF EMPLOYEES WHO HAVE JOINED A COMPANY BEFORE 1980 OR AFTER 1988.
select * from emp where year(hiredate) <= 1980 and year(hiredate)>=1988;


-- 5.WAQTD DETAILS OF EMPLOYEES WHO ARE HIRED FEB.
select * from emp where month(hiredate)=2;


-- 6.FIND 3RD MINIMUM SALARY IN THE EMPLOYEE TABLE.
select * from emp where sal = (select max(sal) from emp where sal < (select max(sal)from emp where sal < (select max(sal) from emp)));

select * from emp order by (sal) desc limit 1 offset 3;


-- 7.GET ALL EMPLOYEES WHO EARN MORE THAN THE AVERAGE SALARY .
select * from emp where sal > (select avg(sal) from emp);

select * from dept;

-- 8. DISPLAY THE DEPARTMENT INFORMATION OF EMPLOYEE WHO IS WORKING FOR NEW YORK LOCATION
select * from emp where deptno = (select deptno from dept where loc = 'new york');



CREATE TABLE student (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    class VARCHAR(10)
);
INSERT INTO student (student_id, name, class) VALUES
(1, 'Alice', '10A'),
(2, 'Bob', '10B'),
(3, 'Charlie', '10A');
CREATE TABLE marks (
    mark_id INT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    score INT,
    FOREIGN KEY (student_id) REFERENCES student(student_id)
);
INSERT INTO marks (mark_id, student_id, subject, score) VALUES
(1, 1, 'Math', 85),
(2, 2, 'Science', 90),
(3, 1, 'English', 78),
(4, 3, 'Math', 88);

select * from student;

select * from marks;


-- 9.GET EACH STUDENTS NAME ,CLASS ,SUBJECT ,AND SCORE.
select * from student inner join marks on student.student_id=marks.student_id;


-- 10.SHOW NAMES OF STUDENTS WHO SCORED MORE THAN 80
select * from student where student_id in (select student_id from marks where score>80);


select * from dept;
select * from emp;

-- waqtd name,deptno,dname where working as 'manager'
select ename,emp.deptno,dname from emp,dept where emp.deptno=dept.deptno and job='manager';
select ename,emp.deptno,dname from emp inner join dept on emp.deptno=dept.deptno and job='manager';


select ename,job,hiredate,dname,loc from emp,dept where emp.deptno=dept.deptno and loc='new york';
select ename,job,hiredate,dname,loc from emp inner join dept on emp.deptno=dept.deptno and loc='new york';


select ename,job,loc,sal from emp,dept where emp.deptno=dept.deptno and sal >(select sal from emp where ename='allen');
select ename,job,loc,sal from emp inner join dept on emp.deptno=dept.deptno where sal > (select sal from emp where ename='allen');


select e.ename employe,m.ename manager from emp e,emp m where e.mgr=m.empno;
select e.ename employe,m.ename manager from emp e,emp m where e.empno=m.mgr;

select e.ename employename,e.sal employesalary,m.ename managername,m.sal managersalary from emp e,emp m where e.mgr=m.empno and e.sal>m.sal;



select * from emp;
-- 1. List each employee along with their manager’s name.
select e.ename employename, m.ename mnagername from emp e,emp m where e.mgr=m.empno;

-- 2. Find employees who are managers (i.e., other employees report to them).
select distinct m.empno, e.ename managers from emp e,emp m where e.mgr=m.empno;
select ename,job from emp where job='manager';


-- 3. Display employees and their manager’s job title.
select e.ename employename,e.job employejob,m.ename managername,m.job managerjob 
from emp e,emp m where e.mgr=m.empno;


-- 4. Find employees who work in the same department as their manager.
select e.ename empname,m.ename manname from emp e,emp m where e.mgr=m.empno and e.deptno=m.deptno;


select * from emp;
-- 5. Find employees earning more than their manager.
select e.ename empname,m.ename manname from emp e,emp m where e.mgr=m.empno and e.sal>m.sal;




select * from dept;
select * from emp;

-- 1. Get all employees with their department name and location.
select * from emp where deptno in (select deptno from dept);


-- 7. Count employees in each department.
select count(job),job from emp group by job;


-- 9. List employees who have commission (comm) more than their salary.
select * from emp where comm>sal;

-- 8. Find employees without a manager.
select * from emp where mgr is null;


-- 6. Find employees who earn more than the average salary of their department.
select * from emp where sal> (select avg(sal) from emp);


-- 5. Find highest paid employee in each department.
select * from emp where (sal,job) in (select max(sal),job from emp group by job);

select ename,sal from emp inner join dept on emp.deptno=dept.deptno where sal = (select max(sal) from emp where dept.deptno=emp.deptno);

-- 2. Find employees who are managers.
select e.ename empname,m.ename manname from emp e,emp m where e.mgr=m.empno;


-- 4. Find employees hired in 1981.
select * from emp where year(hiredate)=1981;

select name,salary,job_title from employees where (salary,job_title) in (select min(salary),job_title from employees group by job_title);
select * from emp where (sal,job) in (select max(sal),job from emp group by job);
select * from emp where (sal,job) in (select max(sal),job from emp group by job);



select * from emp;
select * from dept;

-- Display all employees working in the SALES department.
select * from emp where deptno = (select deptno from dept where dname='sales');

-- List the names and salaries of employees who earn more than 2000.
select ename, sal from emp where sal > 2000;

-- Show the names of employees whose job is CLERK
select ename from emp where job='clerk';

-- Find the employees who joined in the year 1981.
select ename from emp where year(hiredate)='1981';
select ename from emp where month(hiredate)='11';

-- Show the names of employees with their department name and location.
select ename,dname,loc from emp join dept on emp.deptno=dept.deptno;
select ename,(select dname from dept where dept.deptno=emp.deptno) dname,(select loc from dept where emp.deptno=dept.deptno) loc from emp;









-- self join

-- ename , esal , mname , msal , mmname , mmsal
select e.ename empname,e.sal empsal,m.ename manname,m.sal mansal,s.ename sname ,s.sal ssalary from emp e,emp m, emp s where e.mgr=m.empno and m.mgr=s.empno;

select * from emp;
-- emp name, hiredate ,man name and hiredate, who hired before manager join
select e.ename employename,e.hiredate employehireate ,m.ename managername,m.hiredate managerhiredate ,h.ename highname,h.hiredate highhiredate
from emp e,emp m ,emp h where e.mgr=m.empno and e.hiredate<m.hiredate;

select e.ename employename,e.hiredate employehireate ,m.ename managername,m.hiredate managerhiredate
from emp e,emp m where e.mgr=m.empno and e.hiredate<m.hiredate;



-- empname,depname,locemp,who work in newyork
-- ename,dname,dept no, sal who sal repeated

select ename,dname,sal,emp.deptno,loc from emp,dept where emp.deptno=dept.deptno and sal in (select sal from emp group by sal having count(sal)>1);


