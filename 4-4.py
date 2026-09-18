#4-4

sentence = input("Enter a sentence: ")
words = sentence.split()
result = []
for word in words:
    result.append(word[0].upper() + word[1:].lower())
print("Title case:", " ".join(result))



#output:
#Enter a sentence: he is studying
#Title case: He Is Studying
