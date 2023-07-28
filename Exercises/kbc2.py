# name=input("Enter yout name: ").title()
# print("Hlo",name,'Welcome to KBC.Lets get started')
q=["Who is known as father of computer?",
   "What do you mean by ENIAC?",
   "How many members are there in parliament?",
   "Who was the person to step on moon?",
   "What is the full form of IBM?"]
v="Charles Babbage"
x="Electronic Numerator Integrator And Calculator"
def check(ans):
 if ans=="Charles Babbage":
  print("congratulations,you are right\nYou have won 10000") 
 elif ans=="Electronic Numerator Integrator And Calculator":
  print("congratulations,you are right\nYou have won 15000")
 elif ans== "601":
        print("congratulations,you are right\nYou have won 50000")
 elif ans == "Neil Armstrong":
        print("congratulations,you are right\nYou have won 100000")
 elif ans == "International Business Machine":
        print("congratulations,you are right\nYou have won 150000")
 else:
    print("wrong")
 print(q[0])
 answer=input("Enter your answer: ").title()
 check(answer)
 print(q[1])
 s=input("Enter your answer: ").title()
 check(s)
 print(q[2])
 d=input("Enter your answer: ")
 check(d)
 print(q[3])
 e=input("Enter your answer: ").title()
 check(d)
 print(q[4])
 f=input("Enter your answer: ").title()
 check(d)
