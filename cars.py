print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if(choice == 1):
    print("What type of bike?")
    print("1.Normal\n")
    print("2.Mountain\n")

choice2=int(input("Enter your choice2: "))
if choice2==1:
    print("You have selceted normal")
else:
    print("You have selected mountain")

if (choice==2):
    print("What type of car?")
    print("1.SUV")
    print("2.Truck")
    choice3=int(input("Enter your choice3: "))

    if choice3==1:
        print("You have selected a SUV")
    else:
        print("You have selected a truck")

else:
    print("Wrong choice")

