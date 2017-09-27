import random
import math

#config
low = 1
high = 100
limit = math.ceil(math.log(100, 2))

#helper functions
def show_start_screen():
    print("""   _____                               _   _                 _               
  / ____|                             | \ | |               | |              
 | |  __ _   _  ___  ___ ___    __ _  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|  / _` | | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \ | (_| | | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/  \__,_| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  """)

def show_credits():
    print("""               __     _                
 /|/| _ _/_   / _)   /_| /_ '_   _/_   
/   |(/(/(-  /(_)(/ (  |((-/(//)(// () 
                 /       _/            """)

def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +". You have " + str(limit) + " tries!")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print(" ")
        print("You guessed too low.")
    elif guess > rand:
        print(" ")
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print(" ")
        print("You win!")
        print(" ")
    else:
        print(" ")
        print("You ran out of tries! The number was " + str(rand) + ".")
        print(" ")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()
        
        print(" ")
        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")
            print(" ")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
