#This is a snake, water and gun game for 3 points between user and computer.

#snake beats water, water beats gun, gun beats snake

import random 
import time

name=input("Please enter your name: ")
print(f"Welcome to the Snake,Water,Gun game {name}! First to 3 points wins. Let the battle begin! 🐍💧🔫\n")

print("The key mapping for game is as following\n1. Snake 🐍\n2. Water 💧\n3. Gun 🔫")

swg={1:"Snake",2:"Water",3:"Gun"}

user_score=0
comp_score=0

def display_choices():
        print(f"User choice: {swg[user_input]}")
        print(f"Computer choice: {swg[comp_choice]}")


while user_score<3 and comp_score<3:
    
    user_input=int(input("\nChoose between snake, water and gun: "))
    comp_choice=(random.randint(1,3))

    if user_input==comp_choice:
            print("That's a draw!!\n")
            display_choices()
            time.sleep(1.5)
            

    elif user_input==1 and comp_choice==2:
            print(name,"wins!!")
            user_score+=1
            display_choices()
            time.sleep(1.5)

    elif user_input==2 and comp_choice==1:
            print("Computer wins!!")
            comp_score+=1
            display_choices()
            time.sleep(1.5)

    elif user_input==2 and comp_choice==3:
            print(name,"wins!!")
            user_score+=1
            display_choices()
            time.sleep(1.5)

    elif user_input==3 and comp_choice==2:
            print("Computer wins!!")
            comp_score+=1
            display_choices()
            time.sleep(1.5)

    elif user_input==3 and comp_choice==1:
            print(name,"wins!!\n")
            user_score+=1
            display_choices()
            time.sleep(1.5)

    elif user_input==1 and comp_choice==3:
            print("Computer wins!!\n")
            comp_score+=1
            display_choices()
            time.sleep(1.5)

    else:
            print("Invalid input!!\n")
    
time.sleep(1)
if comp_score==3:
    print(f"Computer wins, better luck next time!")    
elif user_score==3:
    print(f"\nCongrats {name}, you win!!")

