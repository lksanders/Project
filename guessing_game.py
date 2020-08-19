# This is a guess the number game.
import random

print('Hello what is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secertNumber = random.randint(1,20)

for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secertNumber:
        print('Your guess is to low.')
    elif guess > secertNumber:
        print('Your guess is to high.')
    else:
         break #This is for the correct guess to break.

if guess == secertNumber:
    print('Good job ' + name + '! You guessed the correct number in ' + str(guessesTaken) + ' guesses!')
else:
    print('You are wong you idiot! It was ' + str(secertNumber))          