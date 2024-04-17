use scratch;
show tables;

create table employee(id int, Name varchar(25), dept_id int, salary int);
insert into employee values
(1, 'Tarun', 101, 25000),
(2, 'Varun', 101, 27000),
(3, 'Akshay', 103, 26000),
(4, 'Arun', 102, 30000),
(5, 'Chenna', 102, 25000),
(6, 'Prem', 104, 22000),
(7, 'Balakrishna', 103, 24000),
(8, 'Mani', 105, 26000),
(10, 'uday', 105, 25000);

insert into employee values (9, 'praveen', 104, 22000);

select * from employee; -- id, name, dept_id, salary

create table department(id int, name varchar(25));
insert into department values (101, 'Development'),
(102, 'Testing'),
(103, 'Marketing'),
(104, 'Sales'),
(105, 'Finance');

select * from department; -- id, name

create table project (id int, projectName varchar(25));
insert into project values(111, 'SearchEngine'),
(222, 'Customer Segmentaion'),
(333, 'Retail markert research');

select * from project; -- id, projectName

create table projectMap (projectId int, employee_id int);

insert into projectMap values 
(111, 1),
(111, 2),
(111, 4),
(222, 3),
(333, 7),
(333, 10),
(333, 6);

select * from projectMap;

/*
Applying window function on the given table

*/

-- How many no of employees are asigned into projects, print their id, name, deparment
select *
from employee e
right join projectMap pm
on e.id = pm.employee_id
join department d
on e.dept_id = d.id
join project p
on pm.projectId = p.id;

-- salaries greater than average salary
select * from employee
where salary > (select avg(salary) from employee);

-- applying row number function on the employees
select *,
row_number() over(order by salary desc) as row_num
from employee
where id >5;

-- ranking the employees on salary
select *,
rank() over(order by salary desc)
from employee;

-- ranking based on the department
select *,
rank() over(partition by dept_id order by salary desc) as salary_rank
from employee e
join department d
on e.dept_id = d.id;

-- dense rank on employee salary
select *,
dense_rank() over(order by salary desc) as dense_salary_rank
from employee;

-- dense rank and partition by department
select *,
dense_rank() over(partition by dept_id order by salary desc) as dense_salary_rank
from employee;


-- entile operations on the employee table
select *,
ntile(2) over(order by salary desc) as ntile_rank
from employee;

select *,
ntile(4) over(order by salary desc) as ntile_rank
from employee;