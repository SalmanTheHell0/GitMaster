print("IQ Test \n\tapproved by MENSA International! (not really)")

instructions = """\nInstructions/ rules:\t
\tAnswer goes straight after the question
\tNo cheating!
\tAnd most importantly have fun! (somehow)"""

print(instructions)

first_question = int(input("\nIf CAT = 3, PUPPY = 5 and MOTHER = 6, then what does CORONAVIRUS equal?"))

if first_question == 11:
    print("Well done! The answer is 11!")
else:
    print("Bad Luck :(")

second_question = input("""\nThere are 4 girls, they are Bethany, Charlotte, Bess and Susan. 
Bethany is watching TV:
Charlotte is playing chess:
and Bess is reading a book. What is Susan doing?""")
second_question = second_question.lower()

if second_question == "Playing chess" or "Playing chess with Charlotte":
    print("\nWell done! She is playing chess with Charlotte!")
else:
    print("\nThat was a tough one to be fair!")

third_question = int(input("""\nThere are 3 doors and you have to go in one of them:
One door has poisonous gas
Another is where Jack The Ripper (a murderer from the 1800s) stays
And the last one is a doorway to a warzone. Which door is safe (put your answer in numbers, first is 1 then 2 and last is 3)?"""))

if third_question == 2:
    print("Correct! If Jack The Ripper was active in the 1800s he'd be dead!")
    print("\nYour IQ totals up to 145!")
else:
    print("It was the second door :(")
    print("Your IQ totals up to 93!")