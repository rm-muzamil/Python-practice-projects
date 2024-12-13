import random

def numGuessing():
   randomNum = random.randint(1,100)
   attempts = 0
   print("Guess a number between 1 and 100")
   while True:
       try:
            guessNum = int(input("Guess a number"))
            attempts += 1
            if randomNum > guessNum:
                print("Too, Higher than guessed")
            elif randomNum < guessNum:
                print("Too, Lower than guessed")
            else:
                print("Correct")
                break
       except ValueError:
           print("error")
           
numGuessing()