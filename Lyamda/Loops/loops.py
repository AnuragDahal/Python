# For loop
name="Anurag"
for i in name:#variable after for and inside print should be same
    # print(i)
# for printing lists
# lists are written in[]
 ranks=["first","second","third","fourth","fifth"]
for rank in ranks:
    print(rank)
    for d in rank:
        print(d)
#range function 
# used for printing numbers between two numbers
# eg.(1,2001) prints from 1 to 2000
for a in range(1,2001):
    print(a)
'''means runs from 5 to 10 with each jump of 2 numbers
i.e 5,7,9 gets printed
its due to step function'''
for f in range(5,10,2):
    print(f)
