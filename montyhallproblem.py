import random
# Monty presents 3 doors, 2 with garbage, 1 with a prize
# Contestant picks door A, for example
# Monty, knowing the prize is in door B, opens door C, revealing garbage
# Is it better to stay with door A, or switch to door B?

# This program will run the simulation with random n times, and display the results for number of wins and losses.

def montyHall(n):
    print("Running Monty Hall problem " + str(n) + " times with random inputs...")

    numWins = 0
    numLosses = 0

    for _ in range(n):
        # Contestant door is randomly picked
        door = random.randint(1, 3)

        # Prize door is randomly picked
        prizeDoor = random.randint(1, 3)

        # Monty picks door that is not the prize and not the one Contestant picked
        while(True):
            montyPick = random.randint(1, 3)
            if(montyPick != door and montyPick != prizeDoor):
                break

        # Picks the remaining unpicked door
        for i in range(1, 4):
            if(i != door and i != montyPick):
                temp = i

        # Choice to switch is randomly picked
        switch = random.randint(0, 1)

        # Switch to other door if randomly chosen to 
        if(switch == 1):
            door = temp

        if(door == prizeDoor):
            numWins += 1
        else:
            numLosses += 1

    # Print results of n trials
    print("------------------------")
    print("Total Wins: " + str(numWins))
    print("Total Losses: " + str(numLosses))
    print("Win Rate: " + str((numWins / n) * 100) + "%")
    print("------------------------")

    # If we set switch to always 0, win rate is almost exactly 1/3
    # If we set switch to always 1, win rate is almost exactly 2/3
    # If we randomly set switch, win rate is almost exactly 1/2, as half the time it's 1/3 and half the time it's 2/3

def manualMonty():
    while(True):
        door = input("Enter door 1, 2, or 3: ")
        if(door in "123" and door != ""):
            door = int(door)
            break
        else:
            print("Wrong input! Please enter an int from 1 to 3...")
    
    # Prize door is randomly picked
    prizeDoor = random.randint(1, 3)

    # Monty picks door that is not the prize and not the one Contestant picked
    while(True):
        montyPick = random.randint(1, 3)
        if(montyPick != door and montyPick != prizeDoor):
            break
    
    for i in range(1, 4):
        if(i != door and i != montyPick):
            temp = i
    
    while(True):
        switch = input("Monty picked door number " + str(montyPick) + ", do you want to switch from door " + str(door) + " to door " + str(temp) + "? ")
        if(switch == "y" or switch == "n"):
            if(switch == "y"):
                door = temp
            break
        else:
            print("Wrong input! Please enter either 'y' or 'n'...")

    print("The prize was behind door number " + str(prizeDoor) + "!")
    if(door == prizeDoor):
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost...")

def main():
    while(True):
        try:
            n = int(input("Enter how many simulations you want to run (enter 0 or less for a manual simulation): "))
        except: 
            print("Wrong input! Please enter an int...")
            continue
        break
    if(n >= 1):
        montyHall(n)
    else:
        manualMonty()

main()