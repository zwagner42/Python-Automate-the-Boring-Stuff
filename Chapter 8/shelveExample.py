#! python3
# shelveExample - Program to demonstrate the shelve module
# Use plaintext to store human readable informaion, shelve for non-human readable information

import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

print('-----------------------')
shelfFile = shelve.open('mydata')
print(type(shelfFile))
print(shelfFile['cats'])
shelfFile.close()

print('--------------------------')
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))	#Important to use list since .keys() returns a list-like value not a list
print(list(shelfFile.values()))
shelfFile.close()