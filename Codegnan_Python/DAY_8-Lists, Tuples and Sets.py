Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Lists
a =[3,4.5,"ssatya",3+9j,True, False]
print(a)
[3, 4.5, 'ssatya', (3+9j), True, False]
type(a)
<class 'list'>
a = 4.5
type(a)
<class 'float'>
a = [4.5]
type(a)
<class 'list'>
#List methods
#append --> add one item to exisiting list , adding more than one item also possible but it automatically creates another list in existing list
a = ["python", "java","c"]
a.append("c++")

print(a)
['python', 'java', 'c', 'c++']
a.append("c++", "matlab")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("c++", "matlab")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c++","matlab])
          
SyntaxError: unterminated string literal (detected at line 1)
a.append(["c++","matlab"])
          
print(a)
          
['python', 'java', 'c', 'c++', ['c++', 'matlab']]
#extend --> adding one or more items in exisiting list
          
a = ["apple","banana","grapes"])
         
SyntaxError: unmatched ')'
a = ["apple","banana","grapes"]
         
a.extend(["orange","mango"])
         
print(a)
         
['apple', 'banana', 'grapes', 'orange', 'mango']
#insert --> add item at particular position
         
a = ["brinjal","tomato","mango"]
         
a.insert(1,"chilli")
         
print(a)
         
['brinjal', 'chilli', 'tomato', 'mango']



#index --> gives position of any item
         
a = ["hyd","vij","vzg"]
         
a.index("vzg")
         
2
a.copy() # copy() --> copies the list and returns copied list
         
['hyd', 'vij', 'vzg']
b = a = ["hyd","vij","vzg"]
         
b
         
['hyd', 'vij', 'vzg']
c = a.copy()
         
c
         
['hyd', 'vij', 'vzg']
#sort --> ascending order
         
a = ["mango", "apple", "orange", "banana"]
         
a.sort()
         

a
         
['apple', 'banana', 'mango', 'orange']
b = [3,5,2,1,4,20,1,2,67]
         
b.sort()
         
b
         
[1, 1, 2, 2, 3, 4, 5, 20, 67]
c =["apple","orange","Banana", "Grapes"]
         
c.sort(a)
         
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c.sort(a)
TypeError: sort() takes no positional arguments
c.sort()
         
c
         
['Banana', 'Grapes', 'apple', 'orange']
#if your list has both upper case and lower case then first it wll consider uppercase, then lower case
         
#reverse() --> it prints from end to start
         
a = ["black","blue","white","red"]
         
a.reverse()
         
a
         
['red', 'white', 'blue', 'black']
b =[4,7,8,9,1,2,4,5,9]
         
b.reverse()
         
b
         
[9, 5, 4, 2, 1, 9, 8, 7, 4]
#pop() --> it removes the last item or anyy specific position item
         
a = ["java","c","c++"]
         
a.pop() # removes last itemm
         
'c++'
a
         
['java', 'c']
a.pop("java") # it gives error
         
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.pop("java") # it gives error
TypeError: 'str' object cannot be interpreted as an integer
a.pop(0) # removing item at specific position
         
'java'
a
         
['c']
#clear --> clears the entire list
         
a = ["chair","table"]
         
a.clear()
         
a
         
[]
a.append("desk")
         
a
         
['desk']
#len()  --> difference in usage of len() in string and list
         
a = ["hi","hello"]
         
len(a)
         
2
b ="hello"
         
len(b)
         
5
c =["hello"]
         
len(c)
         
1
a.count("hi")
         
1
print("***********************************************************************************************************************************************")
         
***********************************************************************************************************************************************
#tuples
         
a =(3,4.5,"ssatya",3+9j,True, False)
         
a
         
(3, 4.5, 'ssatya', (3+9j), True, False)
type(a)
         
<class 'tuple'>
a.count(8+9j)
         
0
a.count(3+9j)
         
1
a.index(True)
         
4
len(a)
         
6
print("*********************************************************************************************************************************************")
         
*********************************************************************************************************************************************
#Sets
         
a ={3,4.5,"ssatya",3+9j,True, False}
         
a
         
{False, True, 3, 4.5, 'ssatya', (3+9j)}
type(a)
         
<class 'set'>
#set methofd
         
a = {1,2,3,4,5,6,7,8}
         
a.add(9)
         
a
         
{1, 2, 3, 4, 5, 6, 7, 8, 9}
#add --> adds element in existing set
         
a = {1,2,3,4,5,6}
         
b ={5,6,7,8,9,10}
         
a.issubset(b)
         
False
b.issubset(a)
         
False
a = {2,3,4,5,6,7,8}
         
b = {5,6,7,8}
         
b.issubset(a)
         
True
#subset --> part of a main set
         
#superset
         
a = {4,5,6,7,8,9}
         
b ={7,8,9}
         
a.issuperset(b)
         
True
b.issuperset(a)
         
False
#union --> merging of two sets
         
a = {10,11,12,13,14,15,16}
         
b = {14,15,16,17,18,19}
         
a.union(b)
         
{10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
#removing duplicates
         
a = {2,4,6,8,3,4,6,7,8,25,63,3,1}
         
a
         
{1, 2, 3, 4, 6, 7, 8, 25, 63}
#iintersection() --> it returns common elements from the set
         
a = {4,5,6,7,8,9,10)
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a = {4,5,6,7,8,9,10}
         
b = {8,9,10,11,13,15}
         
a.intersection(b)
         
{8, 9, 10}
#update
         
a = {3,4,5,6,7}
         
b ={6,7,8,9,10}
         
a.update(b)
         
a
         
{3, 4, 5, 6, 7, 8, 9, 10}
b
         
{6, 7, 8, 9, 10}
b.update(a)
         
b
         
{3, 4, 5, 6, 7, 8, 9, 10}
b
         
{3, 4, 5, 6, 7, 8, 9, 10}
#difference --> it returns the unique items from set1/2
         
a = {5,6,7,8,9,10,11}
         
b = {9,10,11,12,13,14}
         
a.difference(b)
         
{8, 5, 6, 7}
b.difference(a)
         
{12, 13, 14}
#symmeteric_difference --> deletes the common elements and returns unique items
         
a = {3,4,5,6,7,8}
         
b ={5,6,7,8,9,10}
         
a.symmetric_difference(b)
         
{3, 4, 9, 10}
#difference_update()
         
a = {4,5,6,7,8,9}
         
b = {6,7,8,9,10,11}
         
a.difference_update(b)
         
a
         
{4, 5}
b.difference_update(a)
         
b
         
{6, 7, 8, 9, 10, 11}
#intersection_update()
         
a = {5,6,7,8,9,10,11}
         
b = {9,10,11,12,13,14}
         
a.intersection_update(b)
         
a
         
{9, 10, 11}
b.intersection_update(a)
         
b
         
{9, 10, 11}
#symmetric_difference_update()
         
a = {10,20,30,40,50}
         
b = {30,40,50,60,70}
         
a.symmetric_difference_update(b)
         
a
         
{20, 70, 10, 60}
b.symmetric_difference_update(a)
         
b
         
{50, 20, 40, 10, 30}
#pop() --> removes random element from set
         
a = {2,3,4,5,6,7}
         
a.pop()
         
2
a
         
{3, 4, 5, 6, 7}
a.remove(5)
         
a
         
{3, 4, 6, 7}
a.pop(7) # pop doesn't take any arguments
         
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    a.pop(7) # pop doesn't take any arguments
TypeError: set.pop() takes no arguments (1 given)
#remove()/ discard() -> specific element from set
         
a.discard(6)
         
a
         
{3, 4, 7}
#copy()
         
a = {5,6,7,8,9,20}
         
a.copy()
         
{20, 5, 6, 7, 8, 9}
a.clear()
         
a
         
set()
b = set()
         
b.add(60)
         
b
         
{60}
#clear --> clear the sets
         
#isdisjoint()
         
a = {4,5,6,7,8}
         
b = {9,10,11,12}
...          
>>> a.isdisjoint(b)
...          
True
>>> a = {2,3,4,5}
...          
>>> b = {3,4,5,6}
...          
>>> a,isdisjoint(b)
...          
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    a,isdisjoint(b)
NameError: name 'isdisjoint' is not defined
>>> a.isdisjoint(b)
...          
False
>>> #len()
...          
>>> a = {4,5,6,7,8,9}
...          
>>> len(a)
...          
6
>>> a.count(8) #count() --> is not applicable as sets doesn't contain any duplicates
...          
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    a.count(8) #count() --> is not applicable as sets doesn't contain any duplicates
AttributeError: 'set' object has no attribute 'count'
>>> a.index(5)
...          
Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    a.index(5)
AttributeError: 'set' object has no attribute 'index'
