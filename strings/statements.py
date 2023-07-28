# Match case statements
# here python tries to match the user input with the cases included.
a=int(input("Enter the value of a(1-12): "))
match a:
    case 0:
        b="invalid input"
        print(b)
    case 1:
        print("It\'s January")
    case 2:
        print("It\'s February")
    case 3:
        print("It\'s March")
    case 4:
        print("It\'s April")
    case 5:
        print("It\'s May")
    case 6:
        print("It\'s June")
    case 7:
        print("It\'s July")
    case 8:
        print("It\'s August")
    case 9:
        print("It\'s September")
    case 10:
        print("It\'s October")
    case 11:
        print("It\'s November")
    case 12:
        print("It\'s December")
    case _:    
        error="invalid input"
        print(error)

 
