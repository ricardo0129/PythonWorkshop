#create a list with some values already in it
animals = ['cat', 'dog', 'cow', 'seahorse', 'tiger', 'lion']

#We can take slices of the list which allows us to take a chunk only
#list[start:stop] doesn't include the stop element 
subset_list = animals[1:4]
print(subset_list)
#it doesn't change the original list
print(animals)

#create a new list of animals and add that entire list to 
#our original list of animals using extend
more_animals = ['spider', 'whale', 'geko', 'snake']
animals.extend(more_animals)
print(animals)

#insert an animal to the second position
animals.insert(1, 'horse')
print(animals)

length = len(animals)
print(length)