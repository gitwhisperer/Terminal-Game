import random

print("Welcome to the Space Adventure!")
print("You are the captain of a spaceship exploring an unknown galaxy.")

while True:
    print("\nYou encounter a strange planet. What do you want to do?")
    print("1. Land on the planet")
    print("2. Continue exploring space")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        print("\nYou land on the planet and find an alien civilization.")
        print("What do you want to do?")
        print("1. Communicate with the aliens")
        print("2. Attack the aliens")
        choice = input("Enter 1 or 2: ")
        
        if choice == '1':
            print("\nThe aliens are friendly and share their advanced technology with you.")
            print("You gain new knowledge and resources for your journey.")
            outcome = "success"
        elif choice == '2':
            print("\nThe aliens are hostile and fight back.")
            if random.choice([True, False]):
                print("You win the battle and take their resources.")
                outcome = "success"
            else:
                print("You lose the battle and your spaceship is destroyed.")
                outcome = "failure"
        else:
            print("Invalid choice. Try again.")
            continue
    elif choice == '2':
        print("\nYou continue exploring space and find a mysterious space station.")
        print("What do you want to do?")
        print("1. Dock at the space station")
        print("2. Ignore the space station and keep exploring")
        choice = input("Enter 1 or 2: ")
        
        if choice == '1':
            print("\nYou dock at the space station and find valuable supplies.")
            print("You gain new resources for your journey.")
            outcome = "success"
        elif choice == '2':
            print("\nYou keep exploring but run out of fuel and resources.")
            print("Your spaceship drifts aimlessly in space.")
            outcome = "failure"
        else:
            print("Invalid choice. Try again.")
            continue
    else:
        print("Invalid choice. Try again.")
        continue

    if outcome == "success":
        print("\nCongratulations! You successfully completed your space adventure.")
    else:
        print("\nGame Over. Better luck next time.")
    
    choice = input("\nDo you want to play again? (yes/no): ")
    if choice.lower() != 'yes':
        print("Thanks for playing! Goodbye.")
        break

