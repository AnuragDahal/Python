'''There is no built in do while loop in python but we cam emulate it'''
# Emulation of do while loop 
secret_word = "python"
counter = 0
while True:# true is used to print the user input at least once
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        print("right answer")
        break# it is used to exit a loop
    if word != secret_word and counter > 3: 
        print("Error")
        break