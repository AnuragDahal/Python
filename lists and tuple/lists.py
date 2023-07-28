l=[5,6,3,"Anurag",False]
print(l)
print(l[0],l[3])#Alike of index ins strings
# 0 means first subject in list i.e5 and so on
'''same as slicing in strings'''
print(l[:4])
'''Negative slicing'''
print(l[0:len(l)-1])
print(l[:-1])
print(l[0:4])
print(l[1:5:2])#2 is jump index 
# examples of jump index
names=["Ram","shyam","Hari","Sita","Gita","Pujan","Sujan"]
print(names[0:7:3])

# List Comprehension
# they are used for creating new lists from other iterables like lists,
# tuples,dictionaries,sets and even in arrays and strings.
num=[a for a in range(5)]
print(num)
# condition can also be applied
num1=[i for i in range(40)if i%3==0]
print(num1)
