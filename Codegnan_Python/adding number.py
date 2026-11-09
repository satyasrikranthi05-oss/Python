#adding two numbers -- 3 methods
"""
a = 2
b = 4
c = a + b
print(c)

print("-------------------------------------------------")

a = 2
b = 4
print(a+b)

print("-------------------------------------------------------")

print(2+3)
print("---------------------------------------------------------")
"""
#runtime_input()
"""
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a+b)

print("---------------------------------------------------------")

a = float(input("Enter a float number: "))
b = float(input("Enter a float number: "))
print(a+b)

print("---------------------------------------------------------")

a = str(input("Enter a string: "))
b = str(input("Enter a string: "))
print(a+b)

print("----------------------------------------------------------")

a = input("Enter a string: ")
b = input("Enter a string: ")
print(a+b)

print("-----------------------------------------------------------")

fname = input("First Name: ")
lname = input("Last Name:  ")
print((fname + " " + lname).title()) 

print("-----------------------------------------------------------")"""
"""
a = complex(input("Enter a complex number: "))
b = complex(input("Enter a complex number: "))
print(a+b)

print("-----------------------------------------------------------")

a = bool(input("Enter a bool input: "))
b = bool(input("Enter a bool input: "))
print(a+b)
#bool result will equal to number of inputs """

"""
#options

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
option = int(input("Choose the option 1.add 2.sub 3. mul "))
print(a+b)
print(a-b)
print(a*b)

print("------------------------------------------------------------------------------")

a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
option = int(input('''Choose the option
                                         1.add
                                         2.sub
                                         3. mul '''))
print(a+b)
print(a-b)
print(a*b)

print("--------------------------------------------------------------------------")

a = int(input("Enter a value: "))
b = int(input("Enter a value: "))
option = input('''Choose the option
                                         add
                                         sub
                                         mul ''')
print(a+b)
print(a-b)
print(a*b)

print("--------------------------------------------------------------------------")

a = int(input())
b = int(input())
print(a+b)

print("--------------------------------------------------------------------------")

a = input()
print(a)
"""

"""
#swapping two variables
#without using temp variable
a = 10
b = 20
a,b = b,a
print("Value of a: ",a)
print("Value of b: ",b)

#using temp variable
a = 10
b = 20
temp = a
a = b
b = temp
print("Value of a: ",a)
print("Value of b: ",b)

#using arithmetic operators
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("Value of a: ",a)
print("Value of b: ",b)

#using number format
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("Value of a: %d , b = %d" % (a,b))
"""
"""
#tasks
#for float
a = float(input("Enter a float number:  "))
b = float(input("Enter a float number:  "))
a = a + b
b = a - b
a = a - b
print("Value of a: %.2f , b = %.2f" % (a,b))

#string
a = input("Enter a string: ")
b = input("Enter a string: ")
temp = a
a = b
b = temp
print("A is : %s , B is = %s" % (a,b))

"""
#student profile

Student_name = input("Enter a name: ")
student_id = int(input("Enter a roll no:  "))
Student_phone_number = int(input("Enter phone number:  "))
student_email_id = input("Enter email address: ")
college = input("Enter college name: ")
Stream = input("Enter Stream: ")
print("-----------------------------------Student Profle------------------------------------------")
print("Student name:",Student_name)
print("Student id:", student_id)
print("Student Phone number:", Student_phone_number)
print("Student Email id:",student_email_id)
print("College name:",college)
print("Stream:",Stream)

