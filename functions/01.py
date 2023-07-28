# functions are of two types 
# user defined and built in 
# print,sum,range,int,input,type,pass,etc are built in functions
# user defined
def Simplify(a,b,c):
    result=(a*b*c)/(a+b+c)
    print(result)
d=12
e=3
f=1
Simplify(d,e,f)
def Subtract(x,y):
    if(x>=y):
        output=x-y
        print(output)
    else:
        output=y-x
        print(output) 
f=40
g=100
Subtract(f,g)      