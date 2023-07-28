print("******Opening calculator*****")
name=input("what is your name")
print("Hey"+ name)# here + concatenates(joining two strings(hey gets concatinated with name)) two strings but adds integers 
print("I am capable of doing calcualtions as per your request")
a=input("enter your number")
b=input("Enter another number")
# \"" This is an escape sequence character used
# to display "" in output 
# there are other charcters as well such as /n for new line /b for break etc
operator=input('''Enter operators\"+,-,*,/\"''')
# == is used for comparsion its a comparison operator
if (operator=="+"):
 # variables a and b are in string type we need to change it into integer in order to perform operations
 # for that int()is used  
 print("the sum of two numbers is",int(a)+int(b))    
if (operator=="-"):
 print("the difference of two numbers is",int(a)-int(b))    
elif (operator=="*"):
 print("the product of two numbers is",int(a)*int(b))    
elif (operator=="/"):
 print("the quotient of two numbers is",int(a)/int(b))    
# unknown about using ":" and giving space before print
# error found if not done so
print("Thank you for using me ") 
