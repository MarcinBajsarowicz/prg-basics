# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   number_of_rows = len(seats)
   number_of_seats = len(seats[0])
   return number_of_rows * number_of_seats

def seats_available(seats):
   count = 0
   for row in seats:
      for i in row:
         if i == 'A':
            count += 1
   return count

def seats_booked(seats):
   count = 0
   for row in seats:
      for i in row:
        if i == 'B':
           count += 1
   return count

def seat_status(seats, row, place):
   actual_seat_number = seats[row-1][place-1]

   if actual_seat_number == "A":
      return "Available"
   else:
      return "Booked"
   




print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3,5))