#functions
"""
a = 10
b = 20
print("The sum is: ",a+b)
print("The diff is:  ",a-b)
print("The product is: ",a * b)

a = 100
b = 200
print("The sum is: ",a+b)
print("The diff is:  ",a-b)
print("The product is: ",a * b)

a = 1000
b = 2000
print("The sum is: ",a+b)
print("The diff is:  ",a-b)
print("The product is: ",a * b)
"""

"""
def calculate (a,b): #calculate is a function name , def is a key word , a and b are arguments
    print("The sum of two numbers: ", a + b)
    print("The diff of two numbers: ", a - b)
    print("The product of two numbers: ", a * b)
calculate(10,20) #10, 20 are positional parameters or parameters 
calculate(100,200)# calculate is calling a function
calculate(1000,2000)

def cal (a,b):
    print("The pow of two numbers: ",a ** b)
    print("The remainder of two nnumbers: ", a % b)
    print("The intger division of two numbers: ", a // b)
cal ( 10 ,5)
cal(10,2)
cal(1 , 2)
"""
"""
def add (a,b):
    c = a + b
    print("Sum of two numbers: " , c)
add(4,5)
"""
"""
#user input and using functions
def add():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print("Sum of two numbers: " ,a + b)
add()


def fullname ():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    print ((fname + "  " + lname).title())
fullname()
"""
# print vs return --> 
"""
def sub (a,b):
    print(a - b)
sub(4,10)

def sub (a , b):
    return a - b
print(sub(3,12))
"""
"""
def cal(a,b):
    c = a + b
    d = a - b
    e = a * b
    print(c)
    print(d)
    print(e)
cal(2,4)
"""
"""
def cal(a,b):
    c = a + b
    d = a - b
    e = a * b
   # return c # it returns value of c and exits the function
   # return d 
   # return e
    return c, d, e # it returns c , d , e values
print(cal(2,4))
"""
# in one code we use only once return 

#tasks
# using operations
"""
def calculate ():
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    options = input("Choose options: add , sub, mul :  " )
    if options == "add":
        print(a + b)
    elif options == "sub":
        print(a - b)
    elif options == "mul":
        print ( a * b)
    else:
        print("Choose correct option")
calculate()
"""
"""
def add():
    print(a + b)
def sub():
    print(a - b)
def mul():
    print(a * b)
while True:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    options = input("Choose options: add , sub, mul :  " )
    if options == "add":
        add()
    elif options == "sub":
        sub()
    elif options == "mul":
        mul()
    else:
        print("Choose correct option")
"""
# --------------------------------------------------------------------------------------------14 - 10 - 26-------------------------------------------------------------------------------------------------------
"""
#keyword and positional arguments
#Positional arguments --> values are passed to a function based on their position.
#keyword arguments --> Values are passed to a function using the parameter names (name=value).

def Details(id,name,mailid):
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid") #-----------------------------------keyword arguments


def Details(id,name,mailid):
    print(id,name,mailid)

Details(id="id",name="name",mailid="mailid") # keyword arguments
Details(id=20,name="uday",mailid="r@gmail.com") # Keyword arguments with different values
Details(30,"venkat","uday@gmail.com") #positional arguments
Details("goetham","dchddjv@.com",30) # Positional arguments with different data types
Details(name="uuu",mailid="ud@gmail.com",id=50) # Keyword arguments in a different order

#id,name,mailid,salary,designation
def Details(id,name,mailid,salary,designation):
    print(id,name,mailid,salary,designation)

Details(id="id",name="name",mailid="mailid",salary="salary",designation="designation") # Keyword arguments
Details(id=10,name="uday",mailid="u@gmail.com",salary=20000,designation="backend") #Keyword arguments with actual values
Details(10,"uday","u@gmail.com",20000,"backend") #Positional arguments
Details("uday","u@gmail.com",20000,"backend",10) #Positional arguments in the wrong order
Details(name="uday",mailid="u@gmail.com",salary=20000,designation="backend",id=10) #Keyword arguments in a different order


#default arguments
def Grocery(item,price):
    print('item is %s' %item)
    print('price is %.2f' %price)
Grocery("rice",2000)
def Grocery(item,price=20000):
    print('item is %s' %item)
    print('price is %.2f' %price)
Grocery("rice")
def Grocery(item="rice",price):
    print('item is %s' %item)
    print('price is %.2f' %price)
Grocery(2000)
def Grocery(item,price,qty=1):
    print('item is %s' %item)
    print('price is %.2f' %price)
Grocery("rice",2000)



#cake,price,qty
def bakery(cake,price,qty):
    print('cake is %s' %cake)
    print('price is %.2f' %price)
    print('qty is %s' %qty)
c=bakery("choclate",2000,"1kg")
def bakery(cake,price=3000,qty="2kg"):
    print('cake is %s' %cake)
    print('price is %.2f' %price)
    print('qty is %s' %qty)
c=bakery("choclate")
def bakery(cake="choclate",price,qty):
    print('cake is %s' %cake)
    print('price is %.2f' %price)
    print('qty is %s' %qty)
c=bakery(2000,"1kg")
def bakery(cake,price,qty="3kg):
    print('cake is %s' %cake)
    print('price is %.2f' %price)
    print('qty is %s' %qty)
c=bakery(4000,"1kg")'''
"""
"""
#task --> total_no of persons given , total amount given, find amount to pay by each person
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def split():
    total_no_of_persons=int(input("Enter total no.of persons : "))
    total_amount=int(input("Enter the total amount :"))
    print(f"Bill for per head:  ", total_no_of_persons // total_amount)
split()


def split():
    total_no_of_persons=int(input("Enter total no.of persons : "))
    total_amount=int(input("Enter the total amount :"))
    bill= amount/persons
    print("no of persons is %d"%persons)
    print("total bill is %d"%amount)
    print("amount for each person is %.2f"%bill)
split()
"""
"""
#--------------------------------------------------------------------------------------15 - 10 - 26 ------------------------------------------------------------------------------------------------------------------------
# star arguments --> used to unpack the elements , as well as to pass the values for variable
a = [3,4,5,6,7,8,9]
print(a) # returns [3,4,5,6,7,8,9]
print(*a) # returns 3 4 5 6 7 8 9

a = (4,5,6,7,8)
print(a) # returns (4,5,6,7,8)
print(*a) # returns  4 5 6 7 8 

a = {6,7,8,9,10}
print(a)  # returns {6,7,8,9,10}
print(*a) # returns 6 7 8 9 10

a = {"year": 2000, "month" : 10}
print(a) # returns  {"year": 2000, "month" : 10}
print(*a) # returns year month
"""
"""
a, b, c = 3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(c) # gives error 3 variables it should have 3 values
"""
"""
a, b, c = 3,4,5
print(a)
print(b)
print(c) # returns 3 4 5

a, b, *c = 3, 4, 5, 6, 7, 8, 9, 10, 11
print(a)
print(b)
print(*c)

a = "codegnan"
print(a)
print(*a) # returns c o d e g n a n

a, b, c = "codegnan"
print(a)
print(b)
print(c) # gives error

a, b, c = "cod"
print(a) # returns c
print(b)  # returns o
print(c) # returns d

a, b, *c = "codegnan"
print(a) # returns c
print(b) # returns o
print(*c) # returns d e g n a n

*a, b, c = "codegnan"
print(*a) # returns c o d e g n
print(b) # returns a
print(c) # returns n


*a, b, *c = "codegnan"
print(*a)
print(b)
print(*c) # gives error 

#variable length arguments --> which  automatically stores in tuple we use * arguments

def check(*a):
    print(a)
    print(*a)
    print(type(a))
check()
b = [2, 3, 4, 5, 6, 7, 8]
check(*b)
c = (5, 6, 7, 8)
check(*c)
d = {5, 6, 7, 8, 10}
check(*d)
e = {"city": "vja"}
check(*e) # returns keys in tuple



        
def check1(*a):
    d = 2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int, float):
            d = d + i
            print (d)
check1()
check1(2, 3, 4, 5, 6)
check1(2, 3, 4.2, 5.3)
check1(1, 2, 3, 5, 2.3, 4.2, "pooja")

"""
"""
#railway ticket task
while True:
    def railway_ticket():
        print("--------------------------------Railway ticket ---------------------------------------")
        ticket = 1000
        print("Choose gender:  Male or Female")
        gender = input().title()
        age = int(input("Enter age: "))
        if gender == "Male":
            if age >= 60:
                ticket = ticket - 30 /100 * ticket
                print("The ticket price for the senior citizen:  ",ticket)
            elif age < 60:
                print("The ticket price is : ", ticket)
        elif gender == "Female":
            if age >= 60:
                ticket = ticket - 50 /100 * ticket
                print("The ticket price for the senior citizen: ",ticket)
            elif age < 60:
                ticket = ticket - 30 /100 * ticket
                print("The ticket price is: ", discounted_price)
        else:
            print("Choose correct gender")
    railway_ticket()
"""
#----------------------------------------------------------------------------------------------------16 - 10 - 26-----------------------------------------------------------------------------------------------
#kwargs(** double star arguments
"""
def check(**a):
    print(a)
    print(type(a))
check()
details = {"idnos": [10,20,30], "names": ["noshad", "shanab", "satya"], "status":["p", "a","p"]}
check(**details)

def check (**a):
    print(a)
    print(type(a))
    for i in a:
        print(i) # returns keys using loops
    for i in a.keys():
        print(i) # returns keys using dict methods
    for i in a:
        print(a[i]) # returns values using loops
    for i in a.values():
        print(i) # returns values using dict methods
    for i in a:
        print(i , a[i]) # returns items using loops
    for i in a.items():
        print(i) # returns items using loops
check()
details = {"idnos": [10,20,30], "names": ["noshad", "shanab", "satya"], "status":["p", "a","p"]}
check(**details)
    
"""
"""
#using both * and **
def usage( *a , **b):
    d = 3
    print(a)
    print(type(a))
    print(b)
    print(type(b))
    for i in a:
        d = d + i
        print(d)
    for i, j in b.items():
        print("Key is: ",i)
        print("Value id: ",j)
usage()
data = (2,3,4,5,3.4,5.2)
usage(*data)
dic = {"names": ["satya", "sri", "noshad"], "marks" : [80, 90, 95]}
print(dic)
usage(**dic)


#ASCII -->Amercian Standard Code for Information Interchange
#chr() --> numbers to char
#ord() --> characters to numbers
#chr usage
print(chr(90))
print(chr(65))
print(chr(91))
# 65 to 90 A TO Z
#ord usage
print(ord("a"))
print(ord("z"))
#  97 TO 122 a to z

#task
for i in range (65,91):
    print(chr(i), end = " ")
print("\n")
for i in range (96,122):
    i = i + 1
    print(chr(i), end = " ")
print("\n")

#names ascii
name = input("Enter the name:  ")
for i in name:
    print(i, ord(i), end = " ")

"""
#---------------------------------------------------------------------------------22-10-26-------------------------------------------------------------------------------------------------------------------
#global and local variables
# a variable is inside and outside the function is called global and local variables
#1st case of global variable
"""
a = 4
def check():
    print("Inside value is: ", a)
check()
print("Outside value is: ", a)
"""
#2nd case of global variable
"""
def check2():
    a = 5
    a = a**2
    print("Inside value is" , a)
check2()
print("Outside value is: ", a)
"""
#third case of both global and local variables
"""
a = 3
b = 6
def check3():
    a = 4
    print("Inside value is: ",a)
    a =5
    print("Updated value of a: ",a + 5)
    b = 12 #local variables
    b = b + a
    print("Value of b is: ", b)
check3()
print("Value of a is: ", a)
print("Value of b is: ", b)
"""
#fourth case using global keyword
#definition of global keyword - when user wants to create a variable inside the function directly and carry forward the updated value we need to use global keyword
"""
a = 6
def final():
    global a
    print("Inside value is" ,a)
    a = 7
    print("Updated value is", a)
    global b
    b = 15
    b = b + a
    print("Value of b is" ,b)
final()
print("A value is" , a)
print("B value is",b)
"""

#---------------------------------------------------------------------23-10-26------------------------------------------------------------------------------------------------------------------------------
#Generators -- no tuple comprehension in the above cases; if we remove those braces and keep parentheses, then the outcome is generators
#difference between generators and list comprehensions..................................?


# syntax for list comprehension:---------------a = [expr for var in collection/range]
"""
a = [i for i in range(16)]
print(a)
print(type(a))

a = (i for i in range(21))
print(a)
print(*a)
print(type(a))


#print(list(a))
print(type(a))
#print(tuple(a))
print(set(a))
"""
#Generators --> a generator is a also a function which can be used as an iterator (loops) by producing group of values where we can use yield keyword

#yield vs return
# return will terminate the function  and gives back the value where as yield can pass the function and go on with every successive iteration

#difference between printvs yield vs return
"""
a,b = [int(x) for x in input("Enter values: ").split( ",")]
def check(a,b):
    while a < b:
        yield a
        a = a + 1
        yield a
print(*check(a,b))

a, b = [int(x) for x in input("Enter values: ").split(",")]
def check(a,b):
    while a < b:
        a = a + 1
        return a # returns 3 and terminates function
    return a # returns 9 and terminates function
print(check(a,b))

"""
"""
#yield v/s return:
def mygen():
    return "vja"
    return "hyd"
    return "vzg"
    return "vja", "hyd", "vzg"
print(*mygen())

def mygen():
    yield "apple"
    yield "grapes"
    yield "mango"
print(*mygen())

#next() ---> built in functin
d = mygen()
print(next(d))
print(next(d))
print(next(d))
print(next(d))
"""
#tasks
#application BMI
"""
while True:
    weight = float(input("Enter your weight:  "))
    height = float(input("Enter height in cms: "))
    bmi = (weight/((height / 100)**2))
    if bmi <= 18.5:
        print("Under weight-----------------Take Good food")
    elif bmi > 18.5 and bmi <= 24.5:
        print("Normal weight")
    elif bmi > 24.5 and bmi <= 29.5:
        print("Healthy weight")
    elif bmi >= 30:
        print("Obseity")
"""

#-------------------------------------------------------------------------------------24-10-26------------------------------------------------------------------------------------------------------------
#built in functions --> 
"""max(),min(),sum(),print(),input(),len(),
dir --> collection of files

print(dir())
print(dir("__builtins__"))
#fromkeys() --> it is dict method

a = "codegnan"
print(a)
print(list(a))
print(tuple(a))
print(set(a))
# print(dict(a)) # it gives error

b = dict.fromkeys(a)
print(b)

b = dict.fromkeys(a,"pooja")
print(b) # in place of non it prints pooja

b['o'] = "priya"
print(b) # what to change a specific value use indexing
"""
"""
while True:
    a = int(input("Enter a value: "))
    b =int(input("Enter b value: "))
    print(a + b)

while True:
    a = float(input("Enter a value: "))
    b =float(input("Enter b value: "))
    print(a + b)

while True:
    a = str(input("Enter a value: "))
    b =str(input("Enter b value: "))
    print(a + b)

while True:
    a = eval(input("Enter a value: "))
    b = eval(input("Enter b value: "))
    print(a + b)
"""
#eval() --> it accepts any datatype no need to specify the datatype and for string during input enter it in quotes
#built in direct ga work avvadhu, datatype undalllli
#zip() --> we can combine multiple collections into one collection
"""
a = [10,20,30,40,50]
names = ["satya","sri","shanab","noshad","pooja"]
print(a+names)


b = zip(a,names)
print(b)

c = list(zip(a,names))
print(c)

d = tuple(zip(a,names))
print(d)

e = set(zip(a,names))
print(e)

f = dict(zip(a,names))
print(f)

#enumerate( ) --> we can give counter to the collection
names = ["harshitha", "vinuthuna","satya","masthan","pooja"]
for i in range(len(names)):
    print(i, names[i])

b = list(enumerate(names,100)) # 100 is starting -- that numbering should be start from 100
print(b)


c = dict(enumerate(names,100)) # 100 is starting -- that numbering should be start from 100
print(c)

d = set(enumerate(names,100)) # 100 is starting -- that numbering should be start from 100
print(d)

e = tuple(enumerate(names,100)) # 100 is starting -- that numbering should be start from 100
print(e)

#map( ) --> each object from a collection and forms a new collection
a = [2,5,7,8,10,12,15,20]
b = [1,3,6,8,17,25,40,60]
c = list(map(max,a,b))
print(c)

d = list(map(min, a, b))
print(d)

e = sum(a) # while doing sum map and datatype is not possible
print(e)
"""



#-------------------------------------------------------------------------------------------27-10-26--------------------------------------------------------------------------------------------------------
# anonymous  functions -- are nameless functions and we use a key word called as lambda to create anonymous functions

#task --> write a function to calculate(2*x+5) where x = 5
"""
def calculate(x):
    print(2 * x + 5)
calculate(5)
    
def cal():
    x = int(input())
    print(2*x+5)
cal()
"""
#syntax
# a = lambda arg:expr
"""
a = lambda x:2*x+5
print(a(5))

a = int(input("Enter a value: "))
b = lambda x:2*x+5
print(b(a))
"""
#task 1
"""
a = "python"
#PYTHON

a = input("Enter: ")
b = lambda x:x.upper()
print(b(a))


b = lambda x:x.upper()
print(b("python"))
"""
#task 2
"""
a = input("Enter: ")
b = lambda x:x.title()
print(b(a))
"""

#task 3
#fname + lname = full name
"""
fname = input("fname:" )
lname = input("lname:")
names = lambda fname,lname: (fname + " " + lname).title()
print(names(fname,lname))

fname,lname = [str(x) for x in input("Enter names: ").split( ",")]
names = lambda fname,lname: (fname + " " + lname).title()
print(names(fname,lname))
"""

#task 4
#power
"""
#a = int(input("Enter num: "))
#b = int(input("Enter num: "))
c = lambda a,b : a ** b
print(c(5,2))
"""

#filter( ) 

a = [2,6,8,10,13,15,20,27,40,60,87,100]
"""
for i in a:
    if i % 2 == 0:
        print(i,end = " " )


b =list(filter(lambda x:x%2 == 0,a))
print(b)
"""
#[],(),{}
"""
a = []
print(type(a))

b = ()
print(type(b))

c = {}
print(type(c))

d = set()
print(type(d))
"""
#-------------------------------------------------------------------------------------------------29-10-26---------------------------------------------------------------------------------------------------
#example
"""
a = [[]," ",(),set(),{},None,3,7.8,3+9j,True, False,"python"]
b = list(filter(None,a)) # it removes empty list, tuples, set, dict, none a values
print(b)
"""
#different types of run time
#str type
"""
a = input("data1 : ")
b = input("data2:  ")
print(a+b)

a,b = input("Enter the names: ").split(",")
print(a+b)

a = [x for x in input("Enter the names: ").split(",")]
print(a)

a,b = map(str,input("Enter the names: ") .split(","))
print(a+b)
"""
#int
"""
a = int(input("enter value : "))
b = int(input("enter value:  "))
print(a+b)

a,b = int(input("Enter the values: ").split(","))
print(a+b) # it gives error 

a = [int(x) for x in input("Enter the values: ").split(",")]
print(a) # [4, 5] output format

a,b = map(int,input("Enter the values: ") .split(","))
print(a+b)

a = list(map(int,input("Enter the values: ").split(",")))
print(a)

a = tuple(map(int,input("Enter the values: ").split(",")))
print(a)

a = set(map(int,input("Enter the values: ").split(",")))
print(a)

a = list(map(eval,input("Enter the values: ").split(",")))
print(a) #eval accepts all datatypes

a,b = map(eval,input("Enter the values: ").split(","))
print(a+b)
"""

a = input("enter the key and value pair: ")
b = dict (i.split(":") for i in a.split(","))
print(b)



























