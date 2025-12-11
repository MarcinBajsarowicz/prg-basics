grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

pep = list(filter(lambda x: x != 2.0, grades ))


mean = sum(pep) / len(pep)

# Print the result
print(f"Arithmetic mean for grades <> 2.0 is {mean:.2f}")