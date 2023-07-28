# Which number is greater take user input
def analyze(a,b,c):
    if a>b and a>c:
        print(a,"is greater")
    elif b>a and b>c:
        print(b,"is greater")
    elif a==b==c:
        print("None is greater")
    else:
        print(c,"is greater")
f=int(input("Enter first number: "))            
g=int(input("Enter second number: "))            
x=int(input("Enter third number: "))            
analyze(f,g,x)
def lesser(q,w,e):
    pass
# pass is used when we just want to create a function name and write its body later
# it doesn't affect other codes 
# if pass is not used throws an error
