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


-- 1️.Find the N-th highest salary (e.g., 3rd highest). 
select ename,sal from emp where sal=(select max(sal) from emp where sal <(select max(sal)from emp where sal <(select max(sal) from emp)));


-- 2.Display employees who earn more than the average salary of their department.
select ename,sal,deptno from emp e where sal >(select avg(sal) from emp where e.deptno=deptno);


-- 3.List employees who earn the same salary as someone else in another department.
select ename,sal,deptno from emp where sal in (select sal from emp group by sal having count(sal)>1);
select ename,dname,sal,emp.deptno,loc from emp,dept where emp.deptno=dept.deptno and sal in (select ename,sal from emp group by sal having count(sal)>1);


-- 4️.Find employees who don’t have a manager. 
select e.ename from emp e where e.mgr is null;
select ename,job from emp where mgr is null;


-- 5.Display manager → employee relationship hierarchy.
select e.ename emp,m.ename manager from emp e join emp m where e.mgr=m.empno;


-- 6.Show department name, employee name, and department total salary.
select dname,ename,(select sum(sal),deptno from emp group by deptno) from emp join dept using(deptno);

select sum(sal),deptno,dname from emp join dept using(deptno) group by deptno;


-- 7.List employees whose salary is greater than ALL SALESMAN salaries.
select ename , sal from emp where sal > all(select sal from emp where job='salesman');


-- 8.Display employee name, salary, and a “Grade” column.
select ename,sal, case when sal >= 3000 then 'high salary' when sal between 1500 and 2999 then 'medium salry' else 'low salary' end as grade from emp;


-- 9.Find employees who earn more than the average salary of their manager’s department.
select e.ename emp,e.sal sal from emp where sal > (select avg(sal) from e.mgr);

select e.ename emp,m.ename manager from emp e join emp m where e.mgr=m.empno and e.sal > avg(m.sal);

SELECT e.ename, e.sal
FROM emp e
WHERE e.sal > (
    SELECT AVG(sal)
    FROM emp
    WHERE deptno = (
        SELECT deptno FROM emp WHERE empno = e.mgr
    )
);


-- 10.Display departments along with cumulative total salary using a window function.
SELECT deptno, ename, sal,
       SUM(sal) OVER (PARTITION BY deptno ORDER BY sal) AS cumulative_salary
FROM emp;

-- 1. *List all employees.*  
select * from emp;
select * from dept;

-- 2. *Show names and salaries of employees who earn more than 2000.*
select ename,sal from emp where sal >= 2000;

-- 3. *Find all employees who work in department 30.*
select ename, deptno from emp where deptno=30;

-- 4. *Display employee names and their job titles who are managers.*
select ename , job from emp where job='manager';

-- 5. *List employees hired before 1981.*
select ename , hiredate from emp where year(hiredate) < 1981;

-- 6. *Show all departments located in 'DALLAS'.*
select dname from dept where loc='dallas';

-- 7. *Find the name and salary of the highest-paid employee.*
select max(sal) from emp;

-- 12. *Show the total salary paid to SALESMANs.*
select sum(sal) from emp where job = 'salesman';

-- 13. *List employees whose names start with 'S'.*
select ename from emp where ename like 's%';

-- 14. *Find employees who report to manager 7839.*
select ename , mgr from emp where mgr = 7839 ;

-- 15. *Display employee names and their hire dates sorted by newest first.*
select ename , hiredate from emp order by hiredate desc;

-- 16. *Show all employees who have the same salary as someone else.*
select ename , sal from emp where sal in (select sal from emp group by sal having count(sal)>1);
select ename,sal,deptno from emp where sal in (select sal from emp group by sal having count(sal)>1);

-- 17. *List departments that have no employees.*
select dname,deptno from dept group by deptno having count(deptno)=0;
select dname,loc from dept where deptno not in (select deptno from emp);
select emp.deptno,dname from emp right join dept using(deptno);