from datetime import date

class student:

    def __init__(self, id, name, dob, classification):
        self.studentID = id
        self.name = name
        self.birthdate = dob
        self.classification = classification

    def calc_age(self):
        self.age = (date.today() - self.birthdate).days//365

    def set_dates(self):
        if self.classification == 'Sr':
            self.reg_date = '4/1 thru 4/3'
        elif self.classification == 'Jr':
            self.reg_date = '4/4 thru 4/6'
        elif self.classification == 'S':
            self.reg_date = '4/7 thru 4/9'
        else:
            self.reg_date = '4/10 thru 4/12'

    def get_age(self):
        return (self.age)

    def get_dates(self):
        return (self.reg_date)