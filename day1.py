Python 3.10.11 (tags/v3.10.11:7d4cc5a, Apr  5 2023, 00:38:17) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello.............")
Hello.............
A = 10
a= 20
A
10
a
20
type(A)
<class 'int'>
a = "akhil"
a
'akhil'
type(a)
<class 'str'>
a =1.5
type(a)
<class 'float'>
List1 = [1,2,3,4]
List
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    List
NameError: name 'List' is not defined. Did you mean: 'List1'?
List1
[1, 2, 3, 4]
type(List[0])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type(List[0])
NameError: name 'List' is not defined. Did you mean: 'List1'?
type(List1[0])
<class 'int'>
List = ['a',1,2,4]
type(List[0])
<class 'str'>
List[1]
1
type(List[0])
<class 'str'>
type(List[1])
<class 'int'>
List = ['a',1,2,4,[2,3,4]]
List[4][2]
4
List[4]
[2, 3, 4]
dic = {1:"akhil",2:"test"}
dic[1]
'akhil'
age = input()
123
type(age)
<class 'str'>
age = int(input())
2345
type(age)
<class 'int'>
age = int(input())
"akhil"
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    age = int(input())
ValueError: invalid literal for int() with base 10: '"akhil"'
age = int(input())
A
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    age = int(input())
ValueError: invalid literal for int() with base 10: 'A'
test = "A"
int(test)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    int(test)
ValueError: invalid literal for int() with base 10: 'A'
List = list(map(int, input().split()))
1 2 3 4 5
List
[1, 2, 3, 4, 5]
y=input()
1 2 3 4 5
y
'1 2 3 4 5'
y.split()
['1', '2', '3', '4', '5']
y=input()
1-2-3-4-5
y
'1-2-3-4-5'
y.split('-')
['1', '2', '3', '4', '5']
map(int, y.split()))
SyntaxError: unmatched ')'
map(int, y.split())
<map object at 0x00000209F1F8DFF0>
x = list(1,2,3)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x = list(1,2,3)
TypeError: list expected at most 1 argument, got 3
print("This is a value", A)
This is a value 10

======================================= RESTART: C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py ======================================
Python is awesome
a is 10
0

======================================= RESTART: C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py ======================================
Python is awesome
Traceback (most recent call last):
  File "C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py", line 9, in <module>
    myfunc()
  File "C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py", line 5, in myfunc
    print("a is",a)
UnboundLocalError: local variable 'a' referenced before assignment

======================================= RESTART: C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py ======================================
Python is awesome
Traceback (most recent call last):
  File "C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py", line 9, in <module>
    myfunc()
  File "C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py", line 5, in myfunc
    print("a is",a)
UnboundLocalError: local variable 'a' referenced before assignment

======================================= RESTART: C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py ======================================
Python is awesome
Traceback (most recent call last):
  File "C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py", line 9, in <module>
    myfunc()
  File "C:/Users/aakhilsa/AppData/Local/Programs/Python/Python310/test.py", line 5, in myfunc
    print("a is",a)
UnboundLocalError: local variable 'a' referenced before assignment
a=[1,2,3]
a
[1, 2, 3]
a[1] = "123"
a
[1, '123', 3]
tup = (1,2,3)
tup
(1, 2, 3)
tup[1]
2
tup[1]="123"
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    tup[1]="123"
TypeError: 'tuple' object does not support item assignment
range(1,10)
range(1, 10)
x = range(1, 10)
x
range(1, 10)
x = range(6)
x
range(0, 6)
for i in x:
    print(i)

    
0
1
2
3
4
5
range(2, 6)
for i in range(2, 6):
    print(i)
    
SyntaxError: multiple statements found while compiling a single statement
for i in range(2, 6):
    print(i)

    
2
3
4
5
for i in range(1,10,2):
    print(i)

    
1
3
5
7
9
for i in range(1,10):
    print(i)

    
1
2
3
4
5
6
7
8
9
for i in range(0,10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(0,10,1):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
for i in range(0,10,2):
    print(i)

    
0
2
4
6
8
for i in range(0,10,3):
    print(i)

    
0
3
6
9
set1 = {1,1,2,3,4,4,5,5}
st1
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    st1
NameError: name 'st1' is not defined. Did you mean: 'set1'?
set1
{1, 2, 3, 4, 5}
set1 = {10,12,22,3,4,4,5,5}
set1
{3, 4, 5, 22, 10, 12}
True
True
False
False
true
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    true
NameError: name 'true' is not defined. Did you mean: 'True'?
x = b"Hello"
x
b'Hello'
'
type(x)
<class 'bytes'>
x = bytearray(5)
>>> x
bytearray(b'\x00\x00\x00\x00\x00')
>>> x = None
>>> x
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> str1 = "Priya   Dhanalakota"
>>> for i in str1:
...     print(i)
... 
...     
P
r
i
y
a
 
 
 
D
h
a
n
a
l
a
k
o
t
a
list1 = [1,2,3,4,5,6]
for i in list1:
    print(i)

    
1
2
3
4
5
6
list1 = [1,2,3,4,5,'akhil']
for i in list1:
    print(i)

    
1
2
3
4
5
akhil
for i in range(6):
    print(i)

    
0
1
2
3
4
5
for i in range(0,4):
    print(i)

    
0
1
2
3
for i in range(0,6,2):
    print(i)

    
0
2
4
