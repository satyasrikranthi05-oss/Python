#loops
#for, while,break,continue,pass loops

#for loop- sequence iterations
"""
a = [10,20,30,40,50]
print(a) # returns in list  in row
"""
"""
# for loop --> i means temporary variable, a is defined variable, in is membership operator 
a = [10,20,30,40,50]
for i in a :
    print(i) # returns in sequence one by one in column

a = [10,20,30,40,50]
for i in a :
    print(a)
#difference between print(i) and print(a)
#print(i) --> returns in sequence one by one in column
#print(a) --> returns no of values in a list times

a = [10,20,30,40,50]
for i in a:
    print(i, end = " ")
"""
#end is used to get output in side by side instead of one by one

#datatype --> list, tuple, set and dict
"""
a = [5,6,7,8,9,10]
for i in a:
    print(i)
print(type(a))
print(type(i))

a = (5,6,7,8,9,10)
for i in a:
    print(i)
print(type(a))
print(type(i))

a = {5,6,7,8,9,10}
for i in a:
    print(i)
print(type(a))
print(type(i))
print("*********************************************************************************************************************************************")
a = {"name" : "pooja" , "city" : "vja" , "year" : 2026}
for i in a:
    print(i)
    #print(type(a))
    #print(type(i))
for i in a.keys():
    print(i)
    print(type(a))#type will be dict
    print(type(i))#type will be str
for i in a.values():
    print(i)
    print(type(a))#type will be dict
    print(type(i)) #type will return str,str,int
for i in a.items():
    print(i)
    print(type(a))#type will be dict
    print(type(i)) #type will return tuple

print("***********************************************************************************************************************************************")
a = [4.5,6.7,8.9]
for i in a:
    print(i)
print(type(a)) # return type will be list
print(type(i))#type will be float

a = ["python","java","dsa"]
for i in a:
    print(i)
print(type(a)) # return type will be list
print(type(i))#type will be str

a = [3+9j,8+9j]
for i in a:
    print(i)
print(type(a)) # return type will be list
print(type(i))#type will be complex

a = [True, False]
for i in a:
    print(i)
print(type(a)) # return type will be list
print(type(i))#type will be bool

print("************************************************************************************************************************************************")

#tasks
#

#a  = ["vja","hyd","vzg"]
#outpput -> ["VJA","HYD","VZG"]

a  = ["vja","hyd","vzg"]
b = [ ]
for i in a:
    b.append(i.upper())
    #print(b)
print(b)
#difference between using print inside loop and outside loop
#inside loop: it will append one value by one value and returns after adding each value
#Outside loop: it will return all values at a time in a list
#.upper(), .lower() string methods will not apply to a variable because a is a list , will apply to i -accessing each value in list

print("************************************************************************************************************************************************")

# while loop --> contious iteration
#if for a defined variable

a = 10
while a > 1:
    print(a) # without increment or decrement if we print it return continously

a = 10
while a > 1:
    print(a)
    a = a - 1 # it returns 10 to 2

a = 10
while a >= 1:
    print(a)
    a = a - 1 # it returns 9 to 1

a = 10
while a >= 1:
    a = a - 1
    print(a) # it returns 9 to 0

a = 10
while a >= 1:
    a = a - 1
print(a)  # it returns 1 only, as it is written outside the loop

a = 15
while a > 1:
    print(a)
    a += 1 # it returns continously wihout breaking so, if in a defined variable the value is higher use decrement

a = 15
while a > 1:
    print(a)
    a -= 1 #  it returns 15 to 2

a = 5
while a < 20:
    print(a)
    a += 1 # it returns 5 to 19


#tasks
#number is even or odd
while True:
    num = int(input("Enter a number:  "))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

#leap year
while True:
    year = int(input("Enter a year: "))
    if year % 4  == 0:
        print("Leap year")
    else:
        print("Not a leap year")

#guests code
while True:
    names = ["Pooja", " Riya " , "Priya", "Noshad", "Satya"]
    name = input("Enter name of guest: ")
    if name in names:
        print(f" Welcome {name}")
    else:
        print("Welcome Guest")

#bakery
while True:
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

#task
#attendace tracker
"""
students = int(input("Enter number of students: "))
P = 0
A = 0
for i in range(1,students+1):
    c = input(f"Student {i} - P/A: ")
    if c == "P":
        P = P + 1
    elif c == "A":
        A = A + 1
print("---------------------------Attendance Tracker--------------------------")
print("Total no of students: ", students)
print("Total presenties: ",P)
print("Total absenties :  ",A)
"""
#range loop --> the range function returns a sequence of numbers, starting from zero, by default it starts with zzero and increments by 1 by 1 and stops before a specified number.

"""for i in range(10): # 10 is stop value, by default starts with 0
    print(i,end = " ")
print("---------------------------------------")
for i in range(5,15): # 15 is stop value, 5 is start value
    print(i,end = " ")      
"""
#tasks
"""
#1
for i in range(0,20,2):
    print(i, end = " ")
print("\n")
#2
for i in range(5,50,5):
    print(i, end = " ")
print("\n")
#3
for i in range(3,30,3):
    print(i, end = " ")
print("\n")
"""

#student marks
"""
while True:
    marks = int(input("Enter marks of students: "))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range (50,71):
            print("Grade D")
    else:
        print("Fail.")

"""
#difference between break, continue and pass
#break - it is used to terminate the entire loop
#Continue – it is used to skip the current iteration, and the rest of the code will continue
#pass – it is a null statement; it does nothing, but syntactically we need it (it is place holder)

# we can use only in for and while
#break
"""
a = 10
while a > 1:
    print(a)
    a = a - 1
    if a == 6:
        break

a = 20
while a > 1:
    a = a - 1
    if a == 6:
        break
    print(a)

for i in range(25):
    if i == 18:
        break
    print(i)

a = "python"
for i in a:
    if i == "h":
        break
    print(i)
"""

#contiune
"""
a = 30
while a  > 10:
    a = a - 1
    if a == 20:
        continue
    print(a)


for i in range(15):
    if i == 10:
        continue
    print(i)

a = "python"
for i in a:
    if i == "y":
        continue
    print(i)

"""
#pass
"""
for i in range(10):
    if i == 5:
        pass
    print(i)


a = 20
while a > 5:
    print(a)
    a = a - 1
    if a == 10:
        pass
"""











        
