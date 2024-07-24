#List generally store multiple value/items in a single variable
#List items are ordered, changeable and allow duplicate values.

myList=["BMW","Banana","BMW","Football"]

print(myList)
print(len(myList))
print(type(myList))

myList2=list(("Mango",42,"River"))#list constructor

print(myList2)
print(type(myList2))

##### Access List Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[1])
print(thislist[-1])
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

##### Change List Items

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]  #The length of the list will change when the number of items inserted does not match the number of items replaced.
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

##### Add List Items

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")  #To add an item to the end of the list
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  #To insert a list item at a specified index
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  #To append elements from another list to the current list
print(thislist)            #The elements will be added to the end of the list.

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)  #can add any iterable object (tuples, sets, dictionaries etc.)
print(thislist)

##### Remove List Items

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  #The remove() method removes the specified item.
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")  #If there are more than one item with the specified value, the remove() method removes the first occurrence
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  #The pop() method removes the specified index.
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()  #If you do not specify the index, the pop() method removes the last item.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]  #del keyword also remove specific index item
print(thislist)

#thislist = ["apple", "banana", "cherry"]  #it will delete full list
#del thislist
#print(thislist)

thislist = ["apple", "banana", "cherry"] 
thislist.clear()  # just delete the items in the list
print(thislist)

##### loop List

thislist = ["apple", "banana", "cherry"]

for x in thislist:
  print(x)

for i in range(len(thislist)):
  print(thislist[i])

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

[print(x) for x in thislist]