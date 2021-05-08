-- 1. List the following details of each employee: employee number, last name, first name, sex, and salary.

SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM employees e
INNER JOIN salaries s
	ON e.emp_no = s.emp_no
ORDER BY e.last_name

-- 2. List first name, last name, and hire date for employees who were hired in 1986.

SELECT e.first_name, e.last_name, e.hire_date, EXTRACT(YEAR FROM e.hire_date) As hire_year
FROM employees e
GROUP BY e.first_name, e.last_name, e.hire_date
HAVING EXTRACT(YEAR FROM e.hire_date) = '1986'

-- 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

SELECT d.dept_no, d.dept_Name, dm.emp_no, e.last_name, e.first_name
FROM departments d
INNER JOIN department_manager dm
	ON d.dept_no = dm.dept_no
INNER JOIN employees e
	ON dm.emp_no = e.emp_no
GROUP BY d.dept_no, d.dept_name, dm.emp_no, e.last_name, e.first_name
ORDER BY d.dept_no

-- 4. List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT  de.emp_no, e.last_name, e.first_name, d.dept_Name
FROM departments d
INNER JOIN department_employee de
	ON d.dept_no = de.dept_no
INNER JOIN employees e
	ON de.emp_no = e.emp_no
GROUP BY  d.dept_name, de.emp_no, e.last_name, e.first_name

-- 5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT e.first_name, e.last_name, e.sex
FROM employees e
WHERE e.first_name = 'Hercules' AND e.last_name LIKE 'B%'

-- 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT  de.emp_no, e.last_name, e.first_name, d.dept_Name
FROM departments d
INNER JOIN department_employee de
	ON d.dept_no = de.dept_no
INNER JOIN employees e
	ON de.emp_no = e.emp_no
WHERE d.dept_name LIKE 'Sales'
GROUP BY  d.dept_name, de.emp_no, e.last_name, e.first_name

-- 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

SELECT  de.emp_no, e.last_name, e.first_name, d.dept_Name
FROM departments d
INNER JOIN department_employee de
	ON d.dept_no = de.dept_no
INNER JOIN employees e
	ON de.emp_no = e.emp_no
WHERE d.dept_name LIKE 'Sales' OR d.dept_name LIKE 'Development'
GROUP BY  d.dept_name, de.emp_no, e.last_name, e.first_name

-- 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT e.last_name, COUNT(e.last_name)
FROM employees e
GROUP BY e.last_name
