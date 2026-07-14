Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#SLICING
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[:5]
'codeg'
a[5:]
'nan'
a[:]
'codegnan'
a[:9]
'codegnan'
a[0:4]
'code'
a="work until you succed"
a[0:4]
'work'
a[5:10]
'until'
>>> a[15:]
'succed'
>>> b="time is very precious
SyntaxError: unterminated string literal (detected at line 1)
>>> b="time is very precious"
>>> b[13:]
'precious'
>>> b[8:12]
'very'
>>> b[0:4]
'time'
>>> #NEGATIVE SLICING
>>> a="simple is better than complex"
>>> a[-12:-18]
''
>>> a[-19:-13]
'better'
>>> a[-29:-23]
'simple'
>>> a[-7:]
'complex'
>>> a="codegnan it solutions"
>>> a[-9:]
'solutions'
>>> a[-21:-13]
'codegnan'
>>> a[-9:-1]
'solution'
