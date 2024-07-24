#Dictionaries generally store multiple value/items in a single variable
#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionaries are allows to create key-value pairs
#we use {"key":"value" } for dictionaries

person={'name':'Rimon','age':21,'edu':'BSc'}

#print (person) #print a dictionaries

#print (person['name'])  #print the values for a key

#person['name']='Snowden'    #way to change a element(value)
#print (person)

#print(person.get('color' , 'light brown'))  #another way to get a value by using 'get()' function
                                            #if get cannot find the key in the dictionaries it print "None"
                                            #we can set a default value against the key,then if it cannot find the key in the dictionaries then it print that default vlaue
                                            #but if it can find the value then it cannot return that dafault value

#print (person.pop('name'))  #pop a specific key and value
#print (person)  #print the dict after pop that specific key and value

#print(person.popitem()) #by using popitems it pop the last index key and value
#print(person)

#print('name' in person) #to check if the key in the dictionaries or not

#print(person.keys())    #get a list with the keys using a key method
#print(list(person.keys()))  #by using list we can find the actual keys list part

#print(person.values())   #get a list with the values using a key method
#print(list(person.values()))    #by using list we can find the actual values list part

#print(len(person))  #how many items in the dictionaries

#print(list(person.items()))     #each items of the dictionaries now a list

#person['favorite food']='Biriyani'  #how to add an items in the dictionaries
#print(person)

#del person['edu']   #use del keyword to delete a key from the dictionaries
#print ( person)

personCopy=person.copy()    #use copy methods to copy a dictionaries
print(personCopy)