Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #TUPLE
>>> a=(8,9.7,"python",8+9j,True,False)
>>> print(a)
(8, 9.7, 'python', (8+9j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.index(8+9j)
3
>>> len(a)
6
>>> a.count(True)
1
