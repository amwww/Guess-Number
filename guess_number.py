# Guess Number
import random as rand
import os
import sys
print("Guess Number!")
def gameLoop():
    while True:
        print("Enter Amount of Chances")
        c = input("")
        try:
            c = int(c)
        except:
            print("tbh if you want to play pls cooperate and enter a number lol.")
            continue
        if int(c) < 1:
            print("Awwwww, don't be too harsh on yourself, because there is 0% chance that you will win!")
            continue
        break
    while True:        
        print("Select Range")
        r = input("1-")
        try:
            r = int(r)
        except:
            print("tbh if you want to play pls cooperate and enter a number lol.")
            continue
        if int(r) < 0:
            print("How in the world can u guess 1 to a negative number hahahha!")
            continue
        elif int(r) == 0:
            print("Why are you entering this? NO POINT!!!!!")
            continue
        elif int(r) == 1:
            print("Wow! Imagine guessing a number from 1-1 bruh, no point.")
            continue
        elif int(r) > 1000000000000:
            print("Inf ERROR (definetly not fake lol)")
            continue
        break
    number = rand.randint(1, r)
    print(number)
    times = 0
    print("Keywords:")
    print("/quit: Quit the game.")
    print("/again: play again! Only when the game ended.")
    print("/restart: Restart the game.")
    print("/cheat: Get the answer.")
    print("/range: Get the range")
    while True:
        print("Guess a number or input a command!")
        guess = input("")
        try:
            times += 1
            if times > c:
                print("Oh No! You ran out of chances! Just make it easier or try again!")
                print("Wanna play again? Use /restart or /again! If you don't, type something random!")
                print("Input a command!")
                guess = input("")
                if guess == "/restart":
                    print("Restarting...")
                    gameLoop()
                elif guess == "/range":
                    print("1-" + r)
                else:
                    print("Quitting the qame on behalf of you.")
                break
            if int(guess) == number:
                print("Yes! You got it in " + str(times) + " tries!")
                print("Wanna play again? Use /restart or /again! If you don't, type something random!")
                print("Input a command!")
                guess = input("")
                if guess == "/restart":
                    print("Restarting...")
                    gameLoop()
                elif guess == "/range":
                    print("1-" + r)
                else:
                    print("Quitting the qame on behalf of you.")
                break
            elif int(guess) < number:
                print("Guess BIGGER!!!!!")
            elif int(guess) > number:
                print("Guess smaller!!!!!")
        except:
            if guess == "/quit":
                print("Quiting...")
                break
            elif guess == "/restart":
                print("Restarting...")
                gameLoop()
            elif guess == "/cheat":
                print("Shhhhhhhhhhhhhhhhh!! It's " + str(number) + "!")
            elif guess == "/range":
                print("1-" + r)
            else:
                print("WTF are you inputting? I don't understand!!!!")
gameLoop()
