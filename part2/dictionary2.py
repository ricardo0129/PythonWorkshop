#create a dictionary like before but in a shorter way
names_age = dict({'Blue': 11, 'Lance': 31, 'Wallace': 25, 'Cynthia': 35, 'Alder': 44})

#update the value of Blue to 1
names_age['Blue'] = 1
print(names_age)

#update it back but using the update method
names_age.update({'Blue': 11})
print(names_age)

#get the value for the lance key
print(names_age.get('Lance'))

#get a list of all keys 
#note the list function is used to actually create the list
#try printing the result of names_age.keys() without that function
all_keys = list(names_age.keys())
print(all_keys)

#we can do the same but for the values in the dictionary 
all_values = list(names_age.values())
print(all_values)