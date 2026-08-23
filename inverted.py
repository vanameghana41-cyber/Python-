

n = 5  

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print() 
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)
n = 4
for i in range(1, n + 1):
    print("*" * (2*i - 1))
for i in range(n, 0, -1):
    print("*" * (2*i - 1))
n = 5
for i in range(1, n + 1):
    print((str(i) + " ") * i)
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1): print(j, end=" ")
    for j in range(i - 1, 0, -1): print(j, end=" ")
    print()
n = 5
for i in range(1, n + 1):
    ch = chr(64 + i)
    print((ch + " ") * i)
n = 4
for i in range(1, n+1):
    print(" "*(n-i) + "* " + " "*(i-1) + "*")
for i in range(n, 0, -1):
    print(" "*(n-i) + "* " + " "*(i-1) + "*")
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
n = 4
for i in range(1, n+1):
    print("* " * i + "  " * (n-i) + "* " * i)
for i in range(n, 0, -1):
    print("* " * i + "  " * (n-i) + "* " * i)
