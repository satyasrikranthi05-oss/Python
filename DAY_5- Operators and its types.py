Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Operators
#Arithmetic
a = 2
b = 4
print(a+b)
6
print(a-b)
-2
print(a*b)
8
print(a//b)#integer division
0
print(a/b)#float division
0.5
print(a%b)
2
print(a**b)
16
#Assignment operators -> it was always take updated value
a = 5
b = 9
a+=b
a
14
a-=b
a
5
a*=b
a
45
a//=2
a
22
a/=3
a
7.333333333333333
a**=4
a
2892.049382716049
a%=2
a
0.04938271604896727
b+=2
b
11
b-=2
b
9
b*=3
b
27
b//=2
b
13
b/=2
b
6.5
b**=2
b
42.25
b%=2
b
0.25
#Comparison Operators --> used in conditions
a = 4
b = 2
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
a = 5
b = 5
a == b
True
#Logical Operators
a = 10
b = 20
a < b and b > a
True
a <= b and b >= a
True
a != b and a ==b
False
a < b or a > b
True
a <= b or b >= a
True
a != b or a ==b
True
not True
False
not False
True
#Identify operators
a = 5
type(a) is int
True
type(a) is not int
False
type(a) is not float
True
# Membership Operators
type(a) is str
False
type(a) is not str
True
type(a) is complex
False
type(a) is not complex
True
type(a) is bool
False
type(a) is not bool
True
#Membership Operations
a = 1,2,3,4,5,6,7,8,9,10
8 in a
True
10 not in a
False
25 in a
False
25 not in a
True
#Bit-wise Operators
bin() # used to find binary format of a number
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    bin() # used to find binary format of a number
TypeError: bin() takes exactly one argument (0 given)
a = 4
b = 6
bin(4)
'0b100'
bin(a)
'0b100'
bin(b)
'0b110'
a & b
4
#bitwise operators is used for binary
#and --> only if two bits are 1 then output will be 1
#or --> any one bit is 1 output will be 1
a = 5
b = 7
a | b
7
a = 2
b == 4
False
del b
b = 4
a| b
6
#not --> formula --> -(a+1)
#trick--> value is positive then simply value - 1 and add - symbol
>>> # value is negative --> then simple value - 1 remove -
>>> a = 5
>>> -(a+1)
-6
>>> ~ a
-6
>>> a = 7
>>> ~a
-8
>>> a = -7
>>> ~a
6
>>> #xor --> if two bits are 1s then 0, if two bits are 0s then 0, if one bit is 1 and 0 then 1
>>> a = 3
>>> b = 5
>>> a ^ b
6
>>> a = 8
>>> b = 10
>>> a ^ b
2
>>> #left shift and right shift
>>> #leftshift ---> higher values
>>> #right shift --> lower values
>>> #if left shift then simply add 0 for how many no of shifts to right side
>>> a = 4
>>> a << 2
16
>>> a = 8
>>> a <<3
64
>>> #if right shift then add 0s for how many no of shifts to left side
>>> # and also elimate numbers from right side = no of shifts
>>> a = 9
>>> a >> 3
1
