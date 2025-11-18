price = 200
current_price = 140

price_decrease = price - current_price

percentage_reduction = round((price_decrease / price) * 100)

print(f'Current product price : {current_price}')
print(f'Product price reduced by {percentage_reduction}%')

if percentage_reduction >= 10:
    print("Buy that product!")
else: 
    print("No putchase recomendation")
