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


select * from emp;
select * from dept;
-- Display employee name, job, salary, and department name.
select ename,sal,job,dname from emp inner join dept on emp.deptno=dept.deptno;


-- List all employees along with their manager’s name.
select e.ename empname , m.ename mangername from emp e, emp m where e.mgr=m.empno;


-- Find the department name and location of employees working as ‘CLERK’.
select dname,loc from dept where deptno in (select deptno from emp where job='clerk');


-- Show employees who work in ‘CHICAGO’.
select ename from emp where deptno = (select deptno from dept where loc='chicago');


-- Find employees with their department name and manager’s name.
select e.ename emp,m.ename man,d.dname from emp e join emp m on e.mgr=m.empno join dept d on e.deptno=d.deptno;


-- Find employees who earn more than the average salary of all employees.
select ename from emp where sal > (select avg(sal) from emp);


-- Find employees whose salary is greater than the salary of ‘ALLEN’.
select ename from emp where sal > (select sal from emp where ename='allen');


-- List employees working in the same department as ‘SCOTT’.
select ename,dname from emp inner join dept on emp.deptno=dept.deptno where dname=(select dname from dept inner join emp on emp.deptno=dept.deptno where ename='scott');


-- Find the employee(s) with the maximum salary.
select ename from emp where sal = (select max(sal) from emp);
select ename from emp where (sal,job) in (select max(sal),job from emp group by job);


-- Find employees who earn more than the average salary of their department.
select ename,sal,deptno,job from emp e where sal > (select avg(sal) from emp where deptno=e.deptno);

select * from emp;
select * from dept;

-- List departments that have no employees.
select dname,loc from dept where deptno not in (select deptno from emp);  


-- Find employees who work in departments where the average salary is above 2000.
select ename,dname from emp inner join dept on emp.deptno=dept.deptno ;
select ename,dname from emp inner join dept on emp.deptno=dept.deptno where sal in
 (select avg(sal),dname from emp inner join dept on emp.deptno=dept.deptno group by dname having avg(sal)>2000);


-- List all employees with their department name and location.
select ename,dname from emp e join dept d on e.deptno=d.deptno;


-- Find employees along with their manager’s name.
select e.ename emp,m.ename manger from emp e join emp m on e.mgr=m.empno;


-- List employees working in 'DALLAS'.
select ename,loc from emp e join dept d on e.deptno=d.deptno where loc='dallas';
select ename from emp where deptno = (select deptno from dept where loc='dallas');

select * from emp;
-- Find all managers with their department details.
select ename,dname from emp e,dept d where e.deptno=d.deptno and job='manager';
select m.ename manger,d.dname from emp e join emp m on e.mgr=m.empno join dept d on m.deptno=d.deptno;
select e.ename emp,m.ename man,d.dname from emp e join emp m on e.mgr=m.empno join dept d on e.deptno=d.deptno;


-- List employees and their managers’ department names.
select e.ename emp,m.ename manager,d.dname department from emp e join emp m on e.mgr=m.empno join dept d on m.deptno=d.deptno;


-- Find employees who earn more than the average salary of their department.
select ename,deptno,sal from emp e where sal > (select avg(sal) from emp where e.deptno=deptno);


-- List employees who work in the same department as ‘SCOTT’.
select ename,dname from emp,dept where emp.deptno=dept.deptno and dname=(select dname from dept,emp where dept.deptno=emp.deptno and ename='scott');


-- Write a query to display employee name, job, department name, and location for all employees.
select ename,job,dname,loc from emp inner join dept using(deptno);


-- Write a query to list employees working in the SALES department.
select ename,dname from emp join dept using(deptno) where dname='sales';


-- Display employee name, department name, and salary for employees who earn more than 2000.
select ename,dname,sal from emp join dept using(deptno) where sal>2000;


-- Show the manager’s name along with each employee’s name (self-join).
select e.ename emp,m.ename manager from emp e join emp m where e.mgr=m.empno;


-- List employees along with their department names, but also include departments that have no employees.
select ename , dname from emp right join dept using(deptno);


-- Find employees who earn more than the average salary of all employees.
select ename from emp where sal > (select avg(sal) from emp);


-- Display the employees who earn more than the average salary of their department.
select e.ename from emp e where e.sal > (select avg(sal) from emp where e.deptno=deptno);
select ename,deptno,sal from emp e where sal > (select avg(sal) from emp where e.deptno=deptno);

