
employees = [
    "SMITH, Lucy", "jones, Janet", "LEE, Jerry", "jackson, Peter",
    "JOHNSON, Rick", "Lewis, Terry", "CLARKE, Robin"
]


def filter_employees_by_lastname(employees):

    return list(filter(lambda name: name.split(",")[0].isupper(), employees))


filtered_employees = filter_employees_by_lastname(employees)


print("Employees with last names in capital letters:")
for employee in filtered_employees:
    print(employee)