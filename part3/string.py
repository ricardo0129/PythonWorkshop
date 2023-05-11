#create two strings and join them
firstName = "Ricardo"
lastName = "Ruiz"
space = " "
fullName = firstName + space + lastName
print(fullName)

#split a sentece by spaces stores all the words in an array
sentence = "my dog was very hungry so she ate my homework"
words = sentence.split(" ")
print(words)

#only chose part of the entire string from letters 6-14
sentence = "today I decided to go to the movies"
section = sentence[6:15]
print(section)

sentence = "The sky is very clear today I cannot find a cloud"
whereIsSky = sentence.find("sky")
print(whereIsSky)
