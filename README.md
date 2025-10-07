# 🧠 Python Mini Exercises — Data Engineering Basics

---

## 🚀 Exercise 1: Greeting Message Script
<img width="544" height="181" alt="image" src="https://github.com/user-attachments/assets/6c47bdc1-143d-4086-aebb-c70a377692f9" />

### 🎯 Objective  
Create a Python program that takes a user’s name as input and prints a greeting message in uppercase.

### 📝 Description  
- The program prompts the user to type their name.  
- It cleans up extra spaces and converts the name to uppercase.  
- Finally, it displays a friendly personalized greeting message like:  
  **“HELLO, NAMRATHA! WELCOME”**  

### 💡 Key Learning  
- Handling user input and output in Python.  
- String manipulation using built-in methods.  
- Basic text formatting and display logic.  


## 📊 Exercise 2: CSV Parsing Script
<img width="434" height="343" alt="image" src="https://github.com/user-attachments/assets/b9b51c4e-9037-49dc-874a-917d0d9e5b4d" />

### 🎯 Objective  
Write a Python script that reads and parses a CSV file using the **pandas** library to explore dataset contents.

### 📝 Description  
- The script reads an **e-commerce dataset** stored as a CSV file.  
- It displays the first few rows of the dataset to preview the data.  
- It also lists all column names to help understand the dataset’s structure.  
- The dataset contains fields like **User ID**, **Product ID**, **Category**, **Price**, and **Quantity**.

### 💡 Key Learning  
- Using `pandas` to load and inspect data.  
- Understanding dataset structure before analysis.  
- Preparing data for cleaning, transformation, and reporting.  

### 🧩 Outcome  
The script successfully loads the dataset and previews its content, confirming that data is correctly parsed and ready for further analysis. This forms the first step of any **ETL (Extract, Transform, Load)** process.

---

## 🏁 Conclusion
These two exercises demonstrate essential beginner-level Python and data-handling concepts:
- **Exercise 1** builds confidence with input/output operations and string formatting.  
- **Exercise 2** introduces **data parsing and exploration** with `pandas`.  
<img width="503" height="272" alt="image" src="https://github.com/user-attachments/assets/676c50ee-4615-4d8f-bb15-f9c4f85362c3" />

## 📘 Overview
---

## 🗂️ Database Exploration — `Sales_Co`

### 🎯 Objective  
To verify and explore all tables available within the `Sales_Co` database in SQL Server Management Studio (SSMS).

### 📝 Description  
The following query was executed to list all tables in the database:

```sql
USE Sales_Co;
GO
SELECT name
FROM sys.tables;

## 🧾 Database Table Exploration — `Sales_Co`
<img width="510" height="264" alt="image" src="https://github.com/user-attachments/assets/62160841-d660-4627-af85-74628f169514" />

### 🎯 Objective  
To view and validate the data stored in each table within the `Sales_Co` database before creating the star schema.

### 📝 Description  
The following SQL queries were executed in **SQL Server Management Studio (SSMS)** to explore the structure and contents of all tables:

```sql
USE Sales_Co;
GO

SELECT name FROM sys.tables;

SELECT * FROM PRODUCT;
SELECT * FROM INVOICE;
SELECT * FROM CUSTOMER;
SELECT * FROM VENDOR;
SELECT * FROM LINE;
SELECT * FROM EMPLOYEE;
SELECT * FROM EMP;

