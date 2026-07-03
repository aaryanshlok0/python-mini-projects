from datetime import date,timedelta
import random


def main():
    number_of_birthdays=int(input("Enter no of birthdays to be genrated: "))
    generated_birthdays = gen_birthdays(number_of_birthdays)

    for birthday in generated_birthdays:
        print(birthday.strftime("%d %B"),end='')
        

    duplicate=has_duplicate_birthdays(generated_birthdays)
    if duplicate:   
        print("A duplicate birthday was found.")
    else:
        print("No duplicate birthday found.")
    simulation_count=int(input("Enter no of simulations to run: "))
    matches=0
    for i in range(simulation_count):
        birthdays = gen_birthdays(number_of_birthdays)

        if has_duplicate_birthdays(birthdays):
            matches += 1

    probability=(matches/simulation_count)*100
    print(f"Out of {simulation_count} simulations,{matches} had matching birthdays.Estimated probability: {round(probability,2)}%")



def gen_birthdays(number_of_birthdays):
    starting_date=date(2026,1,1)
    birthdays=[]

    for i in range(number_of_birthdays):
        random_day=random.randint(0,364)
        random_duration=timedelta(days=random_day)

        birthday_date=starting_date+random_duration
        birthdays.append(birthday_date)
    return(birthdays)

def has_duplicate_birthdays(birthdays):
    if len(birthdays)!=len(set(birthdays)):
        return True
    return False



main()
