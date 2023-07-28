# UNion,Intersection,Disjoint are types of set
#joining sets
a={"anurag","swikriti","anukriti","ram"}
b={"anurag","Hari","sita","ram"}
c=a.union(b)
print(c)
# #union function returns new set by combining given sets
b.update(a)
print(b)
#Intersection and intersection_update
d=a.intersection(b)
print(d)
a.intersection_update(b)
print(a)
# symmetric_difference and symmetric_difference_update
a1=a.symmetric_difference(b)
#prints value which are not common in both sets
print(a1)
a.symmetric_difference_update(b)
print(a,b)
# difference and difference_update
s=a.difference(b)
# print only elements that are in a not in b
print(s)
print(a)
a.difference_update(b)
print(a)
# isdisjoint()
print(a.isdisjoint(b))
# issuperset()
print(a.issuperset(b))
# issubset
print(b.issubset(c))
#add()
l={0,2,3}
l.add(5)
print(l)
# update()
f={1,9,5}
l.update(f)
print(l)
# remove/discard
l.remove(2)
print(l)
l.discard(5)
print(l)
# pop
j=l.pop()#remove a random element from set
print(j)
# del
m={1,2,3,4,5,5,6,7}
del(m)
# clear()
n={1,9,0,8,6}
n.clear()
print(n)
#in
# # checks if the element is present or not
name={"aiger","micheal","john"}
if "aiger" in name:
 print("present")
else:
 print("absent")
