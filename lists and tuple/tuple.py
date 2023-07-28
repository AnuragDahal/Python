'''Tuples are ordered collection of 
data items enclosed by round brackets and separated by commas
#if u r making a tuple of one value use comma else it will be shown as int'''
ans=(1,)#tuples are unchangeable
print(type(ans))
rar=(1,2,True,"red")
print (rar[0])
print(rar[3])
# tuple slicing 
# new tuple is returned after slicing original doesn't get changed
tup=rar[1:3]
print(tup)
tup1=rar[:-1]#negative slicing same as in list
print(tup1)
if "red" in rar:
    print("yes it is here")