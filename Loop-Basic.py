#while loops are defined using while keyword,and they repeat their block until their conditional statement are false

#count=0 #initialization part
#while count<10: #condition part
#    print(f'The number is {count}')     #execution part
#    count +=1   #increment part

#names=['Rimon','Hasib','Sojeb','Somel']
#for index,name in enumerate(names):
#    print(index ,name)

#items=[1,2,3,4]
#for item in items:
#    if item==2:
#        break
#    print(item)

items=[1,2,3,4]
for item in items:
    if item==2:
        continue
    print(item)