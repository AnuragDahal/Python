# import is a process of loading codes from a Python module into the current script.
# ONnce a module is imported you can use the functions and variables defined in it using a dot notation
# for eg.
import math
value=math.sqrt(100)
print(value)

# from keyword
# specific functions or variables can be imported from a module using "from" keyword.
from math import sqrt
a=sqrt(144)
print(a) 

# multiple functions and variables can be imported at once by separating them with commas.
from math import sqrt, pi
result=sqrt(9)*pi
print(result)

# Importing everything
# We can also import all functions and variables using"*" wildcard
# However it is not recommended as it makes things complicated and creates confusion from where specific functions and variables are coming from.

from math import *
result=sqrt(169)
print(result)
print(pi)

# "as"keyword
# It is used to rename modules or functions in a module for convinience
from math import sqrt as s
d=s(4)#instead of sqrt I can write s()
print(d)

import math as m#instead of math.sqrt I can write m.sqrt
f=m.sqrt(1000)
print(f)

'''dir function
It is used to view all the functions and variables defined in a module.'''
import math
print(dir(math))
 