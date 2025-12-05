class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km
    def print_receipt(self):
        print(f'Distance of a ride {self.distance}')
        print(f'Rate of a ride {self.rate_per_km}')
        print(f'Fare of a ride {self.fare}')



def main():
    # your program
    ride1 = TaxiRide(rate_per_km=2)
    ride2 = TaxiRide(rate_per_km=3)

    ride1.calculate_fare(distance=15)
    ride2.calculate_fare(distance=25)
    
    print('Recipit for ride 1 is:')
    ride1.print_receipt()
    print('Recipit for ride 2:')
    ride2.print_receipt()
    ...

if __name__ == "__main__":
    main()
