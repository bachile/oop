
class Car:

    def __init__(self, yrmodel, make):
        self.__year_model = yrmodel
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
