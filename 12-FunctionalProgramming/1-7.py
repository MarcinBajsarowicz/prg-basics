#def is_even(number):
  #  if number % 2 == 0:
   #     return True
    #else:
     #   return False

#n1 = int(input("Enter your number: "))

#result = is_even(n1)

#print(f'Your number is even: {result} ')

is_even = lambda number: number % 2 == 0

# Test the function with a few numbers
test_numbers = [1, 2, 3, 4, 5, 6, 10, 15]

for num in test_numbers:
    if is_even(num):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")