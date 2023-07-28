def greet():
   print ("Namaste my friend")
# greet() for the lower explanation to occur this line needs to be executed and code below definition needs to be commented.

   """By doing this whenever this module is imported it gets executed on 
its own without even calling its functions.It may be a problem whilw writing complex coding that the module is
executed on its own on just importing it"""

# SO to avoid it we use"if__name__=="__main__"
#It is a idiom and it's a common pattern to determine whether the script is being run directly or being imported.
# IF its run directly then its executed but if its imported it doesn't.

if __name__== "__main__":
   greet()
