#task 2:
import csv

def read_employees():
    employees_dict = dict()
    list_of_rows = []
    
    try:
        with open("../csv/employees.csv", "r") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    employees_dict["fields"] = row
                else:
                    list_of_rows.append(row)
            employees_dict["rows"] = list_of_rows
            return employees_dict
        
    except Exception as e:
        print(e)
        
employees = read_employees()
print(employees)

#task 3:
def column_index(column_name):
    return employees["fields"].index(column_name)
    
employee_id_column = column_index("employee_id")

#task 4:
def first_name(row_number):
    first_name_search = column_index("first_name")
    row = employees["rows"][row_number]
    first_name_value = row[first_name_search]
    return first_name_value

#task 5:
def employee_find(employee_id):
    
    #nested function to find row
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#task 6:
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches
    
#task 7
def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

sort_by_last_name()
print(employees["rows"])

#task 8:
# def employee_dict(row):
#     employee_dict_result = {}
#     for i in range(len(employees["fields"])):
#         header = employees["fields"][i]
#         value = row[i]
#         if header != "employee_id":
#             employee_dict_result[header] = value
        
#     return employee_dict_result

# row = employees["rows"][10]
# print(employee_dict(row))

#task 8 with zip:
def employee_dict(row):
    employee_dict_result = {}
    
    for header, value in zip(employees["fields"], row):
        
        if header != "employee_id":
            employee_dict_result[header] = value
    
    return employee_dict_result
    
row = employees["rows"][10]
result8 = employee_dict(row)
print(result8)

#task 9:
def all_employees_dict():
    all_employees = {}
    
    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        employee_data = employee_dict(row)
        all_employees[employee_id] = employee_data
    
    return all_employees

result9 = all_employees_dict()
print(result9)

#task 10:
import os

def get_this_value():
    this_value = os.getenv("THISVALUE")
    return this_value

get_this_value()

#task 11:
import custom_module

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("hello")
print("Secret word:", custom_module.secret)

#task 12:
import csv 

def read_minutes():
    
    #nested file reader func
    def read_one_csv(csv_pathway):
        minute_dict = {}
        minute_list = []
        with open(csv_pathway, "r") as file:
            reader = csv.reader(file)
            for index, row in enumerate(reader):
                if index == 0:
                    minute_dict["fields"] = row
                else:
                    minute_list.append(tuple(row))
            
        minute_dict["rows"] = minute_list
        return minute_dict
    
    minutes1 = read_one_csv("../csv/minutes1.csv")
    minutes2 = read_one_csv("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes1:", minutes1)
print("Minutes2:", minutes2)

#task 13:
def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])
    set_result = minutes1_set.union(minutes2_set)
    return set_result
    
minutes_set = create_minutes_set()

#task 14:
from datetime import datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return minutes_list

minutes_list = create_minutes_list()
print(minutes_list)

#task 15:
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted_list = []
    
    for name, date in sorted_list:
        converted_date = date.strftime("%B %d, %Y")
        converted_list.append( (name, converted_date) )

    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerow(converted_list)
    
    return converted_list

write_sorted_list()
        
