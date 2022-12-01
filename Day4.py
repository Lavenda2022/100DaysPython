#Rock Paper Scissors

import random

you = int(input("What do you choose? Type 0 for rock,1 for paper or 2 for scissors.\n"))

computer = random.randint(0,2)
print(f"Computer choose {computer}.")

if (you == 0) and (computer == 2):
    print("You win.")
elif (computer == 0) and (you == 2):
    print("You lose.")
elif computer > you:
    print("You lose.")
elif computer == you:
    print("It is a draw.")
else:
    print("Invalid input, you lose!")
