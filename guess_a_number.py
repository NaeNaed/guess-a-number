import random

#config
low = 1
high = 100
limit = 10

#helper functions
def get_guess():
    while True:
        guess = input("Take a guess: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("Please enter a number that is positive.")
                  
#start game
rand = random.randint(low, high)
print("I'm thinking of a number from " + str(low) + " to " + str(high) + ".");

guess = -1
tries = 0

#play game
while guess != rand and tries < limit:
    guess = get_guess()
    
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")
        
    tries += 1

#end game
if guess == rand:
    print("You win!")
else:
    print("NANI!? You have no tries left!")

    
