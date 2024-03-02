
import CarClass as c

def main():

    i = 0

    car = c.Car("2010", "Mazda")

    while i < 5:
        car.accelerate()
        print(car.get_speed())
        i += 1

    i = 0

    while i < 5:
        car.brake()
        print(car.get_speed())
        i += 1

main()