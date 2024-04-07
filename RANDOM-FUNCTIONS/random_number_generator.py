import random

#use the help function to get information about the random module
#print(help(random))

number = random.randint(1, 100)#this will return a random number between 0 and 100
print(number)

low = 1
high = 20
number = random.randint(low, high)
print(number)

#use the choice method to select a random element from a collection
options = ("rock", "paper", "scissors")
option = random.choice(options) #this choice method will return a random element from the options tuple
print(option)

#use the shuffle method to shuffle the elements of a collection
deck = list(range(1, 53))
print(deck)
random.shuffle(deck)
print(deck)



# create a number guessing game
low = 1
high = 100
guesses = 0
number = random.randint(low, high)  

while True:
    guess = int(input(f"Enter a number between {low} and {high}: "))
    guesses += 1 #increment the number of guesses after each guess

    if guess < number:
        print(f"{guess} is too low.")
    elif guess > number:
        print(f"{guess} is too high.")
    else:
        print(f"Congratulations! You guessed the number in {guesses} guesses.")
        break

print(f"This round took {guesses} guesses.")