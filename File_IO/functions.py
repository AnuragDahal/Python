# seek()and tell() functions are used to work with the file object and their position.
# seek():-allows you to move the current postion within a file to a specific point. 
f=open("myfile.txt",'r')
# Move to the 7th byte
f.seek(7)
text=f.read(5)#Read the next 5 byte.
print(text)
# tell():-returns the current postion within a file in bytes.
print(f.tell())

# truncate():-Allow you to modify the file size irrespective of the content.
f=open("myfile.txt",'w')
f.write("Anurag Dahal")
f.truncate(7)
f.close()