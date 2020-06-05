# 1st of June 2020

affirmations = {
    "loved": "You love and accept yourself exactly as you are.",
    "valuable": "You are a valuable person with many good qualities.",
    "courageous": "You are strong and face difficulties with courage.",
    "capable": "You are capable of achieving anything you want.",
    "deserving": "You are loved and loving. You deserve to receive love.",
    "positive": "You are a positive person and you attract positive events to your life.",
    "responsible": "You are responsible for yourself and your own future.",
    "generous": "You look at everyone and everything with kind and generous eyes.",
    "perfect": "You are perfect exactly as you are. You accept yourself fully.",
    "healthy": "You are healthy and allow life to flow through you.",
    "respectful": "You respect all creatures you come into contact with.",
    "intelligent": "You are an intelligent person and you learn from everybody.",
    "thankful": "You are thankful for every day of your life.",
    "relatable": "You strive to maintain good relationships with others.",
    "intuitive": "You listen to your intuition.",
    "grateful": "You are grateful for all your blessings.",
    "strong": "You live your life fully with strength and joy."
}

the_keys = ""
for key in affirmations:
    the_keys = the_keys + key + " "
print("\nThe following words are recognised by the Affirmation Bot:")
print(the_keys)

while True:
    message_output = False
    sentence = input("\nHow are you feeling? ")
    sentence = sentence.lower()

    if sentence == "q":
        break

    words = sentence.split(" ")

    for word in words:
        if word in affirmations:
            print(affirmations[word])
            message_output = True

    if not message_output:
        print("Keep on going you will eventually find what you are seeking.")

print("Farewell!")

# 2nd of June 2020

number = int(input("\nPick a number between 1 and 10."))
x = (number)
print(f"The square of your number is {x * number}")

colour = input("\nChoose a colour.")
colour = colour.lower()
if colour == "Red" or "Blue" or "Green":
    print("Not good enough!")
    another_colour = input("Try another colour.")
    another_colour = another_colour.lower()
    if input == "Red" or "Blue" or "Green":
            print("Ok cool byeee")
    else:
        print("Goodbye!")
else:
    print(f"Your colour is {colour}")

base_number = int(input("\nChoose a number. "))
finishing_number = base_number * (4 / (2 *5))
print(f"When playing around with this number it becomes {finishing_number}")

# 3rd of June 2020

minimum_age = 18
my_age = int(input("\nWhat's your age?"))

entry_pass = minimum_age <= my_age

if entry_pass == True:
    print("Welcome in!")
else:
    print("You're not of age. Sorry.")

email = input("\nWhat's the email?")
is_email = bool(email)
print(f"The email is present: {is_email}")

lock = "Close"
unlock = "Open"

lock = lock.lower()
unlock = unlock.lower()

is_open = input("\nVoice activation required!")

if is_open == unlock:
    print("Access Granted!")
else:
    print("Access Denied.")

is_closed = input("\nVoice activation required!")

if is_closed == lock:
    print("Door closing!")
else:
    print("Wrong wake-word.")