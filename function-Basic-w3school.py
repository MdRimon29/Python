def function():
    print("My name is Rimon")

function()

def my_function(sname):
    print(sname +" is my favourite subject")

my_function("CSE")
my_function("EEE")
my_function("ME")

def my_function2(fname,lname):
    print(fname+ " "+lname)

my_function2("Raisul","Rimon")
my_function2("Nafiul","Hasib")
my_function2("Sojeb","Sikder")

#Arbitrary Arguments
#if the numbers of keyword is unknown

def my_function3(*player):
    print (player[2])

my_function3("Messi","Ron","Neymar","Mbappe")

#Keyword arguments

def my_function4(player3,player1,player2):
    print(player1 +" "+ player3+" "+ player2)

my_function4(player1="Messi",player2="Ron",player3="Neymar")

#Arbitrary Keyword Arguments
#if the numbers of keyword arguments is unknown

def my_function5(**player):
    print (player["player2"])

my_function5(player1="Messi",player2="Ron",player3="Neymar")

#return value

def my_function6(x):
    return 10+5*x

print(my_function6(5))

#positional only arguments
def my_function3(player1,player2,/):
    print (player1,player2)

my_function3("Messi","neymar")

#Keyword only arguments

def my_function7(a,b,c,d,/ , *, e,f):
    print(a+b+c+d+e+f)

my_function7(1,2,3,4,e=5,f=6)

#Recursion
#function called itself

def recursion(x):
    if (x==0):
        return 0
    
    else :
        return x+recursion(x-1)
    
print(recursion(5))