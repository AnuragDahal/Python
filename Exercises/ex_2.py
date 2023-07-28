import time 
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hrs=time.strftime('%H')
print(hrs)
mins=time.strftime('%M')
print(mins)
secs=time.strftime('%S')
print(secs)
name=input("Enter your name: ")
hour=int(time.strftime('%H'))
if 4<=hour<12:
 print("Good Morning",name)
elif(12<=hour<17):
 print("Good Afternoon",name)
elif(17<=hour<21):
    print("Good Evening",name)
else:
    print("Goodnight",name)    