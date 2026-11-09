# Q1)
def right_angled(rows):
    for i in range(1, rows + 1): # runs the loop for 5 times
        print(" * " * i)
right_angled(5)


print("-----------------------------------------------------------------------------------------------")


#Q2)
def inverted(rows):
    for i in range(rows + 1, 0, -1):
        print ( " * " * i)
inverted(5)
print("-----------------------------------------------------------------------------------------------")


# Q3
def square(rows):
    for i in range(1, rows + 1):
        print(" * " * rows)
square(4)

print("-----------------------------------------------------------------------------------------------")

#Q4

def pyramid(rows):
    for i in range(1, rows + 1):
        print("  "  *( rows - i)+ " * " * i) # Prints spaces before the stars , Prints an increasing number of stars.
pyramid(5)


