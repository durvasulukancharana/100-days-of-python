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



-- Q1. Display employee name, job, manager name, and manager’s department.
select e.ename emp_name,e.job emp_job , m.ename manager , m.deptno manager_dept , d.dname from emp e join emp m on e.mgr=m.empno join dept d on m.deptno=d.deptno;
select e.ename emp , m.ename man , d.dname from emp e join emp m on e.mgr=m.empno join dept d on m.deptno=d.deptno;


-- Q2. Show department name, employee count, and average salary, only for departments with more than 2 employees.
select dname , count(empno) , avg(sal) from emp join dept using(deptno) group by dname having count(empno)> 2;


-- Q3. List employees along with their department location, and display ‘High Salary’ if salary > 3000 else ‘Normal’.
select ename,dname,sal, case when sal >= 3000 then 'high salary' else 'low salary' end salary_status from emp join dept using(deptno);


-- Q4. Show departments and number of employees for each job role in that department.
select dname , job , count(job) from emp join dept using(deptno) group by dname,job;


-- Q5. List employees who don’t have a manager, along with their department name.
select ename from emp where mgr is null;


-- Q1. Find employees earning more than the average salary of their department (correlated subquery).
select ename,deptno,sal from emp e where sal > (select avg(sal) from emp where e.deptno=deptno);


-- Q2. List employees who earn the maximum salary in their department.
select ename,sal,dname from emp join dept using(deptno) where (sal,deptno) in (select max(sal),deptno from emp group by deptno );
select * from emp where (sal,job) in (select max(sal),job from emp group by job);


-- Q3. Find employees who earn less than the average salary of department 30.
select ename , sal , deptno from emp where deptno=30 and sal < (select avg(sal) from emp where deptno=30);
select ename , sal , deptno from emp where sal < (select avg(sal) from emp where deptno=30);


-- Q4. Display employees who earn more than ALL CLERKs.
select ename , sal from emp where sal > all(select sal from emp where job='clerk');



-- Find employees who earn more than the average salary of their department.
select ename,deptno,sal from emp e where sal > (select avg(sal) from emp where e.deptno=deptno);


-- Q1. Show employee name, department name, and location for all employees earning more than 2500.
select ename , dname , loc from emp join dept using(deptno) where sal > 2500 ;


-- Q2. List employees who work in departments where location is CHICAGO.
select ename , deptno, dname from emp join dept using(deptno) where dname = (select dname from dept where loc='chicago');


-- Q3. Display each department name along with the number of different job roles in that department.
SELECT dname,count(DISTINCT job)
FROM emp
JOIN dept ON emp.deptno = dept.deptno
GROUP BY dname;


-- Q4. Show employee name, manager name, and department name, only for employees who are MANAGERS.
select e.ename manager, m.ename boss from emp e join emp m on e.mgr=m.empno join dept d on e.deptno=d.deptno where e.job='manager';

SELECT e.ename AS Manager, m.ename AS Boss, d.dname
FROM emp e
LEFT JOIN emp m ON e.mgr = m.empno
JOIN dept d ON e.deptno = d.deptno
WHERE e.job = 'MANAGER';


-- Q5. Display the departments that currently have no employees.
select dname,deptno from dept where dept.deptno not in (select emp.deptno from emp); 
select dname,ename from emp right join dept using(deptno); 


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