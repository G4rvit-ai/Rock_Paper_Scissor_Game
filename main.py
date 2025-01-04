'''
Let
r(rock) = -1
p(paper) = 0
s(scissor) = 1

'''

import random                                # Importing random module to generate random numbers

computer = random.choice([-1,0,1])               # Using random module to generate a random number
youStr = input("Enter your choice: ").lower()
youDict  = {"r":-1 ,"p":0 ,"s":1}              
reverseDict = {-1:"Rock", 0:"Paper", 1:"Scissor"}        # Using reverseDict to call youDict for more convinience

you = youDict[youStr]                                  

print(f"You choose {reverseDict[you]}... \nThe Computer choose {reverseDict[computer]}...")     # Using the two variables the "computer" and "you" 


if (computer == you):                                     
    print("It's a draw between the two contenders")                                             

 # Using if-else statement in an if else statemnt

else:
    if (computer == -1 and you == 1):
        print("You Win !")
    
    elif (computer == -1 and you == 0):
        print("You Loose...")
    
    elif (computer == 0 and you == -1):
        print("You Win !")
    
    elif (computer == 0 and you == 1):
        print("You Loose...")

    elif (computer == 1 and you == -1):
        print("You Loose...")

    elif (computer == 1 and you == 0):
        print("You Win !")

    else:
        print("Error, seems something went wrong...")


print("Thank you for playing the Rock Paper Scissor Game") 


    # Programme Ends here
