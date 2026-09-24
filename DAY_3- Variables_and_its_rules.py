Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Variables
print(4+8)
12
a = 10
print(a)
10
x = 50
print(x)
50
print(X)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(X)
NameError: name 'X' is not defined. Did you mean: 'x'?
Z -= 100
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Z -= 100
NameError: name 'Z' is not defined
Z = 100
print(Z)
100
3 = 90
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
a3 = 90
print(a3)
90
5x = 9
SyntaxError: invalid decimal literal
a0123456789 = 100
print(a0123456789)
100
name = "pooja"
print(name)
pooja
city = "vja"
print(city)
vja
country = "india"
print(country)
india
a = 8
b = 9
print(a+b)
17
fname = "pooja"
lname = "ch"
print(fname+lname)
poojach
print(fname+" "+lname)
pooja ch
print(fname,lname)
pooja ch
a = 3,b=7
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a = 4;b=9
print(a+b)
13
a,b = 6,7
print(a+b)
13
a = 4
b = 8
print(a+b)
12
@ = 9
SyntaxError: invalid syntax
$ = 10
SyntaxError: invalid syntax
_=40
print(_)
40
_a=100
print(_a)
100
if = 20
SyntaxError: invalid syntax
while = 6
SyntaxError: invalid syntax
a = 2,3,4,5,6,7,8,9
print(a)
(2, 3, 4, 5, 6, 7, 8, 9)
a,b,c = 3,4,5
print(a,b,c)
3 4 5
a,b,c = 4,5,6,7,8,9,10
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    a,b,c = 4,5,6,7,8,9,10
ValueError: too many values to unpack (expected 3, got 7)
first name = "pooja"
SyntaxError: invalid syntax
first_name = "pooja"
print(first_name)
pooja
firstname = "pooja"
print(firstname)
pooja
 a = 3
 
SyntaxError: unexpected indent
>>> _a=9
>>> print(_a)
9
>>> a =(1,2,3) #packed values
>>> print(a)
(1, 2, 3)
>>> a,b,c= (5,6,7) # for unpacking values in brackets you should require equal variables to equal values
>>> print(a,b,c)
5 6 7
>>> a = 90
>>> print(a)
90
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> name = "pooja"
>>> print(name)
pooja
>>> Name = "pooja"
>>> print(Name)
pooja
>>> NAME = "pooja"
>>> print(NAME)
pooja
>>> print(nAME)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    print(nAME)
NameError: name 'nAME' is not defined. Did you mean: 'NAME'?
>>> a,b,c=10
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
>>> #when comma used equal variables = equal values
>>> a = b = c = 10
>>> print(a,b,c)
10 10 10
