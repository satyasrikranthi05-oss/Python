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




