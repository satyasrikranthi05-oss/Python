Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#String methods
#len() --> number of characters in a given string
a = "Python"
len(a)
6
b = "Python Course"
len(b) # space is also a one character
13
c = ""
len(c)
0
d = " "
len(d)
1
#count() --> number of repeated words or characters\
a = "Twinkle Twinkle little star"
count(a) # count is a method not built-in function , it will give error
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    count(a) # count is a method not built-in function , it will give error
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
0
a.count("Twinkle")
2
a.count("t")
3
a.count(" ")
3
#find a string --> if we give a character or word it find in the string and gives the position of character
a ="python"
a.find("h")
3
a[3]
'h'
a.find("n")
5
b = "hello" # it takes first occurence
b.find(l)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b.find(l)
NameError: name 'l' is not defined
b.find("l")
2
b[2:4]
'll'
#escape sequence
#\n new line
#\t tab space [1 tab space = 4-8 spaces]
a = "name\nmobileno\tcollege\nmailid\tbranch")
SyntaxError: unmatched ')'
a = "name\nmobileno\tcollege\nmailid\tbranch"
print(a)
name
mobileno	college
mailid	branch
b = "name:Pooja\nmobileno:8908907896\tcollege: urce\nmailid:pooja@codegnan.com\tbranch:cse")
SyntaxError: unmatched ')'
b = "name:Pooja\nmobileno:8908907896\tcollege: urce\nmailid:pooja@codegnan.com\tbranch:cse"
\
print(b)
name:Pooja
mobileno:8908907896	college: urce
mailid:pooja@codegnan.com	branch:cse
#replace() --> replace one word with another word
a = "Wait until you succeed"
a.replace("Wait","Work")
'Work until you succeed'
b = "python c"
b.replace("c","dsa")
'python dsa'
#Uppercase --> convert all into captial letter
a = "code"
a.upper()
'CODE'
#lowercase --> convert all into small letters
a = "HELLO"
a.lower()
'hello'
#capitalize --> First letter should be capital and remaning will be small
c = "python"
c.captialize()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    c.captialize()
AttributeError: 'str' object has no attribute 'captialize'. Did you mean: 'capitalize'?
c.capitalize()
'Python'
#title --> In a sentence, all words first letter will be capital
e ="i am in class"
e.title()
'I Am In Class'
e.capitalize()
'I am in class'
#conditions isupper(), islower(),isalnum(), isdigit(),
a = "java"
a.isupper()
False
a.islower()
True
b = "PYTHON"
b.isupper()
True
c = "data science"
c.startswith("d")
True
c.endswith("e")
True
c.alnum()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    c.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
c.isalnum()
False
d = 7896
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d = "67889"
d.isdigit()
True
e = "pooja123"
e.isalnum()
True
e.isdigit()
False
e.isalpha()
False
f = "pooja@123"
f.isalnum()
False
type(f)
<class 'str'>
#special characters dont work in string methods
#strip --> remove spaces only from left and right dont work for middle spaces
#lstrip() leftstrip --> remove space from left side
#rstrip() right strip --> remove space from right side
a = "           pooja               "
a.strip()# remove spaces from both sides
'pooja'
a.lstrip()
'pooja               '
a.rstrip()# remove spaces from right side
'           pooja'
#concatenation --> adding strings
a = "code"
b = "gnan"
print(a+b)
codegnan
a = "python"
b ="course"
print(a+b)
pythoncourse
print(a + " " + b)
python course
fname = "pooja"
lname ="ch"
print(fname + lname)
poojach
print(fname + " "+ lname)
pooja ch
print(fname.title() + " " + lname.title())
Pooja Ch
print((fname+ " " +lname).title())
Pooja Ch
#split()
a = "c c++ python java"
a.split()
['c', 'c++', 'python', 'java']
b = " i am learning python full stack"
b.split()
['i', 'am', 'learning', 'python', 'full', 'stack']
# join --> joining the stringd
"".join(a)
'c c++ python java'
a = "apple", "banana", "grapes"
" ".join(a)
'apple banana grapes'
"".join(a)
'applebananagrapes'
"l".join(a)
'applelbananalgrapes'
d = "apple"
"l".join(d)
'alplpllle'
#formatting --> adding additional data
a = 3
b = 6
print(a + b)
9
>>> print("The sum is" ,a+b)
The sum is 9
>>> city = "vijayawada"
>>> print("City is", city)
City is vijayawada
>>> #format method()
>>> a = "motu"
>>> b ="pathlu"
>>> print("hello {} {}".format(a,b))
hello motu pathlu
>>> print("hello {} hello {}".format(a,b))
hello motu hello pathlu
>>> print("hello {} hello {}".format(a,b).title())
Hello Motu Hello Pathlu
>>> #fstring
>>> a = "pooja"
>>> b ="ch"
>>> print(f"hello {a}{b}")
hello poojach
>>> print(f"hello {a} hello {b}")
hello pooja hello ch
>>> print(f"hello {a} {b}".title() )
Hello Pooja Ch
>>> #task
>>> a = 2
>>> b = 3
>>> print("Product of two numbers: ", a*b)
Product of two numbers:  6
>>> print("Product of two numbers: {}".format(a*b))
Product of two numbers: 6
>>> print(f"Product of two numbers: {a*b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"Product of two numbers: {a*b}")
...       
Product of two numbers: 6
