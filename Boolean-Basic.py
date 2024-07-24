#or genarally return the first value if that value is not a false value,otherwise it return second value
#if x is false then y else x

print (0 or 1) ##1
print (False or 'hey') ##'hey'
print ('hi'or 'hey') ##'hi'
print ([ ] or False) ##'false'
print (False or []) ##[]

#and only valuate 2nd argument when first one is false
#if x is false then x else y

print (0 and 1) ##0
print (False and 'hey') ##false
print ('hi'and 'hey') ##'hey'
print ([ ] and False) ##[]
print (False and []) ##false