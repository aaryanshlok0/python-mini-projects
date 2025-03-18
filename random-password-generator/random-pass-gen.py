#a random password generator which generates strong password having 6 or more characters comprising alphabets,digits and punctuations

import string
import random
n=int(input("Enter the number of characters you want in your password: ")) #min password length should be atleast 6 for better security
if n<6:
    print("❌A strong password must have at least 6 characters. Please try again!")
else:
    password=(''.join(random.choices(string.ascii_letters + string.digits + string.punctuation,k=n))) 
    print(f"✅The generated password is: {password}")
    # ''.join() converts the list of characters into a string

