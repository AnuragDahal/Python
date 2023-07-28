questions=[
  [  
    "Which is the most easy programming language?",
           "Python","Java","C++","Ruby"
  ],
   [
           "Which is the most easy programming language?",
           "Python","php","C++","Ruby"
   ],
   [
           "Which is the most easy programming language?",
           "Python","Java","SQL","Ruby"
   ],
   [
           "Which is the most easy programming language?",
           "Python","Matlab","C++","Ruby"
   ],
   [
           "Which is the most easy programming language?",
           "Python","Java","C++","swift"
   ],
   [
           "Which is the most easy programming language?",
           "Python","Java","C++","Perl"
   ],
]
levels=[1000,2000,3000,10000,15000]
money=0
for i in range(0,len(questions)):
 question=questions[i]          
 print(f"Your question for{levels[i]}is\n")
 print(f'1.{question[0]}')
 print(f"a.{question[1]}   b.{question[2]}") 
 print(f"c.{question[3]}   d.{question[4]}") 
 ans=int(input("ENter your answer 1-4 or 0 to quit: "))
 if ans<0 or ans>4:
  raise ValueError("Enter valid number")
 if ans== 0:
  money=levels[i-1]
  print("YOur takehome money is RS.",money)
  break
 if (ans == 1):
  print(f"right answer you won RS {levels[i]}\n")
  if i==3 or i==5:
   money=levels[i]
 else:
  print("Wrong answer")
  print("YOu won a total of Rs.",money)
  break

          