#Handlings
"""
Error handling
1. Syntax error -->complie error(it shows in complier)
2. Run time error --> during execution time
3. Logical error --> Error in logic, cant be visible
"""

#Syntax error
"""
for i in range(10) # colon missing 
print(i) #indentation 
"""
#Run_time error
"""
a = int(input("a value: "))
b = int(input("b value: "))
print(a//b) # Zero Division error
"""
#Logical error
"""
a = 10
b = 20
print(a-b)
"""
a = 5
b = 3
if a < b:
    print("true")


#Exception handling --> 4 blocks
#in real life --> 
"""
try --> instructions from which we are excepting the exceptions
except --> exceptions are raised in try block it will handle by this block
else --> optional (no exceptions), it will work when try block successfully exceutes
finally --> always it will display
"""
"""
a = int(input("A value: "))
b = int(input("B value: "))
try:
    c = a//b
    print(c)
except:
    print("Exception is raised")
else:
    print("No exceptions")
finally:
    print("Always")


while True:
    try:
        a = int(input("A value: "))
        b = int(input("B value: "))
        c = a//b
        print(c)
    except:
        print("Exception is raised")
    else:
        print("No exceptions")
    finally:
        print("Always")
"""
#--------------------------------------------------------------------------------02-11-2026----------------------------------------------------------------------------------------------------------------

#File handling
#write()
"""
a = open("satya.txt","w")
a.write("python full stack")
a.close( )

a = open("satya.txt" , "w")
a.write("codegnan")
a.close( )
"""
#append( )
"""
a = open("satya.txt","a")
a.write("\tdata")
a.close ( )
"""

#runtime -- 2 methods
"""
a = open("satya.txt","a")
a.write(input( ))
a.close( )
"""
"""
a = open("satya.txt","w")
b = input( )
a.write(b)
a.close( )
"""

#readlines()
"""
a = open("satya.txt")

print(a.read( )) #it will display entire content
print(a.readline( )) # it will display first line
print(a . read(10)) #it will display 10- number of characters
print(a.readlines( )) #it will display with \n
"""
#writelines() it makes every object side by side
"""
a = open("python.txt","w")
b = ["satya","sri","noshad","shanab","kranthi"]
a.writelines("\n".join(b))
a.close( )
"""

#giving file path and opening files
"""
a = open("functions.py")
print(a.read( ))
"""
"""
a = open(r"C:\Users\ssury\OneDrive\Desktop\Codegnan_Python\patterns.py")
print(a.read( ))
"""




























