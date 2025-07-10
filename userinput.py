name = input("What is your name?: ")
age = int(input("What is your age?: "))

age = age + 1

print (f"Hello {name}!")
print("Happy Birthday!")


if age > 120:
    print("Please put a valid age")
    age = int(input("Put your age again: "))
    print(f"Your age is {age} years old.")
else:
    print(f"Your age is {age} years old.")
