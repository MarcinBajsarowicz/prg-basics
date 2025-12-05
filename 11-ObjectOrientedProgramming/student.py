# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.age = 0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.surname = "Szoboszlai"
    student2.name = "Olivia"
    student2.surname = "Brown"
    student2.age = 21
    student3.name  = "Charles"
    student3.surname = "Leclerc"
    student3.age = 28

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name},{student1.surname}, {student1.age} years old')
    print(f'{student2.name},{student2.surname}, {student2.age} years old')
    print(f'{student3.name}, {student3.surname}, {student3.age} years old')
if __name__ == "__main__":
    main()