Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Dict{}
a = {"name":"pooja","year":2026,"month":9}
print(a)
{'name': 'pooja', 'year': 2026, 'month': 9}
type(a)
<class 'dict'>
a = {"name","year","month"}
type(a)
<class 'set'>
a = {"name":"pooja","year":2026,"month":9}
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['pooja', 2026, 9])
a.items() # item = both keys and values
dict_items([('name', 'pooja'), ('year', 2026), ('month', 9)])
#dict_methods
#a.keys(),a.values(),a.items()
#while accessing give only keys, if you give value then there will be error
a["name"]
'pooja'
a.get("name")
'pooja'
a.get("pooja")
a["pooja"]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a["pooja"]
KeyError: 'pooja'
#pop() and popitem()
#pop() - if you want to remove any particular key value
#popitem() -  if you want to remove last item
a = {"city":"vja","state":"ap","country":"india"}
a.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("state")
'ap'
a
{'city': 'vja', 'country': 'india'}
a.popitem()
('country', 'india')
a
{'city': 'vja'}
#adding item in existing dict --> should be in 1 {}
a = {"course":"python","duration":100}
a.update({"year":2026})
a
{'course': 'python', 'duration': 100, 'year': 2026}
a.update({"month":"sep"},{"date":30})
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.update({"month":"sep"},{"date":30})
TypeError: update expected at most 1 argument, got 2
#error --> giving two arguments while using update()
a.update({"month":"sep","date":30}) #no error using {} braces for adding 2 items
a
{'course': 'python', 'duration': 100, 'year': 2026, 'month': 'sep', 'date': 30}
#setdefault --> it will set default/ add
a = {"date":30,"time":11}
a.setdefault("hour",11)
11
a
{'date': 30, 'time': 11, 'hour': 11}
a.setdefault(11,"hour")
'hour'
a
{'date': 30, 'time': 11, 'hour': 11, 11: 'hour'}
#difference betweeb update and default
#in update we should it in dict format where as default no dict format is required
#in update using{} we can any number of items where as in default only iitem can be added
#copy() , clear(), len(), index(), count()
a = {"colour":"white","food":"biryani"}
a.copy()
{'colour': 'white', 'food': 'biryani'}
len(a)
2
a.count("colour")
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a.count("colour")
AttributeError: 'dict' object has no attribute 'count'
a.index("food")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.index("food")
AttributeError: 'dict' object has no attribute 'index'
a.clear()
>>> a
{}
>>> #count () --> will give error as dict doesnt allow duplicates
>>> #index() --> key value pair
>>> #index() --> unordered
>>> #in dict --> keys should be different and values can be same
>>> #dict --> doesnt allow duplicates
>>> a = {"name":"pooja","city":"vja","name":"pooja"}
>>> a
{'name': 'pooja', 'city': 'vja'}
>>> a = {"name":"pooja","city":"vja","name":"priya"}
>>> a
{'name': 'priya', 'city': 'vja'}
>>> a = {"name_1":"pooja","city":"vja","name_2":"pooja"}
>>> 
>>> a
{'name_1': 'pooja', 'city': 'vja', 'name_2': 'pooja'}
>>> #one key multiple values
>>> a ={"ids":10,20,30}
SyntaxError: ':' expected after dictionary key
>>> # for giving mulitple values to one key use list to store the values i.e
>>> a ={"ids":[10,20,30],"names":["Satya","Noshad","Kranthi"]}
>>> a
{'ids': [10, 20, 30], 'names': ['Satya', 'Noshad', 'Kranthi']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['ids', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['Satya', 'Noshad', 'Kranthi']])
>>> a.items()
dict_items([('ids', [10, 20, 30]), ('names', ['Satya', 'Noshad', 'Kranthi'])])
>>> #tasks
>>> a = [9,1,5,2,8,4,6,3,7,0]
>>> #output:[7,6,4,3,0,9,8,5,2,1]
>>> result = a.index(8)+a.index(-4:-6)+a.index(-1)+a.index(0)+a.index(4)+a.index(2)+a.index(3)+a.index(1)
SyntaxError: invalid syntax
result = a.index(8)+a.index(-4)+a.index(-5)+a.index(-1)+a.index(0)+a.index(4)+a.index(2)+a.index(3)+a.index(1)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    result = a.index(8)+a.index(-4)+a.index(-5)+a.index(-1)+a.index(0)+a.index(4)+a.index(2)+a.index(3)+a.index(1)
ValueError: list.index(x): x not in list
a.index(9)
0
result = a.index(7)+a.index(6)+a.index(4)+a.index(3)+a.index(0)+a.index(9)+a.index(8)+a.index(5)+a.index(2)
print(result)
44
a = [9,1,5,2,8,4,6,3,7,0]
#output:[7,6,4,3,0,9,8,5,2,1]
b =[0:6]
SyntaxError: invalid syntax
b =a[0:6]
b
[9, 1, 5, 2, 8, 4]
b =a[0:5]
b
[9, 1, 5, 2, 8]
c = a[6:]
c
[6, 3, 7, 0]
c = a[5:]
c
[4, 6, 3, 7, 0]
c.sort()
c
[0, 3, 4, 6, 7]
c.reverse()
c
[7, 6, 4, 3, 0]
b.sort()
b
[1, 2, 5, 8, 9]
b.reverse()
b
[9, 8, 5, 2, 1]
b_reverse = b.reverse()
b_reverse
print(b_reverse)
None
n = b.reverse()
n
print(n)
None
a = [9,1,5,2,8,4,6,3,7,0]
#output:[7,6,4,3,0,9,8,5,2,1]
b =a[0:6]
b
[9, 1, 5, 2, 8, 4]
c = a[6:]
c
[6, 3, 7, 0]
c = a[5:]
c
[4, 6, 3, 7, 0]
b = b.sort()
b
b.sort()
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    b.sort()
AttributeError: 'NoneType' object has no attribute 'sort'
b = a[0:6].sort()
b
print(b)
None
#output:[7,6,4,3,0,9,8,5,2,1]
b =[0:6]
SyntaxError: invalid syntax
b =a[0:6]
SyntaxError: invalid syntax
b =a[0:6]
b
[9, 1, 5, 2, 8, 4]
b.sort()
b
[1, 2, 4, 5, 8, 9]
b.reverse()
b
[9, 8, 5, 4, 2, 1]
c = a[6:]
c
[6, 3, 7, 0]
c = a[5:]
c
[4, 6, 3, 7, 0]
c.sort()
c
[0, 3, 4, 6, 7]
c.reverse()
c
[7, 6, 4, 3, 0]
b+c
[9, 8, 5, 4, 2, 1, 7, 6, 4, 3, 0]
c+b
[7, 6, 4, 3, 0, 9, 8, 5, 4, 2, 1]
#task 2
a = ["codegnan","python"]
#output ["CODEGNAN","PYTHON"]
b = str(a)
b
"['codegnan', 'python']"
b.upper()
"['CODEGNAN', 'PYTHON']"
#task 3
a = [2,5,7,9,10,15]
#[2,5,6,7,8,9,10,15]
a.append(8)
a
[2, 5, 7, 9, 10, 15, 8]
a.sort()
a
[2, 5, 7, 8, 9, 10, 15]
#insert()
a
[2, 5, 7, 8, 9, 10, 15]
a = [2,5,7,9,10,15]
a
[2, 5, 7, 9, 10, 15]
a.insert(3,8)
a
[2, 5, 7, 8, 9, 10, 15]
#task 4
a = (10,20,30,40)
a
(10, 20, 30, 40)
a.append(50)
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    a.append(50)
AttributeError: 'tuple' object has no attribute 'append'
a.list()
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    a.list()
AttributeError: 'tuple' object has no attribute 'list'
b = a.list()
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    b = a.list()
AttributeError: 'tuple' object has no attribute 'list'
a.list()
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    a.list()
AttributeError: 'tuple' object has no attribute 'list'
b = list(a)
b
[10, 20, 30, 40]
b.append(50)
b
[10, 20, 30, 40, 50]
c = tuple(b)
c
(10, 20, 30, 40, 50)
#task 5
a = [2,3,4,5,6,"c","o","d","e"]
a.extend("code")
a
[2, 3, 4, 5, 6, 'c', 'o', 'd', 'e', 'c', 'o', 'd', 'e']
a = [2,3,4,5,6]
a.extend("code")
a
[2, 3, 4, 5, 6, 'c', 'o', 'd', 'e']
#swapping of two variables
a = 10
b = 20
c = temp
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    c = temp
NameError: name 'temp' is not defined
a = 10
b = 20
c = a
del c
c = b
b = a
a
10
b
10




a = 10
b = 20
c = b
b = a
a = b
a
10
b
10





a = 10
b = 20
c = b
b = a
a = c
a
20
b
10



