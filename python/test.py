pardhu@pardhu-VirtualBox:~$ python3
Python 3.11.4 (main, Jun  9 2023, 07:59:55) [GCC 12.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> rollno = [45,46,47]
>>> my_neighbours = ["ved varshith","pardhu","vamsi"]
>>> print(len(my_neighbours))
3
>>> print(my_neighbours[1:])
['pardhu', 'vamsi']
>>> print(my_neighbours[:1])
['ved varshith']
>>> my_neighbours[3]="roopak"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> my_neighbours[3] = "roopak"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
>>> my_neighbours.append("Roopak")
>>> print(my_neighbours)
['ved varshith', 'pardhu', 'vamsi', 'Roopak']
>>> my_neighbours.insert(0,"navarang")
>>> print(my_neighbours)
['navarang', 'ved varshith', 'pardhu', 'vamsi', 'Roopak']
>>> #removing
>>> my_neighbours.pop(0)
'navarang'
>>> my_neighbours.remove("roopak")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> my_neighbours.remove("Roopak")
>>> print(my_neighbours)
['ved varshith', 'pardhu', 'vamsi']
>>> my_neighbours.sort() #ascending
>>> print(my_neighbours)
['pardhu', 'vamsi', 'ved varshith']
>>> my_neighbours.sort(reverse = true ) #descending
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> my_neighbours.sort(reverse = True ) #descending
>>> my_neighbours.sort(reverse = 3 ) #descending
>>> print(my_neighbours)
['ved varshith', 'vamsi', 'pardhu']
>>> my_neighbours.sort(reverse = True ) #descending
>>> print(my_neighbours)
['ved varshith', 'vamsi', 'pardhu']
>>> my_neighbours.sort(reverse) #descending
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'reverse' is not defined. Did you mean: 'reversed'?
>>> my_neighbours.sort(reversed) #descending
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: sort() takes no positional arguments
>>> my_neighbours.sort(reverse = True ) #descending
