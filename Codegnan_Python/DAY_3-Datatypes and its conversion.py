Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Data_types
a = 10
type(a)
<class 'int'>
b = 7.8
type(b)
<class 'float'>
c ='python'
type(c)
<class 'str'>
d = "codegnan"
type(d)
<class 'str'>
e = '''course'''
type(e)
<class 'str'>
f = 4+9j
type(f)
<class 'complex'>
g = 2j+8
type(g)
<class 'complex'>
i = 7j
type(i)
<class 'complex'>
k = 9i
SyntaxError: invalid decimal literal
x = True
type(x)
<class 'bool'>
l = j
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l = j
NameError: name 'j' is not defined
l ="j"
type(l)
<class 'str'>
y = False
type(y)
<class 'bool'>
z = true
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    z = true
NameError: name 'true' is not defined. Did you mean: 'True'?
z ="true"
type(z)
<class 'str'>
#type() --> is a function used to find the type of data type
------------------------------------------------------------------------------------------
SyntaxError: invalid syntax
#Data type conversion
#int
int(8)
8
int(6.7)
6
int(3+9j)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    int(3+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int("pooja")
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    int("pooja")
ValueError: invalid literal for int() with base 10: 'pooja'
int(True)
1
int(False)
0
#string
str(9)
'9'
str(9.0)
'9.0'
str(3+9j)
'(3+9j)'
str("pooja")
'pooja'
str(True)
'True'
str(False)
'False'
#Complex
complex(2)
(2+0j)
complex(7.9)
(7.9+0j)
complex("pooja")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    complex("pooja")
ValueError: complex() arg is a malformed string
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex(8+9j)
(8+9j)
>>> #float
>>> float(8)
8.0
>>> float(9.0)
9.0
>>> float('pooja')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    float('pooja')
ValueError: could not convert string to float: 'pooja'
>>> float(5+9j)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    float(5+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> #bool
>>> bool(7)
True
>>> bool(8.9)
True
>>> bool("pooja")
True
>>> bool(3+9j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> #In integers strings and complex cant be convertiable
>>> #In strings all are convertiable because python string based
>>> #In complex only string cant be convertiable
>>> #In float strings and complex cant be convertiable
