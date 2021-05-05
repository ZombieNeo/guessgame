from random import *


num = randint(1,10)
score = 0
while True:
    guess = int(input("GUESS "))
    if guess < num:
        print("HIGHER ")
    if guess > num:
        print("LOWER ")
    if guess == num:
        print(" you win")
        score = score + 1
        print(score)
