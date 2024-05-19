cars=["BMW", "Rolls Royce", "Mercedes","Toyota","Lamborghini","Bugatti"]

for x in cars:
    print(x,end=" ")#use end='' or end="" for avoid newline

print (end='\n')#for create a newline 

name='Raisul'
for x in name:
    print (x,end='')

print(end='\n')

subject=['EEE','CSE','Math','ENG','BAN','CE','BIO']
for x in subject:
    if x=='BAN':
        break   #must add a whitespace for identation
    if x=='Math':
        continue
    print(x)

for x in range(2,40,2):#start from 2,end before 40 and increase 2 every round
    print (x,end='')

print(end='\n')

for x in range(4):
    print(x)
else:
    print('Done')   #else execute when the loop is finished 

for x in [1,2,3]:
    pass

for i in subject:
    for j in cars:
        print(i,j)