# else is executed if the loop completes successfully.
for a in range(10):
 print(a)
else:
    print("loop over")
#When we break a loop else is not executed 
for d in range(6):
    print(d)
    if d==4:
     break
else:
    print("over")
# can be used with while as well
i=1
while i<8:
    i=i+1
    print(i)
    if i==6:
        break
else:
    print("over")