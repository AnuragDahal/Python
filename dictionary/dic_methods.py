# There are some methods with which we can do changes in dictionary.
# 1.update()
id1={
    122:78,
    111:89,
    345:90}
id2={001:50,223:95,550:85}
id1.update(id2)
print(id1)
# 2.clear()
# removes all the elements of dic
id2.clear()
# pop()
c=id1.pop()
print(c)
# del
# used to delete an entire dictionary or a key if assigned
del id1[111]#deletes 111 key and its value from id1
print(id1)
del id1
'''there are other methods to check it from dictionary documentation in google
'''
