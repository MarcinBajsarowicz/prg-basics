import math

# Function to calculate the area of a triangle using Heron's formula
def triangle_area(a, b, c):
    # Calculate the semi-perimeter
    s = (a + b + c) / 2
    # Calculate the area using Heron's formula
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Example: Calculate the area of a triangle with sides 3, 4, and 5
a, b, c = 3, 4, 5
area = triangle_area(a, b, c)

# Print the result
print(f'The area of a triangle with sides {a}, {b}, and {c} is {area:.2f}')

a, b, c = 5, 12, 13
area = triangle_area(a, b, c)

# Print the result
print(f'The area of a triangle with sides {a}, {b}, and {c} is {area:.2f}')

a, b, c = 7, 24, 25
area = triangle_area(a, b, c)

# Print the result
print(f'The area of a triangle with sides {a}, {b}, and {c} is {area:.2f}')
