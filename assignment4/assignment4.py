# === TASK 1 ===
import pandas as pd
import numpy as np

# 1a.) Create DF from dict:
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
print(df)
task1_data_frame = df

# 1b.) Add new column:
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# 1c.) Modify existing column:
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# 1d.) Save DF as CSV file:
task1_older.to_csv("employees.csv", index=False)


# === TASK 2 ===
# 2a.) Read data from CSV file:
task2_employees = pd.read_csv("employees.csv")
print(task2_employees)

# 2b.) Read data from JSON file:
json_employees = pd.read_json("additional_employees.json")
print(json_employees)

# 2c.) Combine DFs:
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)


# === TASK 3 ===
# 3a.) Use head() method:
first_three = more_employees.head(3)
print(first_three)

# 3b.) Use tail() method:
last_two = more_employees.tail(2)
print(last_two)

# 3c.) Get shape of DF:
employee_shape = more_employees.shape
print(employee_shape)

# 3d.) Get info:
print(more_employees.info())


# === TASK 4 ===
# 4a.) Load CSV:
dirty_data = pd.read_csv("dirty_data.csv")
print(dirty_data)
clean_data = dirty_data.copy()

# 4b.) Remove duplicate rows:
clean_data.drop_duplicates(inplace=True)
print(clean_data)

# 4c.) Convert age to numeric:
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors= "coerce")
print(clean_data)

# 4d.) Convert salary to numeric:
clean_data['Salary'] = clean_data['Salary'].replace(["unknown", "n/a"], pd.NA).fillna("NaN")
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")
print(clean_data)

# 4e.) Fill missing numeric values:
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(clean_data)

# 4f.) Convert Hire Date to datetime:
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], format="mixed", errors="coerce")
print(clean_data)

# 4g.) Strip extra whitespace and standarize:
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(clean_data)

# pytest -v -x assignment4-test.py