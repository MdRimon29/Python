#Tuples are used to store multiple items in a single variable
#Tuple items are ordered, unchangeable, and allow duplicate values.
#we cannot modify tupples,that means we cannot add or remove from tupples
#we use () bracket instead of {} or [] for tupples,ex- subject=("eee",'cse','me',phy)

names=('Rimon','Hasib','Monir','Mehedi')

#print(names[-1])   #for access an element

#print(names.index('Hasib'))    #for find an index for existing element 

#print(len(names))  #for find the length for the tupples

#print('Tanvir' in names)   #we can use in for check that is that element exist in our tupples or not

#print (names[-4:])  #for slicing tupples

#print(sorted(names))    #when we sorted a tupples,it basically sort and create a new tupples,not modify the previous one

newNames=names+('Sojeb','Joy','Ashfaque')   #we can create a new tupples from an existing tupples by using + operator

print (newNames)