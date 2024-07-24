#decorator is a function which take function as a parameter

def logtime(func):
    def wrapper():
        print("First call or before")

        val=func()
        print('Second call or after')

        return val
    return wrapper

@logtime
def name():
    print("My name is Rimon")

name()