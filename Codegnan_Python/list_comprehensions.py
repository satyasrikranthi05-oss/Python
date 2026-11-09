#list comprehensions - every list comprehension can be rewritten as a for loop and every for loop cannot be rewritten as list comprehensions
#for loop lo list comprehension anedi possible avvadhu .............................................. list comprehension lo for loop anedi use cheyyachu
#tasks list comprehension
a = ["python","java","dsa"]
#output- ["PYTHON", "JAVA","DSA"]

# print(a.upper()) --> gives error becuase upper() is used for strings not list
"""
b = str(a)
print(b.upper())

for i in a:
    print(i.upper(), end = " , ") # it gives all in upper case but not gets in list


#syntax
# a = [expr for var in collection/range]

b = [i.upper( ) for i in a]
print(b)


#task 1

a = ["hyd","vja","vzg"] # output: ['Hyd', 'Vja', 'Vzg']
b = [i.title( ) for i in a] (b = [i.captailize( ) for i in a])
print(b)

a = [1,3,4,5,6,8,12,13] #output : [1, 9, 16, 25, 36, 64, 144, 169]
b = [i ** 2 for i in a] #1st method
b = [i * i for i in a] #2nd method
b = [pow(i,2) for i in a] #3rd method
print(b)

#using range
b = [i for i in range(0,21)]
print(b)


#if-usage in list comprehensions

# print only even numbers
"""
b = [i  for i in range(0,16)
     if i % 2 == 0]
print(b)
"""
# print squares of  even numbers
"""
b = [i ** 2  for i in range(0,16)
     if i % 2 == 0]
print(b)
"""
# print only odd numbers
"""
b = [i ** 2  for i in range(0,16)
     if i % 2 != 0]
print(b)

"""
#Print fruits name which contains a
"""
a = ["apple","grapes","kiwi", "mango", "dragon", "berry"]
b = [i  for i in a  if "a" in i]
print(b)

#Print fruits name which doesn't contains a
a = ["apple","grapes","kiwi", "mango", "dragon", "berry"]
b = [i  for i in a  if "a" not  in i]
print(b)
"""
"""
# no elif usage in list comprehensions

# if else usage in list comprehensions
#task
# even number square and odd number * 5
"""
b = [i * i if i % 2 == 0 else i * 5 for i in range(31)]
print(b)
"""
"""
a = [1,2,3,4,5]
b = [5,4,3,2,1]
#output: [6,6,6,6,6]
# a = [expr for var in collection/range]
c = [a[i] + b [ i] for i in range(5)] # 1 method
d = [a[i] + b [ i] for i in range(len(a))]
print(c)
print(d)
"""

#built in functions
#max(), min(), sum()
'''
print(max(7,10,20,40,50,70))
print(min(7,10,20,40,50,70))
a = 7,10,20,40,50,70
print(sum(a))
print(sum([2,3,4,5,6,7,8]))

'''
#task using max min and sum
#marks analysis report

number_of_students = int(input("Enter number of students: "))
students_marks = [ ] 

for i in range(1, number_of_students + 1):
    marks = int(input(f"Enter Student {i } Marks: "))
    students_marks.append(marks)
    max_marks = max(students_marks)
    min_marks = min(students_marks)
    sum_marks = sum(students_marks)
    average = sum_marks / number_of_students
print("----------------------------------------Marks analysis report----------------------------------------")
print("Maximum Marks: ", max_marks)
print("Minimum Marks:", min_marks)
print("Sum of Marks:", sum_marks)
print("Average Marks:", average)

