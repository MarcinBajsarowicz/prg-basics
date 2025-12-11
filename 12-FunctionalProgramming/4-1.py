employees = ["SMITH Lucy", "JONES Janet", "LEE Jerry",
             "JACKSON Peter", "JOHNSON Rick",
             "LEWIS Terry", "CLARKE Robin"]

# Filter employees whose last name starts with 'J'
emp_J = list(filter(lambda e: e.split()[0].startswith('J'), employees))

# Print the filtered list
print(emp_J)
