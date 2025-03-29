import random
import string  #to randomly generate strings
name=input("Enter your name: ")
print("Hello", name)


text=input(f"Enter the text your want to encode or decode: ").lower()

user_choice=int(input("Press 1 to encode your text\nPress 2 to decode your text:\n"))

#creating dictionary and assigning values to replace
f = {
    'a': 'm', 'b': 'x', 'c': 'j', 'd': 'q', 'e': 'z', 'f': 'a', 'g': 't', 'h': 'o', 'i': 'w', 'j': 'b', 'k': 'p', 
    'l': 'd', 'm': 'y', 'n': 'h', 'o': 'u', 'p': 'e', 'q': 'v', 'r': 'n', 's': 'l', 't': 'c', 'u': 'f', 'v': 'g', 
    'w': 'r', 'x': 's', 'y': 'i', 'z': 'k', ' ': 'g', '.': 'a'
}

f_decode = {value: key for key, value in f.items()}

# Convert to translation tables
encoding_table = str.maketrans(f) #to replace characters in one go as .replace is sequential
decoding_table = str.maketrans(f_decode)

if user_choice==1:   
    if (len(text))<3:     #This reverses the string when text entered is less than 3 characters.
        a=(text[::-1])
        print(a)
    
    elif (len(text))>=3:
        b=(text[1::])
        c=''.join(random.choices(string.ascii_letters,k=3)).lower() #converts list to string using ''.join so can easily concatenate the strings 
        d=text[0]
        e=c+b+d

        #creating f and assigning all replaces 
       
        text1 = e.translate(encoding_table)
        print(text1)

          

elif user_choice==2:
  
    decoding_dict = {value: key for key, value in f.items()}   #swapping the values of key and value as to decode them

    if len(text)<3:
        print(text[::-1])
    elif len(text)>=3:
        a=text[3:-1]
        b=text[-1]
        c=b+a
        text2 = c.translate(decoding_table)
        
        print(text2)

else:
    print("Invalid input, please try again!.")

