normal_price = float(input("Enter price "))
discount = int(input( "Enter discount % "))
reduction = round((normal_price * discount)/100, 2)
price_with_discount = round(normal_price - reduction, 2)

print(f"The total price with discount : {price_with_discount}. The reduction of price is {reduction}")

