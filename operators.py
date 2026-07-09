Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#ARTHEMETIC OPERATORS
a=2
b=6
print(a+b)
8
print(a_b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    print(a_b)
NameError: name 'a_b' is not defined
print(a-b)
-4
print(a*b)
12
print(a**)
SyntaxError: invalid syntax
print(a**b)
64
print(a%b)
2
print(a//b)
0
print(a/b)
0.3333333333333333
#comparision operators
a=4
b=6
a+=b
b
6
b-=a
b
-4
b*=a
b
-40
b*=6
b
-240
b%=a
b
0
b%=2
b
0
b**=a
b
0
b**=4
b
0
b**=5
b
0
b|=a
b
10
b|=6
b
14
#comparision opearators
a=9
b=10
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
a==b
False
a=8
b=8
a!=b
False
a==b
True
#LOGICAL OPEARTORS
a=7
b=8
a<b and a>b
False
a<=b and a>=b
False
a!=b and a==b
False
a!=b or a==b
True
not true
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    not true
NameError: name 'true' is not defined. Did you mean: 'True'?
not True
False
not False
True
#IDENTIFY OPERATORS
a=6
type(a) is int
True
type(a)is not int
False
a=7.8
type(a) is float
True
type(a)is not float
False
b="deviii"
type(b)is string
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    type(b)is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
b="devii"
type (b) is str
True
type(b) is not str
False
c=a+9j
type (c) is complex
True
type (c) is not complex
False
d=true
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    d=true
NameError: name 'true' is not defined. Did you mean: 'True'?
d=False
type(d) is bool
True
type (d) is not bool
False
#MEMBERSHIP OPERATORS
a=9,7,5,4,3,4,6
9 in a
True
10 in a
False
10 not in a
True
7 not in a
False
#BITWISE OPERATORS

a=4
b=6
a&b
4
bin(4)
'0b100'
bin(6)
'0b110'
a=8
b=9
bin(8)
'0b1000'
bin(9)
'0b1001'
a&b
8
a=3
b=8
a&b
0
bin(3)
'0b11'
bin(8)
'0b1000'
a=2
b=6
a|b
6
b=8
c=9
b&c
8
>>> a=7
>>> -(a+1)
-8
>>> b=34
>>> ~b
-35
>>> c=-8
>>> ~c
7
>>> a=6
>>> b=7
>>> a^b
1
>>> a=8
>>> b=10
>>> a^b
2
>>> 
>>> a=10
>>> a>>2
2
>>> a=9
>>> a>>3
1
>>> a=9
>>> a<<2
36
