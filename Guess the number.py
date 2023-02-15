import random
import math
#taking inputs
lower= int(input ("Enter Lower bound:- ") )

#Taking inputs
upper = int(input ("Enter Upper bound:- "))


#generating random between the random upper and lower
x = random.randint (lower,upper)
print ("\n\tYou've only" ,
        round(math.log(upper - lower))
        "chances to guess the integer! \n")


#intilaizing the number of guesses
count = 0

#for calculation of minimum number of guesses upon range
while count < math.log(upper - lower + 1, 2):
        count += 1

        #taking guessing number of input
        guess = int (input("Guess a number:- "))

        #condtion testing
        if x == guess:
                print ("congratulation you did it in" )
