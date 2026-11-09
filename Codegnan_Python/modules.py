#--------------------------------------------------------------------------------------------29-10-26--------------------------------------------------------------------------------------------------------
#Difference between module,package and libraries.......................?
#Modules -
"""
  - It is a single python file, which consists python code.
  - It contains functions, variables, and classes.
  - Eg: math.py, random.py and mymodule.py
 """
#Package - 
"""
- One or more python modules known as packages
- Eg: numpy, pandas, matplotlib,reques
"""
#Libraries - 
"""
- A library can consists of both modules and packages
- Eg: numpy, pandas, django, matplotlib
"""

#-----NOTE ----
"""
Every python file is a module and import is a keyword and every python file is saved internally with variable name as __main__.
"""


"""
def greetings(name):
    print("Welcome",name)
"""
"""
a = 5
b = 6
print(a + b)
"""
"""
a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
print(a + b)

details = {"idnos" :[10,20,30], "names" :["pooja","anusha","ambica"], "marks" : [60,70,80]}
"""
#------------------------------------------------------------------------------------30-10-26----------------------------------------------------------------------------------------------------------------
"""
if __name__ == "__main__":
    a = [10,20,30,40,50]
    a.append("code")
    a.extend("code")
    print(a)
"""
"""
def dummy():
    if __name__ == "__main__":
        print("this program is run as script")
    else:
        print("this program is run as module")
dummy()
"""

#math module
"""
print(math.pi)
print(math.pi * 3)
print(math.log(10))
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))
print(math.sqrt(2))
print(math.pow(2,4))
print(math.ceil(2.9))
print(math.floor(4.8))
"""
"""
from math import pi, sqrt,log
print(pi,sqrt(2))
"""
#sys module
"""
import sys
print(sys.path)

for i in sys.path:
    print(i)
print(sys.version)
"""

#os module
import os
#print(os.path)
#print(os.getcwd())
#print(os.listdir())
#print(os.mkdir("oct30"))
#print(os.listdir())
"""
print(os.chdir("C:\\Users\\ssury\\Downloads"))
print(os.listdir())
"""
#random module -- to generate the random numbers in python, randint() function is used, it is defined in random module
#sample -- it returns multiple numbers
"""
import random
a = random.sample(range(20,50),5)
print(a)
"""
#randint()
"""
import random
a = random.randint(60,80)
print(a)
"""
#choice()
"""
import random
a = [3,4,5,6,7,8]
b = random.choice(a)
print(b)
"""


#ludo game
"""
import random
while True:
    dice = int(input("Enter the roll of dice:  "))
    a = random.randint(1,6)
    print(a)
    options = input("Choose options: Yes , No: ")
    if options == "Yes":
        continue
    else:
        break
"""

#------------------------------------------------------------------------------------------------31-10-26-----------------------------------------------------------------------------------------------------

#calendar module
'''import calendar
year = 2026
month = 11
print(calendar.month(year,month))'''
"""
import calendar
year = 2027
print(calendar.calendar(year))

import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
print(calendar.month(year,month))
"""
#date and time module
"""
from datetime import date
a = date.today()
print(a)

import datetime
a = datetime.datetime.now()
print(a)
"""
"""
import time
a = time.time()
print(a) #epoch time

b = time.localtime(a)
print(b)

print(f"Today date is {b.tm_mday}- {b.tm_mon} - {b.tm_year}")
print(f"Time is {b.tm_hour}:{b.tm_min}:{b.tm_sec}")
print(f"Week day is {b.tm_wday}-{b.tm_yday}-{b.tm_isdst}")
"""
#----------------------------------------------------------------------------------------------------------02-11-2026---------------------------------------------------------------------------------------
"""
Regular Expression -They are powerful tools (module) embedded in python which is mainly
used to find a pattern with in a given string or statement or files and we mainly use it for text manipulation
real time - matching 
"""
"""
a = "codegnan is in vja"
print(a)

a = "codegnan\nis\tinvja"
print(a)
"""
#rstring
"""
a = r"codegnan\nis\tinvja"
print(a)
"""
#sequence characters
"""
\w -> it matches alphanumeric
\W -> It matches non alphanumeric
\d -> it matches any digits
\D -> It matches non digits characters
\s -> it returns matches white spaces , for removing white spaces
\S -> it returns matches non white spaces
"""
#RegEx functions -- complie( ), findall( ), split( ), sub( ),search( )
import re
"""
a = "map mat cat money cash code cap maths mug dog donkey"

b = re.compile(r"m\w\w\w\w")
print(b)
"""
#search( )
"""
c = b.search(a)
print(c)
"""
"""
d =re.search(r"m\w+",a)
print(d)
"""
#findall
"""
e = re.findall("m\w+",a)
print(e) #returns words start with m

f = re.findall("c\w+",a)
print(f) #returns words start with c

g = re.findall("d\w+",a)
print(g) #returns words start with d

"""
#split( )
"""
b = re.split(r"m",a)
print(b)

b = re.split(r"\s",a) # it removes white spaces
print(b)
"""
#sub( ) --- for substituion
"""
c = re.sub(r"maths","science",a) # replaces maths with science
print(c)

c = re.sub(r"m", "k",a) # replaces m with k
print(c)


d = "map mat 5 cat money cash code cap maths mug dog donkey 9 10 12"
print(d)

e = re.split(r"\d",d)
print(e)

e = re.search(r"\d",d)
print(e)

f = re.findall(r"\d",d)
print(f)


a = "year 2026 month 11 date 2"
b = re.findall(r"\d+",a)
print(b)
"""
















