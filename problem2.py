
import random

def guess_the_number(wins, lost):
    number = random.randint(1, 100)
  #  print (number)
    guess = input("Enter a number from 1 to 100: ")
    
    while guess!=str(number):
        if(guess=="exit"):
            return
        if guess=="give up":
            print("You lost")
            break
        elif int(guess)>number:
            guess = input ("Enter a lower number or give up : " )
        else:
            guess = input("Enter a higher number or give up : ")
        
    if guess != "give up" :      
        print ("You won!")
        wins+=1
    else:
        lost+=1

    print ( str(wins)+" : " + str(lost))
    guess_the_number(wins,lost)

    return 

guess_the_number(0,0)
