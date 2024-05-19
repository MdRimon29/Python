a=15
b=10

if a<b:
    print("A is less than B")#identation is must.it means one cannot avoid the whitespace before the begining of a line
elif a==b:
    print("A is equal to B")
else :
    print ("A is greater than B")        

c=20
d=25

print("D") if d>c else print ("=") if c==d else print("C")#this technique is called Ternary Operators or Conditional expressions
if(d>c): print("D is greater than C")

e=40
f=50
g=60

if (g>f) and (f>e):#similarly we can use "or" keyword as a logical operator
    print("G is greater than F and E")

h=10
i=15

if not h>i:
    print("I is greater than H")

num=100

if num>50:
    print("Num is greater than 50")
    if num>20:
        print("Num is also greater than 20")
    else:
        print("Num is greater than 50 but not greater than 20")


k=50
l=60
if k>l:
    pass