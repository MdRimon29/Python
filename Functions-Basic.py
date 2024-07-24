#function is a set of instructions which only run when we called it


#def myFunction(name):
#    print("My name is "+name)
#myFunction('Rimon') 


#def myFunction(name='Snowden'): #if dont pass the parameter then print this default value
#    print("My name is "+name)
#myFunction('Rimon') 
#myFunction()    #for this case,we didn't pass any argument,so print snowden


#def myFunction(name,age):      #we can pass more than one argument in a function
#    print("My name is "+name+'.'+'I am '+str(age)+' years old')
#    print(f'My name is {name}.I am {age} years old')   #by using f we can easily showing output
#myFunction('Rimon',21) 

#def myFunction(name):
#    name='Sojeb'
#name='Rimon'
#myFunction(name) 
#print(name)    #so basically a function cannot change the value outside the function
               #so if we change a value inside a function then its doesn't affect outside the function

#def myFunction(person):     #a dictionaries can change inside a function
#    person['name']='Sojeb'
#value={'name':'Rimon'}
#myFunction(value)
#print(value)

#def myFunction(name):   #return statement
#    print(f"Hello {name}!")
#    return name,'Sojeb',21
#print(myFunction('Rimon'))

#age=21  #variable scope.this is a global variable.we can access it from both inside or outside the fucntion
#def myFunction():
#    print(age)
#print(age)
#myFunction()

#def myFunction(phrase):    #nested function
#    def makingWord(word):
#        print(word)
#    words=phrase.split(' ')    #we can use spilit() function and we can give some parameters for spilit 
#    for x in words:
#       makingWord(x)
#myFunction('My name is Rimon') 

#def counter():
#    count=0
#    def increment():
#        nonlocal count  #we need to declare nonlocal for access the variable from present function to outer function
#        count=count+1
#        print(count)
#    increment()
#counter()

def counter():  #closures
    count=0
    
    def increment():
        nonlocal count
        count=count+1
        return count    #a function is terminate when it meets with the return keyword
    
    return increment    #return the inner function

increment=counter()

print(increment())
print(increment())
print(increment())