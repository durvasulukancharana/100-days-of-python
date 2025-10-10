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

select * from emp;
select * from dept;

-- Write a query to display the employee name, job title, and department name for all employees.
select ename,job,dname from emp,dept where emp.deptno=dept.deptno;

-- Write a query to find the employees who work in the 'SALES' department along with their salaries and department location.
select ename,sal,loc from emp,dept where emp.deptno=dept.deptno and dname='sales';

-- Write a query to list the employee names and department names where the employee's salary is greater than 2000.
select ename,dname,sal from emp,dept where emp.deptno=dept.deptno and sal>2000;

-- Write a query to show all employees along with the name of their department, sorted by department name in alphabetical order.
select ename,dname from emp,dept where emp.deptno=dept.deptno order by dname;

-- Write a query to calculate the total salary paid to employees in each department.
select dname,sum(sal) from emp,dept where emp.deptno=dept.deptno group by dname;

-- Write a query to find the employees who were hired in the year 1981 and display their name, job, hire date, and department name.
select ename,hiredate,job,dname from emp,dept where emp.deptno=dept.deptno and year(hiredate)='1981';

-- Write a query to display employee names and department locations where the employee’s commission is not NULL.
select ename,dname,sal from emp,dept where emp.deptno=dept.deptno and comm>=0;
select * from emp;
-- Write a query to list the employees whose manager’s name is 'KING'.
select e.ename empname,m.ename manname from emp e,emp m where e.mgr=m.empno and e.mgr=(select m.empno from emp m where ename='king');
select * from emp where mgr=(select empno from emp where ename='king');

-- Write a query to display the employees’ names, department names, and salaries where the department location is ‘DALLAS’.
select ename,dname,sal,loc from emp,dept where emp.deptno=dept.deptno and loc='dallas';

-- Write a query to count the number of employees in each department and display the department name along with the count.
select count(ename),dname from emp,dept where emp.deptno=dept.deptno group by dname;
select count(ename) from emp;

-- Write a query to find the average salary per department and show only those departments where the average salary is more than 2500.
select avg(sal),dname from emp,dept where emp.deptno=dept.deptno group by dname;

SELECT d.dname,
       d.loc,
       (SELECT AVG(e.sal)
          FROM emp e
         WHERE e.deptno = d.deptno) AS avg_salary
FROM dept d
WHERE (SELECT AVG(e.sal)
         FROM emp e
        WHERE e.deptno = d.deptno) > 2500;


-- Write a query to list employees who work in departments located in either ‘NEW YORK’ or ‘CHICAGO’.
select ename,dname from emp,dept where emp.deptno=dept.deptno and (loc='new york' or loc= 'chicago');
select * from dept;
select * from emp;

-- Write a query to display the department name and the highest salary within each department.
select ename , sal , dname from emp,dept where emp.deptno=dept.deptno and sal in (select max(sal) from emp);
select ename,sal from emp where (sal,job) in (select max(sal),job from emp group by job);
select * from emp where (sal,job) in (select max(sal),job from emp group by job);

-- Write a query to find employees who earn more than their department’s average salary.
select ename,dname from emp,dept where emp.deptno=dept.deptno and (sal,dname) > (select avg(sal),dname from dept group by dname);
select ename,dname from emp,dept where emp.deptno=dept.deptno and (sal,job) > (select avg(sal),job from emp group by job);

-- Write a query to display the employee name, job, department name, and location for all employees whose department number is either 10, 20, or 30.
select ename,job,dname,loc from emp,dept where emp.deptno=dept.deptno and (emp.deptno=10 or emp.deptno=20 or emp.deptno=30);



