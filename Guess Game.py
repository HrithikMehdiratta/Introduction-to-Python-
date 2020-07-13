import random

x= random.randint(1,100)

print(" Welcome to my Guess Game")
print(" I am thinking of a number between 1 to 100")
print(" Lets us see how many guesses it takes you to guess the number")
print(" Best of Luck")

guesses=[0]

while True:
    guess= int(input(" What is your Guess "))
    
    if guess<1 or guess>100:
        print(" Out of Bounds ")
        continue
        
    if guess == x:
        print(f"Congratulations! You guessed the number in {len(guesses)} Guesses")
        break
        
    guesses.append(guess)
    
    if guesses[-2]:
        if abs(x-guess) < abs(x-guesses[-2]) :
            print(" Warmer ")
        else:
            print(" Colder ")
    else:
        if abs(x-guess) <= 10:
            print(" Warm ")
        else:
            print(" Cold ")
