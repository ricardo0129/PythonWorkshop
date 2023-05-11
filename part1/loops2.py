#sum all the numbers from 0-9999
sum = 0
for i in range(0, 10000):
    sum = sum + i
print(sum)

#we can also use a while loop to do the same thing
sum2 = 0
i = 0
while i<10000:
    sum2 = sum2 + i
    i = i+1
print(sum2)

#we can use a while loop to create an infinite loop
while True:
    choice = input()
    print(choice)
    if choice == "exit":
        break