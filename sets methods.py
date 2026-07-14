Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#SETS{}
a={4,7.8,"devi",5+9j,True,False}
print(a)
{False, True, (5+9j), 4, 7.8, 'devi'}
type(a)
<class 'set'>
b={7,8,4,5,3,5,}
print(b)
{3, 4, 5, 7, 8}
#ADD()
a={4,5,6,7,8,9}
a.add(15)
print(a)
{4, 5, 6, 7, 8, 9, 15}
#ISSUBSET()
a={3,4,6,78,9,8,6}
b={5,6,7,8}
a.issubset(b)
False
b.issubset(a)
False
#superset()
a={5,6,7,8,9}
b={1,2,3}
a.isuperset(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a.isuperset(b)
AttributeError: 'set' object has no attribute 'isuperset'. Did you mean: 'issuperset'?
a.issuperset(b)
False
b.issuperset(a)
False
#UNION()
a={1,2,3,3,}
b{6,7,8,9}
SyntaxError: invalid syntax
b={6,7,9}
a.union(b)
{1, 2, 3, 6, 7, 9}
#INTERSECTION
a={2,3,4,5,6,7,}
b={2,4,6,7,8}
a.intersection(b)
{2, 4, 6, 7}
#DIFFERENCE
a={7,8,9,4,5,6}
b={9,8,5,7,4,3}
a.differnece(b)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a.differnece(b)
AttributeError: 'set' object has no attribute 'differnece'. Did you mean: 'difference'?
a.difference(b)
{6}
b.difference(a)
{3}
#update
a={2,3,4,5,6,7}
b={9,7,6,5,4,}
a.update(b)
a
{2, 3, 4, 5, 6, 7, 9}
b.update(a)
b
{2, 3, 4, 5, 6, 7, 9}
b
{2, 3, 4, 5, 6, 7, 9}
#SYMMETRIC DIFFERENCE
a={2,3,4,5,6,9}
b={4,2,3,1,7,8,9}
a.symmetric_difference(b)
{1, 5, 6, 7, 8}
#difference_update()
a={5,7,8,9,6,4}
b={6,7,8,4,3}
a.difference_update(b)
a
{5, 9}
b.difference_update(a)
b
{3, 4, 6, 7, 8}
#INTERSECTION_UPDATE
a.intersection_update(b)
a
set()
a={1,3,4,5,5,8}
b={8,9,6,4,3,2}
a.intersection_update(b)
a
{8, 3, 4}
b.intersection_update(a)
b
{8, 3, 4}
a=
SyntaxError: invalid syntax
a={11,12,13,14,15}
b={13,14,15,16}
a.symmetric_difference_update(a)
a
set()
a
set()
a.symmetric_difference_update(b)
a
{16, 13, 14, 15}
#pop
a={3,4,5,6}
a.pop()
3
a
{4, 5, 6}
a.pop(2)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a.pop(2)
TypeError: set.pop() takes no arguments (1 given)
a.remove(6)
a
{4, 5}
#COPY
a={1,2,34,5,6}
a.copy()
{1, 2, 34, 5, 6}
b=a.copy()
b
{1, 2, 34, 5, 6}
a.discard(34)
b
{1, 2, 34, 5, 6}
a
{1, 2, 5, 6}
a.clear()
a
set()
>>> b.add(100)
>>> b
{1, 2, 34, 100, 5, 6}
>>> b
{1, 2, 34, 100, 5, 6}
>>> b=set()
>>> b.add(100)
>>> b
{100}
>>> #isdisjoint
>>> a={1,23,4,56}
>>> b={1,4,5,8}
>>> a.isdisjoint(b)
False
>>> c={10,20,30,40}
>>> d={20,3060,70}
>>> c.isdisjoint(d)
False
>>> c={10,2,30}
>>> d={40,50,60}
>>> c.disjoint(d)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    c.disjoint(d)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> c.isdisjoint(b)
True
