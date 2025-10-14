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

