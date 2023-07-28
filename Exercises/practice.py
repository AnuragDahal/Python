name=input("Enter your name: ")
current_time=input("ENter your time")
print(current_time)#returns string
hour=int(current_time)#converting into integer in order to perform operations
if(4<=hour<12):
    print("Good Morning",name)
elif(12<=hour<17):
    print("Good Afternoon",name)
elif(17<=hour<21):
    print("Good Evening",name)
else:
    print("Good Night",name)
