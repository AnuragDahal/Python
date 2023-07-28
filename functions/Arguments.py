'''There are four types of arguments
default arguments,required arguments,keyword arguments,variable length arguments
'''
# default arguments gives default value even if the value is not given 
def add(a=6,b=7):
    value=a+b
    print(value)
add()
'''keyword arguments
can provide arguments with key=value'''
add(a=10)#b value remains same 
add(b=0,a=23)#order doesnt matter b value replaced by 0 and a by 23
f=1
g=12
add(f,g)#both values are changed
add(g)#default value of a is replaced by g but b value remains same
'''Required arguments
here we cannot the skip the value we need to enter on our own'''
def subtract(p,o):
    diff=p-o
    print(diff)
subtract(p=10,o=9)#both values should be given 
'''Variable length arguments
Sometimes we need to pass more arguments than the defined one'''
# Arbitary Arguments
def average(*numbers):# *numbers gives us a tuple of numbers.
    avg=0
    for i in numbers:
        avg=avg+i
        print("Average is",avg/len(numbers))
#keyword arbitary arguments
def name(**name):#**name gives us a dictionary
    print('hello',name["fname"],name["mname"],name["lname"])
name(fname="Anurag",lname="Dahal",mname="")
