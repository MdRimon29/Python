####map() is used to run a function upon each item is a iterable item and like a list 
# and create a new list with the same numbers of items but the values are changed

numbers=[1,2,3,4,5,6]

#def double(a):
#    return a*2
#result=map(double,numbers)
#print (list(result))

#double=lambda a:a*2
#result=map(double,numbers)
#print(list(result))

#result=map(lambda a:a*2,numbers)
#print(list(result))

print(list(map(lambda a:a*2,numbers)))


####filter return a filtered object which is also orginal object

#def is_Even(n):
#    return n%2==0
#result=filter(is_Even,numbers)
#print(list(result))

print(list(filter(lambda n:n%2==0,numbers)))


####reduce is used to calculate a value or sequence

from functools import reduce
expenses=[('Dinner',80),('Car repair',120)]
sum=0
#for expense in expenses:    #without reduce
#    sum+= expense[1]
#print(sum)

sum=reduce(lambda a,b: a[1]+b[1],expenses)

print(sum)