-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/T0kOSe
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.
--DROP TABLE IF EXISTS departments;
--DROP TABLE IF EXISTS department_employee;
--DROP TABLE IF EXISTS department_manager;
--DROP TABLE IF EXISTS employees;
--DROP TABLE IF EXISTS salaries;
--DROP TABLE IF EXISTS title;

-- Create Department Table. --
CREATE TABLE "departments" (
    "dept_no" varchar(10)   NOT NULL,
    "dept_name" varchar(50)   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

-- Create Department Employee. --
CREATE TABLE "department_employee" (
    "emp_no" int   NOT NULL,
    "dept_no" varchar(10)   NOT NULL
   
);

-- Create Department Manager Table. --
CREATE TABLE "department_manager" (
    "dept_no" varchar(10)   NOT NULL,
    "emp_no" int   NOT NULL,
	 CONSTRAINT "pk_department_manager" PRIMARY KEY (
        "emp_no")
   
     
);

-- Create Employees Table. --
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

-- Create Salaries Table. --
CREATE TABLE "salaries" (
    "emp_no" int   NOT NULL,
    "salary" dec   NOT NULL,
    CONSTRAINT "pk_salaries" PRIMARY KEY (
        "emp_no"
     )
);

-- Create Title Table. --
CREATE TABLE "title" (
    "title_id" varchar(10)   NOT NULL,
    "title" varchar(50)   NOT NULL,
    CONSTRAINT "pk_title" PRIMARY KEY (
        "title_id"
     )
);

--- After creating table Imported the data using import/export wizard ----
