# lambda is used to create anonymous function
# It's often used in situation where a small function is required for a short period of time.
# Syntax
# lambda argument:expression
square= lambda x: x*x 
print(square(4))
# or
def sq(a):
 return a*a 
sq(4)
# lambda also takes multiple arguments.
avg= lambda x, y, z:(x + y + z)/3
print(avg(4,5,6))
# Function can also be passed as an argument on other function.
def fn(fx,a):
 return fx(a)+ 8
print(fn(square,6))
print(fn(lambda x: x*x,6))