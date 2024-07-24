#annotation optionally allow to do a specify a variable parameter or a functions return value
#python basically ignore this annotations

def increment(n :int)->int:
    return n+1

print(increment(5))