# Task 3:
import csv

# print first + last names
try:
    with open("../csv/employees.csv", "r") as file:
        reader = csv.DictReader(file)
        names_list= [(col["first_name"] + " " + col["last_name"]) for col in reader]
        print(names_list)
except Exception as e:
    print(f"Error: {e}")
    
# print names with e's:
try:
    with open("../csv/employees.csv", "r") as file:
        reader = csv.DictReader(file)
        names_with_e = [
            f"{row['first_name']} {row['last_name']}"
            for row in reader
            if "e" in row["first_name"].lower() and "e" in row["last_name"].lower()
            ]
        print(f"Names including e's: {names_with_e}")
except Exception as e:
    print(f"Error: {e}")


