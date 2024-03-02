from datetime import date
import StudentClass as s

def main():

    student = s.student(892584643, 'Brando', date(2002,5,18), 'Sr')    

    student.calc_age()

    student.set_dates()

    print(f'Your age is: {student.get_age()}\nYour registration dates are: {student.get_dates()}')

main()