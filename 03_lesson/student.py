class Student:
    def __init__(self, first_name, last_name, ege, course):
        self.first_name = first_name
        self.last_name = last_name
        self.ege = ege
        self.course = course
    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.ege}, {self.course}'