def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    else:
        return base * power(base, exp - 1)

print("2^5 =", power(2, 5))
print("2^-3 =", power(2, -3))
'''2^5 = 32
2^-3 = 0.125'''
