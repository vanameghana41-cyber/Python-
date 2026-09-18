#4-3


sentence = input("Enter a sentence: ")
words = sentence.split()
reverse = words[::-1]
print("Reversed order:", " ".join(reverse))

#output:
#Enter a sentence: she is studying
#Reversed order: studying is she
