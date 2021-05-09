--upload the data in following order. Because Foreign Key tries to match the data to the table where the 
--Primary key is located and if it don't find it will give error
-- 1. departments
-- 2. salaries
-- 3. title
-- 4. employees
-- 5. department_employee
-- 6. department_manager

-- DROP TABLE IF EXISTS department_employee;
-- DROP TABLE IF EXISTS department_manager;
-- DROP TABLE IF EXISTS employees;
-- DROP TABLE IF EXISTS salaries;
-- DROP TABLE IF EXISTS title;
-- DROP TABLE IF EXISTS departments;

--Create Departments Table--
CREATE TABLE "departments" (
    "dept_no" varchar(10)   NOT NULL,
    "dept_name" varchar(50)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

--Create Salaries Table--
CREATE TABLE "salaries" (
    "emp_no" int   NOT NULL,
    "salary" dec   NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "emp_no"
     )
);

--Create Title Table--
CREATE TABLE "title" (
    "title_id" varchar(10)   NOT NULL,
    "title" varchar(50)   NOT NULL,
    CONSTRAINT "pk_title" PRIMARY KEY (
        "title_id"
     )
);

--Create Employees Table--
CREATE TABLE "employees" (
    "emp_no" int   NOT NULL,
    "emp_title_id" varchar(10)   NOT NULL,
    "birth_date" date   NOT NULL,
    "first_name" varchar(50)   NOT NULL,
    "last_name" varchar(50)   NOT NULL,
    "sex" varchar(1)   NOT NULL,
    "hire_date" date   NOT NULL,
    CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
     )
);

-- Alter Table employees to add Foreign Key on emp_no and emp_title_id --
ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_no" FOREIGN KEY("emp_no")
REFERENCES "salaries" ("emp_no");
ALTER TABLE "employees" ADD CONSTRAINT "fk_employees_emp_title_id" FOREIGN KEY("emp_title_id")
REFERENCES "title" ("title_id");

-- Create department employee table --
CREATE TABLE "department_employee" (
    "emp_no" int  NOT NULL ,
    "dept_no" varchar(10)   NOT NULL
);
--Alter department_employee table to add foreign key on emp_no --
ALTER TABLE "department_employee" ADD CONSTRAINT "fk_department_employee_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

--Create Department_manager table --
CREATE TABLE "department_manager" (
    "dept_no" varchar(10)   NOT NULL,
    "emp_no" int   NOT NULL
);
-- Alter dept_manager table to add Foreign key on dept_no --
ALTER TABLE "department_manager" ADD CONSTRAINT "fk_department_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");


--Check if all the records uploaded--
-- select * from departments
-- select * from salaries
-- select * from title
-- select * from employees
-- select * from department_employee
-- select * from department_manager
