#Opening a file.
# python provides open() function for opening a file which takes two arguments
# The name of file and the mode in which the file is to be opened.
f=open("myfile.txt",'r')
print(f)
# # reading a file
text=f.read()
print(text)
f.close()
# Modes in file(read"r",write"w",append"a")
# read()
"""allows to read content in a file but throws an error if the file doesn't exist."""
#Writing a file
# write()
'''allows to write on/over a file and creates it if the file doesn't exist.'''
a=open("myfiles2.txt",'w')
text=a.write("Hello World")#THe text written here gets printed on myfiles2.txt which is the assinged file in this case 
a.close()#its necessary to close a file after performing actions on it

# # Append to a file
'''allows you to add content at the end of a file'''
a=open('myfile.txt','a')#append mode
a.write("HEY I am a cool guy.")
a.close()

# With statement-automatically closes the file after you are done with it.
with open('myfiles2.txt','a') as j:
 j.write("Good morning")
