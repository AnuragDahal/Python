# def f(n):
#     if f(n)==0:
#      return 0
#     elif f(n)==1:
#      return 1
#     else:
#      n=f(n-1)+f(n-2)
#     print(n)
# v=int(input("Enter any number: "))
# f(v)
a= int(input("Enter any number : "))

def fibonacci(n):
    if (n == 1 or n == 0):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(a))
 