
class Student:
    def __init__(self,name,age,city):
        self.name = name
        self.age = age
        self.city = city
        self.marks = []

        def add_mark(self,mark):
            self.marks.append(mark)
            return self


        def get_all_marks(self):
            return self.marks

        def clac_avg (self,mark):
            my_sum = 0
            for mark in self.marks:
                my_sum += mark
            my_avg = my_sum / len(self.marks)
            return my_avg
studentt = Student("Tarteel",18,"Gaza")



