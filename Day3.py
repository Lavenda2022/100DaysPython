print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

a = input("Do you want to go left or right?")
if (a == "right") or (a!= "left") :
    print("You fall into a hole, Game Over!")
else:
    b = input("Do you want to swim or wait?")
    if (b == "swim") or (b != "wait"):
        print("You attacked by trout, Game Over!")
    else:
        c = input("Which door will you choose: red, blue or yellow?")
        if c == "red":
            print("You burned by fire, Game Over!")
        elif c == "blue":
            print("You eaten by beasts, Game Over!")
        elif c == "Yellow":
            print("You win!")
        else:
            print("Game Over!")
