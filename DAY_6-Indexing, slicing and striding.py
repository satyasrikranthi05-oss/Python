Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#indexing--> used to access elements in string
a = "I am in class"
a[0]
'I'
a[3]
'm'
a[0]+a[1]+a[2]+a[3]
'I am'
a[8] + a[9] +a[10] + a[11]+a[12]
'class'
a[1]
' '
a[1]+a[4]+a[7]
'   '
a = "Vijayawada is a royal city"
a[15]+a[16]+a[17]+a[18]+a[19]+a[20]
' royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]
'is'
a = "vizag is a city of destiny"
a[-15]+a[-14]+a[-13]+a[-12]
'city'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]
'vizag'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a = "simple is better than complex"
\
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
#Slicing
a = "codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a = "work hard until you succeed"
a[9:15]
' until'
a[10:15]
'until'
a[5:9]
'hard'
a[0:4]
'work'
a[16:19]
'you'
a[22:]
'cceed'
a[21:]
'ucceed'
a[20:]
'succeed'
a = "time is very precious'
SyntaxError: unterminated string literal (detected at line 1)
a = "time is very precious"
a[13:]
'precious'
a[8:12]
'very'
a[0:4]
'time'
a = "I love Python"
a[-11:-8]
'lov'
a[-11:-7]
'love'
a[-6:]
'Python'
a = "Today is weekend"
a[-16:-11]
'Today'
a[-10:-8]
'is'
a[-7:]
'weekend'
#Striding --> start:end:step(increment/decrement
a = "Data Science"
a[::]
'Data Science'
>>> a[::1]
'Data Science'
>>> a[::2]
'Dt cec'
>>> a = "Machine learning"
>>> a[::4]
'Miln'
>>> a[::6]
'Men'
>>> a[::2]
'Mcielann'
>>> a[5:]
'ne learning'
>>> a[:9]
'Machine l'
>>> a[::7]
'M n'
>>> a = "Cloud Computing"
>>> a[1:11:2]
'lu op'
>>> a[2:14:4]
'oCu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dCmu'
>>> #negative striding
>>> a = "Python course"
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
>>> #rules
>>> #in positive striding highest to lowest not possible[start value should be greater than end value]
>>> #in negative striding lowest to highest not possible[start value should be less than greater value]
