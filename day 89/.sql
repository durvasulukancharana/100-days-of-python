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


-- Q1. Find employees who earn more than the average salary of the company.
select ename from emp where sal > (select avg(sal) from emp);


-- Q2. Display employees who earn the same salary as FORD.
select ename from emp where sal = (select sal from emp where ename='ford');


-- Q3. List employees who have the earliest hire date in the company.
select ename , hiredate from emp where hiredate = (select min(hiredate) from emp);


-- Q4. Find the employee(s) who earn the second lowest salary.
select ename,sal from emp where sal = (select min(sal) from emp where sal > (select min(sal) from emp));


-- Q5. List employees whose salary is higher than ALL employees in department 10.
select ename,sal from emp where sal = (select max(sal) from emp where deptno=10);


-- Q1. Display employee name, job, department name, and location, sorted by department.
select ename , job , dname , loc from emp right join dept using(deptno) order by dname;


-- Q2. List employees who work in the same department as BLAKE.
select ename from emp join dept using(deptno) where dname = (select dname from emp join dept using(deptno) where ename='blake');
select ename from emp where deptno = (select deptno from emp where ename = 'blake') ;


-- Q3. Show department name and average salary of employees in each department.
select dname,avg(sal) from emp join dept using(deptno) group by dname;


-- Q4. Display employees who don’t have a manager.
select ename,job from emp where mgr is null;


-- Q5. Show employee name, manager name, and department name together.
select e.ename emp , m.ename man , d.dname from emp e join emp m on e.mgr=m.empno join dept d on m.deptno=d.deptno;
select e.ename emp,m.ename man,d.dname from emp e join emp m on e.mgr=m.empno join dept d on e.deptno=d.deptno;


-- Q1. Find employees earning more than the average salary of the SALES department.
select ename from emp where sal > (select avg(sal) from emp join dept using(deptno) where dname='sales' );


-- Q2. List employees who joined after SCOTT.
select ename from emp where hiredate > (select hiredate from emp where ename='scott');


-- Q3. Find the second highest salary in the company. 
select ename,sal from emp where sal = (select max(sal) from emp where sal < (select max(sal) from emp));


-- Q4. Display employees who have the same job as ALLEN.
select ename from emp where job = (select job from emp where ename='allen') ;


-- Q5. List employees who earn more than the average salary of their own department.
select ename from emp e where sal > (select avg(sal) from emp where e.deptno=deptno);


-- Q1. Display employee name, salary, department name, and location.
select ename,sal,dname,loc from emp join dept using(deptno);


-- Q2. List employees working in NEW YORK.
select e.ename,d.dname,loc from emp e join dept d using(deptno) where d.loc = 'new york';
select ename,dname,loc from emp join dept using(deptno) where loc = 'new york';


-- Q3. Show employees and their managers’ names.
select e.ename emp,m.ename manger from emp e,emp m where e.mgr=m.empno;


-- Q4. Display department name and total salary of employees in each department.
select sum(sal) , dname from emp join dept using(deptno) group by dname;


-- Q5. Show all departments and number of employees working in each department (include departments with zero employees).
select count(ename),dname from emp right join dept using(deptno) group by dname;
