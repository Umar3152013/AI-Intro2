# Greet the user
print("Hello! I am an AI Bot. What's your name?")

# Get user input
name=input()

#Respond to the user's name
print(f"Nice to meet you, {name}!")
# ask a questio
print(f"how are you doing today ?(good/bad) :")
mood = input().lower()
if mood == "good":
    print(f"I am glad to hear that from you")
elif mood == "bad":
    print(f"I am sorry to hear that, hope you feel better")
else:
     print(f"I see!")
print(f"it was nice chatting with you {name}. Good bye")
