# List of products: (quantity, price)
products_in_stock = [(20, 5.50), (15, 8.30), (37, 3.85), (4, 11.60)]

# Calculate the total value using map and lambda function
total_value = sum(list(map(lambda product: product[0] * product[1], products_in_stock)))

# Display the result
print("Total value:", total_value)
