#recursion is when a function called itself automaticlly

#factorial

def factorial(n):
    if n==0 :return 1
    return n*factorial(n-1)

print(factorial(5))