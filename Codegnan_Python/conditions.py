#conditions
#if conditions using comparison operators
#<,>,<=,>=,!=,==
"""a = 10
b = 15
if a < b:
    print("true")"""
"""
a = 10
b = 15
if a > b:
    print("true")"""

"""
a = 7
b = 12
if a!= b:
    print("true")"""
"""
a = 2
b = 4
if a >= b:
    print("true")"""
"""

a = 30
b = 40
if a != b:
    print("true")


a = 5
b = 10
if a == b:
    print("true") """

"""
a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
if a < b:
    print("less")

a = int(input("Enter a value: "))
if a != 7:
    print("not equal")

a = "Python"
if a == "Python":
    print("Match")

a = "Python"
if a != "Java":
    print("Not a Match") """


#if conditions using logical operators
# and, or, not
"""
a = 3
b = 6
if a < b and b > a:
    print("True")


a = 4
b = 8
if a <= b and b >= a:
    print("true")

"""
"""
a = 5
b = 7
if a != b and a == b:
    print("true")


a = 5
b = 7
if a != b or a == b:
    print("true")


a = 3
b = 6
if a < b or b > a:
    print("True")
"""
"""
a = 4
b = 8
if a <= b or b >= a:
    print("true")
"""
"""
a = 4
b = 8
if not a<b:
    print("true")
"""
"""
a = 4
b = 8
if not a < b and b > a:
    print("true") """
"""
a = int(input("Enter a number: "))
b = int (input("Enter a number: "))
if a > b and b < a:
    print("True")

a = int(input("Enter a number: "))
b = int (input("Enter a number: "))
if a > b or b < a:
    print("True")


a = int(input("Enter a number: "))
b = int (input("Enter a number: "))
if not a > b and b < a:
    print("True") """

"""
#if condition by using  identify operators
#is, is not
a = 4
if type(a) is int:
    print("It is int")

 
a = 4
if type(a) is not int:
    print("It is int")


a = int(input("Enter a number:  "))
if type(a) is int:
    print("It is int")


a = input("Write: ")
if type(a) is not int:
    print("It is not int")

a = "hello world"
if type(a) is not int:
    print("It is not int")

"""
#if condition by using  membership operators
"""
a = 1,2,3,4,5,6,7,8,9,10
if 10 in a:
    print("True")


a = 1,2,3,4,5,6,7,8,9,10
if 20 in a:
    print("True")


a = 1,2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("True")

a = int(input("Enter a number: "))
if 30 in a:
    print("True") # error

a = 1,2,3,4,5,6,7,8,9,10
b = int(input("Enter a number: "))
if b in a:
    print("True")

a = [1,2,3,4,5,6,7,8,9,10]
b = int(input("Enter a number: "))
if b in a:
    print("True")
"""
    
# if else by using comparison operators
"""
a = 6
b = 12
if a < b:
    print("less")
else:
    print("true")



a = 6
b = 12
if a == b:
    print("less")
else:
    print("true")

"""
"""
# if else by using logical operators

a = 6
b = 12
if a < b and b > a:
    print("less")
else:
    print("true")

a = 8
b = 16
if a > b or b > a:
    print("less")
else:
    print("true")


a = 2
b = 4
if not a < b and b > a:
    print("less")
else:
    print("true")
print("**************************************************************")
# if else by using identify operators

a = 4
if type(a) is int:
    print("It is int")
else:
    print("Not int")

    
a = "Hello"
if type(a) is not int:
    print("It is not int")
else:
    print("Is different data type")

print("*********************************************************************")
#if condition by using  membership operators

a = [1,2,3,4,5,6,7,8,9,10]
b = int(input("Enter a number: "))
if  b in a:
    print("True")
else:
    print("False")



a = [1,2,3,4,5,6,7,8,9,10]
b = int(input("Enter a number: "))
if  b not in a:
    print("True")
else:
    print("False")
"""

#if-elif-else conditons by using comparisons operators
#advantage --> we can check multiple conditions
"""
a = 3
b = 6
if a < b:
    print("less")
elif b > a:
    print("greater")
else:
    print("true") 


a = 3
b = 6
if a == b:
    print("less")
elif b > a:
    print("greater")
else:
    print("true")

a = 3
b = 2
if a == b:
    print("less")
elif b > a:
    print("greater")
else:
    print("true")


a = 3
b = 2
if a == b:
    print("less")
elif b > a:
    print("greater")
elif a != b:
    print("Not equal")
else:
    print("true")"""



    
#if-elif-else conditons by using logical operators
"""
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a < b and b > a:
    print("both conditions are true")
elif a > b or b > a:
    print("only condition is true")
elif not a < b:
    print("Not True")
else:
    print("True")

"""
"""
#if-elif-else conditons by using membership operators
a = [1,2,3,4,5,6,7,8,9,10]
b = int(input("Enter a number: "))
if  b in a:
    print("True")
elif b not in a:
    print("b is not in a - False")
else:
    print("Error")
"""
#if-elif-else conditons by using membership operators
"""
a = input("Enter:  ")
if type(a) is int:
    print("It is int")
elif type(a) is str:
    print("It is string")
else:
    print("Not int and string") """

#mulitple if --> it prints all the true conditions using comparision operators
"""
a = 4
b = 8
if a < b:
    print("less")
if b > a:
    print("greater")
if a != b:
    print("Not equal") 

a = 4
b = 8
if a > b:
    print("less")
if b > a:
    print("greater")
if a != b:
    print("Not equal")"""

#mulitple if --> it prints all the true conditions using logical operators
"""
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > b and b < a:
    print("less")
if b > a or a < b:
    print("greater")
if not a > b:
    print("Not equal")
"""
"""
#mulitple if --> it prints all the true conditions using membership operators

a = [1,2,3,4,5,6,7,8,9,10]
b = int(input("Enter a number: "))
if  b in a:
    print("True")
if b in a:
    print("Number is present")
if b not in a:
    print("Not present")
else:
    print("False")
"""

"""
#mulitple if --> it prints all the true conditions using identify operators

a = (input("Enter a number: "))
if type(a) is int:
    print("Number is int")
if type(a) is int:
    print("Int")
else:
    print("Error")

"""
#nested if cconditions using comparison operators
#diffeerence between nested if and mulitple if
#multiple if -->
"""
a = 5
b = 10
if a < b:
    print("less")
    if b > a:
        print("greater") """
"""
a = 12
b = 15
if a == b:
    print("less")
    if b > a:
        print("greater")"""

"""a = 5
b = 10
if a < b:
    print("less")
    if b == a:
        print("greater") """
"""
a = 30
b = 40
if a < b:
    print("less")
    if b < a:
        print("greater")
    else:
        print("true") 

a = 6
b = 12
if a > b:
    print("less")
    if b < a:
        print("greater")
    else:
        print("error")
else:
    print("true") 

a = 2
b = 4
if a == b:
    print("less")
    if b < a:
        print("greater")
    else:
        print("error")
else:
    print("true")
"""
"""
a = 5
b = 10
if a < b:
    print("less")
    if b > a:
        print("greater")
    elif a != b:
        print("not equal")
    else:
        print("error")
"""
print("***************************************************************************************************************")
#tasks
# using if else
#age above 18 eligible for voting
"""
age = int(input("Enter age:  "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible for vote")
"""
#number is even or odd
"""
num = int(input("Enter a number:  "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

"""
#leap year
"""
year = int(input("Enter a year: "))
if year % 4  == 0:
    print("Leap year")
else:
    print("Not a leap year")
"""

#guests code
"""
name = input("Enter name of guest: ")
if name == "Satya":
    print("Welcome Satya")
else:
    print("Welcome Guest")
"""
"""
names = ["Pooja", " Riya " , "Priya", "Noshad", "Satya"]
name = input("Enter name of guest: ")
if name in names:
    print(f" Welcome {name}")
else:
    print("Welcome Guest")

"""
"""
#tasks --> 06-10-26
#vowels
vowels = ["a", " e " , "i", "o", "u"]
vowel = input("Enter alphabet: ").lower()
if vowel in vowels:
    print("It is vowel")
else:
    print("It is consonant")

#lower() --> it automatically converts the alphabets into lower case so that it will print all(capital + small letters)
"""

#if elif else -- tasks
"""
#bakery
price = int(input("Enter price: "))
if price == 1200:
    print("Red velvet cake")
elif price == 1000:
    print("choco almond cake")
elif price == 800:
    print("chocolate cake")
elif price == 600:
    print("Butterscoth cake")
else:
    print("Cake is not available")
"""

#pizza
"""
pizza = input("Enter pizza name: ")
if pizza == "BBQ pizza":
    print("The price of BBQ pizza is 800rs")
elif pizza == "Crispy Chicken pizza":
    print("The price of Crispy chicken pizza is 600rs")
elif pizza == "Panner pizza":
    print("The price of Panner pizza is 400rs")
elif pizza == "Corn Pizza":
    print("The price of Corn pizza is 300rs")
elif pizza == "French fries & Coke":
    print("The price of French fries & Coke is 200rs")
"""

# multiple if --> only all true conditions will display
"""
age = int(input("Enter age: "))
marks = int(input("Enter marks: "))
attendence = int(input("Enter attendance: "))
if age >= 18:
    print("Eligible for vote")
if marks >= 80:
    print("Eligible for scholar ship")
if attendence >= 80:
    print("Allow to write exams")

"""

#nested if social media login
"""
username = input("Enter username: ")
password = input("Enter password: ")
if username == "satya_sri":
    if password == "170504":
        print("login successful")
    else:
        print("Invalid credenitals")
 """        
 
"""
username = input("Enter username: ")
password = input("Enter password: ")
if username == "satya_sri" and password == "170504":
    print("login successful")
else:
    print("Invalid credenitals")
"""











    




























































































