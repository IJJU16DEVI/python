Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#int
int(4)
4
int(9.8)
9
int("hiii")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hiii")
ValueError: invalid literal for int() with base 10: 'hiii'
int(5+7j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(5+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
#float
float(7)
7.0
float(6.8)
6.8
float("hello")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    float("hello")
ValueError: could not convert string to float: 'hello'
float(5+7j)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float(5+7j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
flaot(False)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    flaot(False)
NameError: name 'flaot' is not defined. Did you mean: 'float'?
float(False)
0.0
#str()
str(5)
'5'
str(8.9)
'8.9'
str(6+9j)
'(6+9j)'
str(True)
'True'
str(False)
'False'
#complex
>>> complex(4)
(4+0j)
>>> complex(7.8)
(7.8+0j)
>>> complex("devi")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    complex("devi")
ValueError: complex() arg is a malformed string
>>> complex(7+8j)
(7+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #boolean
>>> bool(8)
True
>>> bool(9.8)
True
>>> bool("hello")
True
>>> bool(5+8j)
True
>>> bool(True)
True
>>> bool(False)
False
