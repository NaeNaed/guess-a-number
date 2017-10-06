import random
import math

def get_name():
    print(" ")
    player_name = input("Please enter a name ")
    print(" ")
    return player_name
    
def show_start_screen():
    print(""" __    _     ____  __   __        __        _      _     _      ___   ____  ___        __         _       
/ /`_ | | | | |_  ( (` ( (`      / /\      | |\ | | | | | |\/| | |_) | |_  | |_)      / /\   __  | |  __  
\_\_/ \_\_/ |_|__ _)_) _)_)     /_/--\     |_| \| \_\_/ |_|  | |_|_) |_|__ |_| \     /_/--\ (_() |_| (_()           """)
def show_credits():
    print(""" __    ___   ____   __   _____  ____  ___       ___   _          __    _     ____    _    __    _      ___   ___   ___  
/ /`  | |_) | |_   / /\   | |  | |_  | | \     | |_) \ \_/      / /\  | |   | |_    | |  / /\  | |\ | | | \ | |_) / / \ 
\_\_, |_| \ |_|__ /_/--\  |_|  |_|__ |_|_/     |_|_)  |_|      /_/--\ |_|__ |_|__ \_|_| /_/--\ |_| \| |_|_/ |_| \ \_\_/ """)

def pick_lows(player_name):
    pick_low = input("What do you want the low to be " + player_name + ". ")
    if pick_low.isnumeric():
        print(" ")
        print("Thanks! ")
        print(" ")
        return pick_low
    else:
        print(" ")
        print("Please enter a number")
        print(" ")

def pick_highs(player_name):
    pick_high = input("What do you want the high to be " + player_name + ". ")
    if pick_high.isnumeric():
        print(" ")
        print("Thanks! ")
        print(" ")
        return pick_high
    else:
        print(" ")
        print("Please enter a number")
        print(" ")

def get_guess(current_low, current_high):
    g = (int(current_low) + int(current_high)) // 2
    return g

def get_tries(pick_low, pick_high):
    tries = math.ceil(math.log(((int(pick_high) - int(pick_low))-1),2))
    return tries
                               
def pick_number(player_name, pick_low, pick_high):
    print("Think of a number from " + str(pick_low) + " to " + str(pick_high) + " " + player_name + ".")
    print(" ")
    ready = input("Press enter when you are ready ")

def tell_tries(tries, turns):
    print(" ")
    print("I have " + str(turns) + " out of " + str(tries) + " left. ")
                            

def check_guess(guess):
    print(" ")
    print("Is your number " + str(guess) + ".")
    print(" ")
    r = input("If the guess is correct type 'yes' if too high type 'lower' if too low type 'higher' ")
    r = r.lower()

    if r == 'yes' or r == 'y':
        return 0
    elif r == 'lower' or r == 'l':
        return -1
    elif r == 'higher' or r == 'h':
        return 1
    else:
        print("Please type 'yes' 'lower' or 'higher'. ")
    

def show_result():
    pass

def play_again():
    while True:
        print("I win!")
        
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    
    result = -1

    player_name = get_name()

    pick_low = pick_lows(player_name)

    pick_high = pick_highs(player_name)

    tries = get_tries(pick_low, pick_high)

    turns = (tries - 1)
    
    current_low = pick_low
    
    current_high = pick_high
    
    pick_number(player_name, pick_low, pick_high)
    
    while result != 0:
        guess = get_guess(current_low, current_high)
        
        tell_tries(tries, turns)
        
        result = check_guess(guess)

        if result == -1:
            if turns == 0:
                print(" ")
                print("I think you made a mistake somewhere.")
                result = 0
            else:
                current_high = guess
                turns -= 1

        elif result == 1:
            if turns == 0:
                print(" ")
                print("I think you made a mistake somewhere.")
                result = 0
            else:
                current_low = guess
                turns -= 1

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()

