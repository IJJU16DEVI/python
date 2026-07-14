Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#LIST[]
a=[2,4.5,"python",6+9j,True,False]
print(a)
[2, 4.5, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=8.7
type(b)
<class 'float'>
b=9.7
b=[9.7]
type(b)
<class 'list'>
a=["python","c","c++"]
a.append("java")
a
['python', 'c', 'c++', 'java']

a.append("html","css")
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.append("html","css")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["html","css"])
a
['python', 'c', 'c++', 'java', ['html', 'css']]
#INSERT
a=["python","html","css","java"]
a.insert("c++")
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.insert("c++")
TypeError: insert expected 2 arguments, got 1
a.insert(1,"chennai")
a
['python', 'chennai', 'html', 'css', 'java']
#EXTEND
a=["html","css","java"]
a.extend(["python","c++"])
a
['html', 'css', 'java', 'python', 'c++']
#index
a=["apple","banana","grapes"]
a.index("grapes")
2
a.copy()
['apple', 'banana', 'grapes']
b=a.copy()
b
['apple', 'banana', 'grapes']
a.count("apple")
1
len(a)
3
d="apple"
len(d)
5
len(e)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    len(e)
NameError: name 'e' is not defined
e="apple"
len(e)
5
a=["mango","apple","banana","orange"]
a.sort()
a
['apple', 'banana', 'mango', 'orange']
b=[0,6,7,8,5,4,6,7]
b.sort()
b
[0, 4, 5, 6, 6, 7, 7, 8]
a=["ds","kl","ms"]
a.reverse()
a
['ms', 'kl', 'ds']
b=["23","43","89"]
>>> b.reverse()
>>> b
['89', '43', '23']
>>> a=["black","blue","orange"]
>>> a.pop()
'orange'
>>> a
['black', 'blue']
>>> a.pop(2)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.pop(2)
IndexError: pop index out of range
>>> a.pop(1)
'blue'
>>> a
['black']
>>> a.remove("black")
>>> a
[]
>>> a=["ap","ts","ka"]
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("java")
>>> b
['java']
