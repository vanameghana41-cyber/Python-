ch = input("Enter the character: ")
vowels = ['a', 'e', 'i', 'o', 'u']

if ch.isdigit():
    print("It is a digit")
elif ch.isalpha():  
    if ch.lower() in vowels:
        print("It is a vowel")
    else:
        print("It is a consonant")
else:
    print("It is a special symbol")
#Enter the character: a
#It is a vowel
