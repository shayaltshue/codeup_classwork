
------------------------ JOIN_EXAMPLE_DB ---------------------------

-- Use the join_example_db. 
USE join_example_db;

--Select all the records from both the users and roles tables.
SELECT *
FROM users u
JOIN roles r ON u.role_id = r.id;

-- Use join, left join, and right join to combine results from the users and roles tables
-- as we did in the lesson. Before you run each query, guess the expected number of results.

    -- Join
    SELECT *
    FROM users
    JOIN roles ON roles.id = users.id;

    -- Left Join
    SELECT *
    FROM users
    LEFT JOIN roles ON roles.id = users.id;

    -- Right Join
    SELECT *
    FROM users
    RIGHT JOIN roles ON roles.id = users.id;

-- Although not explicitly covered in the lesson, 
-- aggregate functions like count can be used with join queries. 
-- Use count and the appropriate join type to get a list of roles along with 
-- the number of users that has the role. Hint: You will also need to use group by in the query.
SELECT
	r.name AS role_name,
	COUNT(u.id) as count_user
FROM roles r
LEFT JOIN users u ON u.role_id = r.id
GROUP BY r.name;
------------------------ EMPLOYEES ---------------------------

-- 1. Use the employees database
USE employees;

-- 2. Write a query that shows each department along with the name of the current manager for that department.
SELECT 
	d.dept_name AS Department_Name,
	CONCAT(e.first_name, ' ', e.last_name) AS Manager_Name
FROM dept_manager dm
JOIN departments d USING(dept_no)
JOIN employees e USING(emp_no)
WHERE YEAR(dm.to_date) = '9999'
ORDER BY Department_Name;

-- 3. Find the name of all departments currently managed by women.
SELECT 
	d.dept_name AS Department_Name,
	CONCAT(e.first_name, ' ', e.last_name) AS Manager_Name
FROM dept_manager dm
JOIN departments d USING(dept_no)
JOIN employees e USING(emp_no)
WHERE YEAR(dm.to_date) = '9999'
    AND e.gender = 'F'
ORDER BY Department_Name;

-- 4. Find the current titles of employees currently working in the Customer Service department.
SELECT
    t.title as 'Title',
    COUNT(*) as 'Count'
FROM titles t
JOIN dept_emp de USING(emp_no)
JOIN departments d USING(dept_no)
WHERE YEAR(t.to_date) = '9999'
    AND YEAR(de.to_date) = '9999'
    AND d.dept_name = 'Customer Service'
GROUP BY t.title;

-- 5. Find the current salary of all current managers.
SELECT
    d.dept_name AS 'Department Name',
    CONCAT(e.first_name, ' ', e.last_name) AS 'Name',
    s.salary
FROM salaries s
JOIN employees e USING(emp_no)
JOIN dept_manager dm USING(emp_no)
JOIN departments d USING(dept_no)
WHERE YEAR(s.to_date) = '9999'
    AND YEAR(dm.to_date) = '9999';

-- 6. Find the number of employees in each department.
SELECT
    d.dept_no,
    d.dept_name,
    COUNT(*) as num_employees
FROM dept_emp de
JOIN departments d USING (dept_no)
WHERE YEAR(de.to_date) = '9999'
GROUP BY d.dept_no;

-- 7. Which department has the highest average salary?
SELECT
	d.dept_name as dept_name,
	AVG(salary) as average_salary
FROM salaries s
JOIN dept_emp de USING(emp_no)
JOIN departments d USING(dept_no)
WHERE YEAR(de.to_date) = '9999'
	AND YEAR(s.to_date) = '9999'
GROUP BY d.dept_name
ORDER BY average_salary DESC
LIMIT 1;

-- 8. Who is the highest paid employee in the Marketing department?
SELECT
    e.first_name,
    e.last_name
FROM dept_emp de
JOIN salaries s USING(emp_no)
JOIN employees e USING(emp_no)
JOIN departments d USING(dept_no)
WHERE d.dept_name = 'Marketing'
    AND YEAR(s.to_date) = '9999'
ORDER BY s.salary DESC
LIMIT 1;

-- 9. Which current department manager has the highest salary?
SELECT 
    e.first_name,
    e.last_name,
    s.salary,
    d.dept_name
FROM dept_manager dm
JOIN salaries s USING(emp_no)
JOIN employees e USING(emp_no)
JOIN departments d USING(dept_no)
WHERE YEAR(dm.to_date) = '9999'
ORDER BY salary DESC
LIMIT 1;