Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
hobbies={1:"coding",2:"reading",3:"singing",4:"cooking"}
print(hobbies)
{1: 'coding', 2: 'reading', 3: 'singing', 4: 'cooking'}
hobbies
{1: 'coding', 2: 'reading', 3: 'singing', 4: 'cooking'}
best_hero={1:"surya",2:"allu arjun",3:"prabhas"}
best_hero
{1: 'surya', 2: 'allu arjun', 3: 'prabhas'}
fav_teachers={'name':'sana mam',2009:['2yr 1sem']}
fav_teachers
{'name': 'sana mam', 2009: ['2yr 1sem']}
best_stud={'cseviib':'ganesh','CSEVIIB':'arjun'}
best_stud
{'cseviib': 'ganesh', 'CSEVIIB': 'arjun'}
best_stud['cseviib']
'ganesh'
best_stud['CSEVIIB']
'arjun'
best_stud[0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    best_stud[0]
KeyError: 0
sports={}
print(sports)
{}
print("empty dictionary",sports)
empty dictionary {}
students=dict({1:'surya',2:'prabhas',3:'prashanth'})
print("dictionary using dict():")
dictionary using dict():
print(students)
{1: 'surya', 2: 'prabhas', 3: 'prashanth'}
hero=dict([151,"sandeep"),(106,"prabhu")])
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
hero=dict([(151,"sandeep"),(106,"prabhu")])
print(hero)
{151: 'sandeep', 106: 'prabhu'}
pplab={"sec":"aidsb",
       "labno":10,
       "batch1":{"day":"saturday","rnorange":"57-89"},
       "batch2":{"day":"thursday","rnorange":"90-313"}}
print(pplab)
{'sec': 'aidsb', 'labno': 10, 'batch1': {'day': 'saturday', 'rnorange': '57-89'}, 'batch2': {'day': 'thursday', 'rnorange': '90-313'}}
pplab["sec"]
'aidsb'
pplab["labno"]
10
pplab["batch2"]
{'day': 'thursday', 'rnorange': '90-313'}
pplab["batch1"]
{'day': 'saturday', 'rnorange': '57-89'}
aim={}
print(aim)
{}
aim[1]="musician"
aim[2]="software"
aim[3]="business"
aim[4]="masters"
aim
{1: 'musician', 2: 'software', 3: 'business', 4: 'masters'}
aim.get(1)
'musician'
del(aim[3])
aim
{1: 'musician', 2: 'software', 4: 'masters'}
del(pplab['batch1']['rnorange'])
pplab
{'sec': 'aidsb', 'labno': 10, 'batch1': {'day': 'saturday'}, 'batch2': {'day': 'thursday', 'rnorange': '90-313'}}
>>> pplab.clear()
>>> pplab
{}
>>> expaim=aim.copy()
>>> expaim
{1: 'musician', 2: 'software', 4: 'masters'}
>>> aim.update({1:"guitarist"})
>>> aim
{1: 'guitarist', 2: 'software', 4: 'masters'}
>>> gaim={1:"musician"}
>>> aim.update(gaim)
>>> aim
{1: 'musician', 2: 'software', 4: 'masters'}
>>> aim.update(gaim)
>>> aim
{1: 'musician', 2: 'software', 4: 'masters'}
>>> gaim={"first":"musician"}
>>> aim.update(gaim)
>>> aim
{1: 'musician', 2: 'software', 4: 'masters', 'first': 'musician'}
>>> aim.items()
dict_items([(1, 'musician'), (2, 'software'), (4, 'masters'), ('first', 'musician')])
>>> aim.values()
dict_values(['musician', 'software', 'masters', 'musician'])
>>> aim.pop(2)
'software'
>>> aim
{1: 'musician', 4: 'masters', 'first': 'musician'}
>>> aim.keys()
dict_keys([1, 4, 'first'])
>>> aim.popitem()
('first', 'musician')
>>> aim
{1: 'musician', 4: 'masters'}
