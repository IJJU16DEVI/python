Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

#len
a="i love python"
len(a)
13
b="python programming"
len(b)
18
a="twinkle twinkle little star"
a.count(a)
1
a.count(1)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.count(1)
TypeError: count() argument 1 must be str, not int
a.count("1")
0
a.count("l")
4
a.count("n")
2
#find a string
a="python"
a.find("n")
5
a.find("u")
-1
b="saiii"
b.find("i")
2
#escape sequences
#newline
#tabspace
a="name\nnmailid\tmobileno\ncollege\tbranch"
print(a)
name
nmailid	mobileno
college	branch
a="name:devi\nmail id:devisamatham@.com\ncollege:gnr
SyntaxError: unterminated string literal (detected at line 1)
a="name:devi\nmailid:devi@.com\ncollege:gnr
SyntaxError: unterminated string literal (detected at line 1)
a="name:devi\nmail:devisamatham@.com\nmobile:7893554672"
a
'name:devi\nmail:devisamatham@.com\nmobile:7893554672'
print(a)
name:devi
mail:devisamatham@.com
mobile:7893554672
#replace()
a="i love codegnan"
a.replace("love","like")
'i like codegnan'
b="i love rajam"
b.replce("rajam","vijayawada")
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    b.replce("rajam","vijayawada")
AttributeError: 'str' object has no attribute 'replce'. Did you mean: 'replace'?
b.replace("rajam","vijayawada")
'i love vijayawada'
#upper()
a="hello"
a.upper()
'HELLO'
b="python"
b.upper()
'PYTHON'
#lower()
a="HELLO"
a.lower()
'hello'
#starts with
#starts with
c="java"
c.upper("j")
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c.upper("j")
TypeError: str.upper() takes no arguments (1 given)
c="java"
c[j].upper()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c[j].upper()
NameError: name 'j' is not defined
c[0].upper()
'J'
c.capitalize()
'Java'
e="devi samatham"
e.title()
'Devi Samatham'
a="python"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
a="samtham@143"
a.isalnum()
False
a.startswith("s")
True
a.endswith(3)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    a.endswith(3)
TypeError: endswith first arg must be str or a tuple of str, not int
c="samatham"
a.startswith("s")
True
a.endswith("m")
False
#strip()
a="samatham"
a.strip()
'samatham'
a.isstrip()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    a.isstrip()
AttributeError: 'str' object has no attribute 'isstrip'. Did you mean: 'lstrip'?
a="    devi   "
a.lstrip()
'devi   '
a.rstrip()
'    devi'
#split
a=["python","jaba","c++")
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
a=["python","java","c++"]
a=["python java c++"]
a.split()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.split()
AttributeError: 'list' object has no attribute 'split'
a=(python java c++)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=("python java c++")
a.split()
['python', 'java', 'c++']
#join
a=("python","java","c++")
" "join(a)
SyntaxError: invalid syntax
" ".join(a)
'python java c++'
#concatination
a="code"
b="python"
print(a+b)
codepython
>>> print(a+" "+b)
code python
>>> fname="devi"
>>> lname="samatham"
>>> print(("fname+lname").title())
Fname+Lname
>>> print(fname+lname)
devisamatham
>>> print(fname+ "  "+lname)
devi  samatham
>>> print(fname.title()+lname.title())
DeviSamatham
>>> print(fname.title()+" "+lname.title())
Devi Samatham
>>> #formatting
>>> a="motu"
>>> b="pathulu"
>>> print("hello {} {}".format(a,b))
hello motu pathulu
>>> #fstrings
>>> a="devi"
>>> b="samtham"
>>> print(f"hello {a}{b}")
hello devisamtham
>>> print(f"hello {a} hello{b}")
hello devi hellosamtham
>>> print(f"hello  {a} hello {b}")
hello  devi hello samtham
