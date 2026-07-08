Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #int
>>> int(4)
4
>>> int(9.8)
9
>>> int("hiii")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("hiii")
ValueError: invalid literal for int() with base 10: 'hiii'
>>> int(5+7j)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(5+7j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> int(True)
1
>>> int(False)
0
