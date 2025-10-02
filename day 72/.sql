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

-- sql imp :

-- '''to add foreign key:'''
create table info(id int,age int,gender varchar(20),foreign key (id) references employes(id));


-- Find employees who earn more than the average salary of their department.
select ename,deptno,sal from emp e where sal > (select avg(sal) from emp where e.deptno=deptno);


-- 5. Find highest paid employee in each department.
select * from emp where (sal,job) in (select max(sal),job from emp group by job);


-- Q4. Display department names and number of SALESMAN in each department.
 select dname , count(empno) from emp join dept using(deptno) where job='salesman' group by dname;


-- Show the names of employees with their department name and location.
select ename,dname,loc from emp join dept on emp.deptno=dept.deptno;
select ename,(select dname from dept where dept.deptno=emp.deptno) dname,(select loc from dept where emp.deptno=dept.deptno) loc from emp;


-- Q3. Display each department name along with the number of different job roles in that department.
SELECT dname,count(DISTINCT job)
FROM emp
JOIN dept ON emp.deptno = dept.deptno
GROUP BY dname;

 
-- '''''inner join'''''

-- Q5. Show employee name, manager name, and department name together.
select e.ename emp , m.ename man , d.dname from emp e join emp m on e.mgr=m.empno join dept d on m.deptno=d.deptno;


-- ename,dname,dept no, sal who sal repeated
select ename,dname,sal,emp.deptno,loc from emp,dept where emp.deptno=dept.deptno and sal in (select sal from emp group by sal having count(sal)>1);



-- 1. List each employee along with their manager’s name.
select e.ename employename, m.ename mnagername from emp e,emp m where e.mgr=m.empno;


-- 2. Find employees who are managers (i.e., other employees report to them).
select m.empno , e.ename managers from emp e,emp m where e.mgr=m.empno;
select ename,job from emp where job='manager';


-- Q4. Show employee name, manager name, and department name, only for employees who are MANAGERS.
select e.ename manager, m.ename boss from emp e join emp m on e.mgr=m.empno join dept d on e.deptno=d.deptno where e.job='manager';


-- 3. Display employees and their manager’s job title.
select e.ename employename,e.job employejob,m.ename managername,m.job managerjob 
from emp e,emp m where e.mgr=m.empno;


-- 4. Find employees who work in the same department as their manager.
select e.ename empname,m.ename manname from emp e,emp m where e.mgr=m.empno and e.deptno=m.deptno;


select * from emp;
-- 5. Find employees earning more than their manager.
select e.ename empname,m.ename manager from emp e,emp m where e.mgr=m.empno and e.sal>m.sal;


-- List employees along with their department names, but also include departments that have no employees.
select ename , dname from emp right join dept using(deptno);


-- List departments that have no employees.
select dname,loc from dept where deptno not in (select deptno from emp);  


-- Q5. List employees whose salary is greater than the salary of any SALESMAN.
select ename from emp where sal > any (select sal from emp where job='salesman');
select ename from emp where sal > all (select sal from emp where job='salesman');




