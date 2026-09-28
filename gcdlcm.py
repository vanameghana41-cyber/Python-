def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

print("GCD(48, 18) =", gcd(48, 18))
print("LCM(48, 18) =", lcm(48, 18))
'''GCD(48, 18) = 6
LCM(48, 18) = 144'''
