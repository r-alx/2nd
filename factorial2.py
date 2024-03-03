def factorial(hoho):
    fast = 1
    ff = 1
    while ff <= hoho:
        fast = fast * ff
        ff = ff + 1
    return fast
fast = factorial(7)
print("the factorial is:",fast)