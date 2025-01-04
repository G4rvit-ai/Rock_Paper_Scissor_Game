'''
Let
s(snake) = -1
w(water) = 0
g(gun) = 1

'''
import random                                # Importing random module

computer = random.choice([-1,0,1])               # Using random module
youStr = input("Enter your choice: ").lower()
youDict  = {"s":-1 ,"w":0 ,"g":1}              
reverseDict = {-1:"Snake", 0:"Water", 1:"Gun"}        # Using reverseDict to call youDict for more convinience

you = youDict[youStr]

print(f"You choose {reverseDict[you]}... \nThe Computer choose {reverseDict[computer]}...")     # Using the two variables the "computer" and "you" 



if (computer == you):                                    # Using if-else statement in an if else statemnt
    print("It's a draw between the two contenders")


if ((computer - you) == -1 or (computer - you)  == 2):  
    print("You Loose...")

else:
    print("You Win !")                                      

# Summation of the input of Computer and the user below

'''

# Calculating the sum here   

The below logic is written on the basis of the value (computer - you)


if (computer == you):                                     
    print("It's a draw between the two contenders")                                             

else:
    if (computer == -1 and you == 1):         Sum  = -2
        print("You Win !")
    
    elif (computer == -1 and you == 0):      Sum  = -1
        print("You Loose...")
    
    elif (computer == 0 and you == -1):      Sum  = 1
        print("You Win !")
    
    elif (computer == 0 and you == 1):       Sum  = -1
        print("You Loose...")

    elif (computer == 1 and you == -1):      Sum  = 2
        print("You Loose...")

    elif (computer == 1 and you == 0):       Sum  = 1
        print("You Win !")

    else:
        print("Error, seems something went wrong...")

'''

print("Thank you for playing the SWG Game") 


        # Programme Ends here