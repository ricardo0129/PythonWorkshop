#create a function that prints a simple menu
def printMenu():
    print("1. Print a greeting")
    print("2. Print a farewell")
    print("3. Print my Name")
    print("4. Exit")


#print the menu and get the users choice
printMenu()
choice = int(input())

#use if/elif/else statements depending on the choice given
if choice == 1:
    print("Hi there nice to meet you")
elif choice == 2:
    print("See you next time")
elif choice == 3:
    print("My name is Ricardo")
else:
    print("Program is done")