import random


def main():
    print("Welcome to Cho-Han!")
    balance=bet()
    print(f"Thanks for playing Cho-Han!\nFinal balance: {balance}") 


def rolling_dices():
    print("Rolling dices!!")
    dice_1=random.randint(1,6)
    print(f"Value on first dice is {dice_1}")
    dice_2=random.randint(1,6)
    print(f"Value on second dice is {dice_2}")

    dice_total=dice_1+dice_2
    print(f"Total value on dice is {dice_total}")
    if dice_total%2==0:
        print("Result: Cho")
        return "C"
    else:
        print("Result: Han")
        return "H"
    



    
def bet():
    BALANCE=3000
    print(f"Your current balance is {BALANCE}")
    while BALANCE>0:

        amount=int(input("Enter the amount you want to bet: "))

        while amount <= 0 or amount > BALANCE:
            print('Invalid amount entered!')
            amount =int(input("Enter the amount you want to bet: "))
            
        user_input=input("(C)ho or (H)an to make a guess!").upper()
        while user_input not in ('C','H'):
            print("Invalid input")
            user_input=input("(C)ho or (H)an to make a guess!").upper()

        result=rolling_dices()

        if user_input==result:
            BALANCE+=2*amount
            print("Congrats!You won")
        else:
            BALANCE-=amount
            print("Better luck next time!")
        
        print(f"Balance:{BALANCE} ")
        
        userch=input("Would you like to continue? (Y)es or (N)o ")
        if userch in 'Yy' and BALANCE>0:
            continue
        else:
            break

    return BALANCE
        

main()
