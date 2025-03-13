# Solution
employees = {}
next_emp_id = 101  # Start Employee IDs from E101

def generate_employee_id():
    global next_emp_id
    emp_id = f"E{next_emp_id}"
    next_emp_id += 1
    return emp_id

def add_employee():
    emp_id = generate_employee_id()
    print(f"Generated Employee ID: {emp_id}")
    name = input("Enter Name: ")
    if not name.replace(" ", "").isalpha():
        print("Error: Name must contain only alphabets.")
        return
    try:
        age = int(input("Enter Age: "))
        if age <= 0:
            raise ValueError
    except ValueError:
        print("Error: Age must be a positive integer.")
        return
    department = input("Enter Department: ")
    employees[emp_id] = {"name": name, "age": age, "department": department}
    print(f"Employee {name} added successfully with ID {emp_id}.")

def remove_employee():
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully.")
    else:
        print("Error: Employee ID not found.")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Error: Employee ID not found.")
        return
    name = input("Enter new Name (press Enter to keep unchanged): ")
    if name and not name.replace(" ", "").isalpha():
        print("Error: Name must contain only alphabets.")
        return
    age_input = input("Enter new Age (press Enter to keep unchanged): ")
    if age_input:
        try:
            age = int(age_input)
            if age <= 0:
                raise ValueError
            employees[emp_id]["age"] = age
        except ValueError:
            print("Error: Age must be a positive integer.")
            return
    department = input("Enter new Department (press Enter to keep unchanged): ")
    if name:
        employees[emp_id]["name"] = name
    if department:
        employees[emp_id]["department"] = department
    print("Employee details updated successfully.")

def search_employee():
    search_key = input("Enter Employee ID or Name to search: ")
    results = [
        {"ID": emp_id, **details}
        for emp_id, details in employees.items()
        if emp_id == search_key or search_key.lower() in details["name"].lower()
    ]
    if results:
        for emp in results:
            print(emp)
    else:
        print("No matching employees found.")

def sort_employees():
    criterion = input("Sort by (name, age, department): ")
    if criterion not in ["name", "age", "department"]:
        print("Error: Invalid sorting criterion.")
        return
    sorted_list = sorted(
        employees.items(), key=lambda x: x[1][criterion]
    )
    for emp_id, details in sorted_list:
        print({"ID": emp_id, **details})

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            sort_employees()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

