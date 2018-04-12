#Coin Tosses
#Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
import random

def coin_toss():
    print "Starting the program..."
    counter = 1
    heads = 0 
    tails = 0 
    while counter <= 5000:
        flip = random.random()
        flip = round(flip)
        if flip == 0: 
            tails += 1
            print "Attempt #",counter,": Throwing a coin... It's a tail! ... Got ",heads," head(s) so far and ",tails," tail(s) so far"
        else:
            heads += 1
            print "Attempt #",counter,": Throwing a coin... It's a head! ... Got ",heads," head(s) so far and ",tails," tail(s) so far"
        counter+=1
    print "Ending the program, thank you!"
  
  
coin_toss()