import random

class Insect:

    def __init__(self,w,l,n):
        self.wings = w
        self.legs = l
        self.miles = 0
        self.name = n

    def flight_length(self):
        self.miles = random.randint(1,10)

    def get_distance(self):
        return self.miles

    def get_name(self):
        return self.name