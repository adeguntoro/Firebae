import random

x = random.randint(0,10)
y = 7
while x != y:
    print(x)   #Print old (non-7) random number
    x = random.randint(0,10)  #pick a new number.  I hope it's 7 so we can end this madness

print("You found {0}.  Congrats.  Go have a beer.".format(y))
