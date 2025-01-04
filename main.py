'''
Let
s(snake) = -1
w(water) = 0
g(gun) = 1

'''

import random                                # Importing random module to generate random numbers

computer = random.choice([-1,0,1])               # Using random module to generate a random number
youStr = input("Enter your choice: ").lower()
youDict  = {"s":-1 ,"w":0 ,"g":1}              
reverseDict = {-1:"Snake", 0:"Water", 1:"Gun"}        # Using reverseDict to call youDict for more convinience

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


print("Thank you for playing the SWG Game") 


    # Programme Ends here