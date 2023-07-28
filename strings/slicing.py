name="Anurag"
print("n" in name)
# slicing 
print(name[:4])#index starts from 0 in maximum programming lannguages
# [0:4] and [:4] gives same meaning and vice versa
print(name[2:4])#including 2 but not 4 
#bigbrackets for slicing
print("g" in name )#gives output in boolean form
# can find the length of a string using len function
print(len(name))

# negative slicing
print(name[0:-2])
# explantion 
# -2 means len(name)-2 i.e len of name is 6 and
# 6-2 is 4 i.e name([0:4])