
import random

numberProduced=random.randint(1,100)
guessRight=5

while True:
    guess=int(input("Please enter your guess:"))
    if (guess==numberProduced):
        print("Congratulations! You won.")
        break
    elif (guess > numberProduced):
        guessRight-=1
        print("Wrong guess,downgrade your estimate")
        print("Remaining guess",guessRight)
    elif (guess<numberProduced):
        guessRight-=1
        print("Wrong guess,enlarge your guess.")
        print("Remaining guess",guessRight)
    if(guessRight==0):
        print("Your right has expired:",numberProduced) #break komutunu kulladığımız iiçn if yapısı kullanıldı.
        break
        
    else:
         print("Please enter a valid expression.")

