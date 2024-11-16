Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('hello')
hello
print("hello")
hello
a="hello"
print(a.index('h'))
0
print
<built-in function print>
print(a.index('1'))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(a.index('1'))
ValueError: substring not found
print(a.index('1'))
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a.index('1'))
ValueError: substring not found
print(len(a))
5
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
print(a.startswith('h'))
True
print(a.startswith('m'))
False
print(b.endswith('d'))
True
print(b.endswith('w'))
False
print(s.isupper())
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    print(s.isupper())
NameError: name 's' is not defined
print(a.isupper())
False
print(a.islower())
True
print(a+b.swapcase())
helloWORLD
print(a.swapcase())
HELLO
print(b.swapcase())
WORLD
name="lucky"
print(name[:3])
luc
print(name[3:])
ky
name2="python programming language"
name(name2.split(" "))
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    name(name2.split(" "))
TypeError: 'str' object is not callable
print(name2.split(' '))
['python', 'programming', 'language']
s="good"
print(s.replace('g','h'))
hood
m="this is python lab"
print(m.replace('is','was))
                
SyntaxError: incomplete input
>>> print(m.replace('is','was')
... print(m.replace('is','was'))
...       
SyntaxError: '(' was never closed
>>> print(m.replace('is','was'))
...       
thwas was python lab
>>> name="akshaya"
...       
>>> print(name.upper())
...       
AKSHAYA
>>> name="JESUS"
...       
>>> print(name.lower())
...       
jesus
>>> name="JESUS"
...       
>>> m="good afternoon"
...       
>>> print(m.capitalize())
...       
Good afternoon
>>> print(m.count('o'))
...       
4
>>> p[rint(m.find('a'))
... 
...   print(m.find('a'))
...   
SyntaxError: '[' was never closed
>>> print(m.find('a'))
...   
5
