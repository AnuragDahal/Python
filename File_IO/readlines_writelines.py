#writelines():-writes sequence of string to a file.
# Note it doesn't add new line character on its own
f=open("Bi3o.txt",'w')
lines=['hello\n''my name\n''age\n''dob\n']
f.writelines(lines)
f.close()
#if you want to add new lines between the string you can use a loop to write each string separately.
info=['hello''my name''age''dob']
for line in info:
 f.write(line+'\n')
f.close()
# readline():-reads a single line from a file.
f=open("bi3o.txt",'r')
text=f.readline()
print(text)
# You can read multiple lines with the help of loop.
f=open("Bi3o.txt",'r')
while True:
 line=f.readline()
 print(line,end="")
 if not line:
  break
f.close()

# readlines():-Reads all the lines in a file and returns them in the list of strings.
a=open("Bi3o.txt",'r')
content=a.readlines()
print(content)