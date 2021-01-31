-- 1. Write a query that returns all 
-- employees (emp_no), 
-- their department number, 
-- their start date, 
-- their end date, 
-- and a new column 'is_current_employee' that is a 1 if the employee is still with the company and 0 if not.
SELECT
    e.emp_no,
    de.dept_no,
    e.hire_date AS start_date,
    de.to_date AS end_date,
    CASE 
        WHEN to_date > NOW() 
        THEN 1
        ELSE 0
    END AS is_current_employee
FROM employees e
JOIN dept_emp de;

-- 2 Write a query that returns all employee names, and a new column 'alpha_group' that returns 'A-H', 'I-Q', or 'R-Z' 
-- depending on the first letter of their last name.
SELECT
    CONCAT('first_name', ' ', 'last_name') AS full_name,
    CASE
        WHEN LEFT(last_name, 1) IN ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
        THEN 'A-H'
        ELSE 'R-Z'
        END AS alpha_group
FROM employees

-- 3. How many employees were born in each decade?
SELECT decade_born, COUNT(*)   
FROM
    (SELECT CASE
        WHEN YEAR(birth_date) BETWEEN 1990 AND 1999
            THEN '90s'
        WHEN YEAR(birth_date) BETWEEN 1980 AND 1989
            THEN '80s'
        WHEN YEAR(birth_date) BETWEEN 1970 AND 1979
            THEN '70s'
        WHEN YEAR(birth_date) BETWEEN 1960 AND 1969
            THEN '60s'
        WHEN YEAR(birth_date) BETWEEN 1950 AND 1959
            THEN '50s'
        ELSE 'Error'    
    	END AS decade_born
    FROM employees                
    ) as a
GROUP BY decade_born;

-- BONUS ROUND
-- What is the average salary for each of the following department groups: 
-- R&D, Sales & Marketing, Prod & QM, Finance & HR, Customer Service?

SELECT a.dept_groups, AVG(salary)
FROM (SELECT
        dept_no,
        CASE
            WHEN dept_name IN ('Research', 'Development') THEN 'R&D'
            WHEN dept_name IN ('Sales', 'Marketing') THEN 'Sales & Marketing'
            WHEN dept_name IN ('Production', 'Quality Management') THEN 'Prod & QM'
            WHEN dept_name IN ('Finance', 'Human Resources') THEN 'Finance & HR'
            ELSE dept_name
        END AS dept_groups
    FROM departments) AS a   
JOIN dept_emp USING(dept_no)
JOIN salaries USING(emp_no)
GROUP BY a.dept_groups;

