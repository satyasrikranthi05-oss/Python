#OOPS
#--------------------------------------------------------------------------------------------06-11-2026--------------------------------------------------------------------------------------------------
#syntax
"""class classname() :
    #attributes --> name,age, place
    name = "pooja"
    age = 28
    place = "vja"
    def fname(method_name): 
        print("statements.....")
a = classname() # a is object
print(dir(a))
a.fname() 
"""
#Class declartion
"""
class Details():
    name = "pooja"
    age = 28
    place = "vja"
    def display(self):
        print(self.name,self.age,self.place)
a = Details()
print(dir(a))
a.display()
"""
#object instantiation -- can create multiple objects
"""
class details( ):
    def data(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = details()
print(dir(a))
a.data("Noshad",20,"Vja")
a.display()
a.data("Reena",34,"Chennai")
a.display( )

b = details( )
# print(dir(b))
b.data("Satya",21,"Vja")
b.display( )

c = details( )
c.data("Shanab",22,"Hyd")
c.display( )
 """

#object initialization
"""
class details( ):
    #creating a constructor
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
a = details("noshad",28,"vjja")
print(dir(a))
a.display()
"""
"""
class details( ):
    def __init__(self,name,age,place):
        self.name = name
        self.age = age
        self.place = place
    def display(self):
        print(self.name,self.age,self.place)
#a = details(name = input("Name: ")),(age = int(input("Age: "))),(place = input("Place: "))
a = details(eval,input().split(","))
a.display()

class details( ):
    #creating a constructor
    def __init__(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.place = input("Place: ")
    def display(self):
        print(self.name,self.age,self.place)
a = details()
print(dir(a))
a.display()
"""
# -------------------------------------------------------------------------------------07-11-2026-----------------------------------------------------------------------------------------------------------
#difference between _ and __
"""when user wants to create a variable with __ our python interpreter treats it as a special variable to avoid name conflicts with methods and inner classes """
"""
class Employee() :
    def __init__(self):
        self.name = "pooja"
        self._mailid = "pooja@codegnan.com"
        self.__salary = 10000
class Employee2():
    def  __init__(self):
        self.name = "satya"
        self._mailid = "satyasri@gmail.com"
        self.__salary = 20000
class Employee3( ):
    def __init__(self):
        self.name = "noshad"
        self._mailid = "noshad@gmail.com"
        self.__salary = 30000
a = Employee( )
print(dir(a))
print(a.name)
print(a._mailid)
# print(a.__salary) # will give error cant be called directly
print(a._Employee__salary) # private variable can be called using class name
a = Employee2( )
print(a.name)
print(a._mailid)
print(a._Employee2__salary)
a = Employee3( )
print(a.name)
print(a._mailid)
print(a._Employee3__salary)
"""
#4 PILLARS OF OOPS
# 1-------------------------Polymorphism
# operator overloading ---

"""
a = 2
b = 5
print(a + b)
print(a.__add__(b))
print(a.__add__(10))
print(a.__sub__(1))
print(a.__mul__(3))
# print(a.__div__(10))
print(a.__pow__(2))
print(a.__le__(1))
print(a.__ge__(0))

a = [1,2,3,4,5]
b = [5,6,7,8,9,10]
print(a + b)
print(a.__add__(b))
print(a.__getitem__(3))
print(b.__getitem__(5))

a = "code"
b = "gnan"
print(a + b)
a = "python"
b = "course"
print(a.__add__(" " + b).title( ))
print("noshad".__add__(" "+ "shaik").title())
"""
#operator overriding
"""
class A():
    def __init__(self,a):
        self.a = a
    def __add__(self, value):
        return self.a*value.b
class B( ):
    def __init__(self,b):
        self.b = b
x = A(10)
y = B(5)
print(x + y)
"""

#method overloading
"""
class new( ):
    def sum(self, a = None, b = None, c = None):
        if a != None and b != None and c != None:
            print("The sum is:", a + b + c)
        elif a != None and b != None:
            print("The product is:",a * b)
        else:
            print("Program ends")
x = new()
x.sum()
x.sum(2,3,4)
x.sum(6,4)
"""
"""
class new( ):
    def sum(self, a = 5, b = 6, c = 3):
        if a != 2 and b != 2 and c != 2:
            print("The sum is:", a + b + c)
        elif a != 3 and b != 4:
            print("The product is:",a * b)
        else:
            print("Program ends")
x = new()
x.sum()
"""
#method overriding
"""
class Animal( ):
    def speak(self):
        print("Animal can make sounds")
class Dog():
    def speak(self):
        print("Dog can barks")
a = Animal( )
b = Dog( )
a.speak ( )
b. speak( )
"""
#task
"""
class car( ):
    def vechile(self):
        print("Car")
class bike():
    def vechile(self):
        print("Bike")
a = car( )
b = bike( )
a.vechile ( )
b.vechile( )
"""
# ---------------------------------------------------------------------------------------09-11-2026 ---------------------------------------------------------------------------------------------------------
# INHERITANCE - inherting the parent class to the child class
#single inheritance
"""
class RBI(): #parent class
    cash = 100000
    def available_cash(cls):
        print("Available cash is: ",cls.cash)
        #print("Available cash is : ", RBI.cash)
class SBI(RBI):
    pass
class HDFC(RBI):
    cash = 50000
    def new_cash (cls):
        print("New cash is: ",cls.cash + cls.cash)
        #print("New cash is: ", RBI.cash + cls.cash)
a = HDFC()
a.available_cash()
a.new_cash()
"""
# multiple inheritance
"""
class Father(): #parent 1 class
    height_father = "150 cm"
    def height(self):
        print("Height of father: ",self.height_father)
class Mother( ): # parent 2 class
    weight_mother = "50 kgs"
    def weight(self):
        print("Weight of mother: ",self.weight_mother)
class kid(Father, Mother):# child class
    dob = "May 17"
    def kid_dob(self): 
        print("DOB of kid: ",self.dob)
a = kid()
a.height()
a.weight()
a.kid_dob()
"""

"""
class father():
    def height(self):
        print("5.5 inches")
class mother():
    def weight(self):
        print("60 kgs")
class kid(father,mother):
    def dob(self):
        print("Just born")
c = kid()
c.height()
c.weight()
c.dob()
"""

#multi - level
"""
class grandfather():
    def land(self):
        print("land")
class father(grandfather):
    def house(self):
        print("house")
class kid(father):
    def bike(self):
        print("bike")

a = kid()
a.land()
a.house()
a.bike()
"""

#hierarchical means one parent class is inherited by multiple child class
class employee():
    def company(self):
        print("Company name")
class trainer(employee):
    def teaching(self):
        print("Courses")
class developer(employee):
    def develop(self):
        print("code")

a = developer()
a.company()
a.trainer()
a.develop()


















