#single inher:
class Animal :
    def __init__(self,name):
        self.name = name
    def print_animal(self):
        print("animals")
class Dog (Animal) :
    def __init__(self,name , is_barking):
        Animal.__init__(self,name)
        self.is_barking = is_barking
    def print_dog(self):
        print("dog")
class Babydog (Dog) :
    def __init__(self,name , is_barking,age):
        Dog.__init__(self,name,is_barking)
        self.age = age
baby_dog = Babydog('Max','yes',3)
baby_dog.print_dog()
print(baby_dog.age)





#mult inher
class Car:
    def __init__(self,type , year):
        self.type = type
        self.year = year

    def print_car(self):
        print("car is",self.type)


class Van:
    def __init__(self, height, city):
        self.height = height
        self.city = city

    def print_var(self):
        print("van is", self.height)
class Bus(Car,Van):
    def __init__(self ,type,year, height, city,color):
        self.color = color
        Car.__init__(self,type,year)
        Van.__init__(self,height, city)

    def print_bus(self):
        print("this is a bus")

bus1 = Bus('vm',2020,3.4,'germany','red')
bus1.print_car()





#local and global
a = 10
b = 5
def sum():
    a = 5
    b = 4
    return a + b
print(sum())          #استدعيت  دالة الجمع
print(a + b)

x = 20
y = 100

def change_x ():
    #global x
   #x = 40
   print(globals()['y'])
   globals()['y'] = 50
   print(y)


change_x()
print(x)
def outer_fun():
    a = 10
    def inner_fun():
        nonlocal a
        a = 30
        b = 40
        print(a)
        print(b)
    inner_fun()
    print(a)
outer_fun()




