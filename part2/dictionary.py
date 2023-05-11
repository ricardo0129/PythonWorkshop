#create an empty dictionary called names_age
#the dictionary will store the key value pair (name,age)
names_age = dict()

names_age['Blue'] = 11
names_age['Lance'] = 31
names_age['Wallace'] = 25
names_age['Cynthia'] = 35
names_age['Alder'] = 44
print(names_age)

#we can access the value for a given key with the index syntax
#we then store this value in a variable called cynthia_age
cynthia_age = names_age['Cynthia']
print(cynthia_age)

#to remove an element we use the pop method which takes in a key
names_age.pop('Lance')
print(names_age)

#to iterate over all the keys in alphabetical order we just 
#use a loop
for keys in names_age:
    print(keys)

#to actually print the keys and ages we can do something similair
for key in names_age:
    print(keys, names_age[key])