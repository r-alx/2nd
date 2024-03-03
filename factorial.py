# 5! =   1*2*3*4*5
# 3! = 1*2*3

#write a function that calcute the factorial of the given number.

def factorial(num):
    fact = 1
    c = 1
    while c <= num:
        fact = fact * c
        c = c + 1
    return fact

fact = factorial(5)
print("THe factorial is ", fact)