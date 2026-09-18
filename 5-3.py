#5-3

s = input("Enter a string: ")
done = ""
for ch in s:
    if s.count(ch) > 1 and ch not in done:
        print(ch, ":", s.count(ch))
        done += ch



#output:
#Enter a string: HELLO
#L : 2
        
        
