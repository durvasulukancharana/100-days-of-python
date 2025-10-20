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


-- 1️.Display all employee names and their salaries. 
select ename,sal from emp;


-- 2️.List employees who work in department 30.
select ename from emp where deptno=30;


-- 3.Show employee name, job, and hiredate, ordered by hiredate.
select ename,job , hiredate from emp order by hiredate;


-- 4.Find employees whose salary is greater than 2000.
select ename,sal from emp where sal>2000;


-- 5.Display unique job titles from the employee table.
select distinct job from emp;


-- 6.Show the total number of employees in each department.
select count(*),deptno from emp group by deptno;


-- 7.Display employee name and department name using a join.
select ename , dname from emp join dept using(deptno);


-- 8.Find employees whose commission (comm) is NULL.
select ename,comm from emp where comm is null;


-- 9.List all employees who work in DALLAS.
select ename,loc from emp join dept using(deptno) where loc='dallas';


-- 10.Display all departments in ascending order of department name.
select dname from dept order by dname;


-- 1.Find the average salary of each department.
select avg(sal) , dname from emp join dept using(deptno) group by dname;


-- 2.List employees earning more than the average salary of all employees.
select ename,sal from emp where sal > (select avg(sal) from emp);


-- 3.Show department name and the number of SALESMAN in each department.
select ename,count('empno'),dname from emp join dept using(deptno) where job='manager' group by dname;
select * from emp;
select * from dept;

SELECT d.dname, COUNT(e.empno) AS salesman_count
FROM emp e
JOIN dept d ON e.deptno = d.deptno
WHERE e.job = 'SALESMAN'
GROUP BY d.dname;


-- 4️.Display employees who joined after SCOTT.
select ename , hiredate from emp where hiredate > (select hiredate from emp where ename='scott');


-- 5.Show each manager and the number of employees reporting to them.
select e.ename emp , m.ename manager from emp e join emp m where e.mgr=m.empno;


-- 6.Find employees whose salary is greater than their manager’s salary.
select e.ename emp, e.sal sal, m.ename manager, m.sal sal from emp e join emp m where e.mgr=m.empno and e.sal>m.sal;


-- 7.Display the second highest salary in the company.
(select max(sal) from emp where sal <(select max(sal) from emp));


-- 8.List employees who have the same job as ALLEN.
select ename , job from emp where job=(select job from emp where ename='allen') and ename <>'allen';


-- 9.Show department(s) that have the maximum number of employees.
select count(empno),deptno from emp group by deptno having count(empno)>5 ;
select count(*),deptno from emp group by deptno having count(*)=( select max(dept_count) from (select count(*) as dept_count from emp group by deptno)x);


-- 10.Find employees who earn the maximum salary in their department.
select ename,sal,deptno from emp where (sal,deptno) in (select max(sal),deptno from emp group by deptno) ;

