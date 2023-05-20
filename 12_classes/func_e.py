from func_2 import *
employees = []

employee1 = create_employee(1, "John Doe", 50000,"accountant")

employee2 = create_employee(2, "Smith Ross", 60000,"manager")

add_employee(employees, employee1)
add_employee(employees, employee2)



employee2["name"] = "sdf"

display_all_employees(employees)


