import random
heads = 0
tails = 0

for x in range(0, 5001): 
    coin = round(random.random())
    
    if x == 0: # oddly enough attempt zero shouldn't exist. Sooo yeah.
        if coin == 0: # heads
            heads += 1
            print "Attempt #", x + 1, ": Throwing a coin... It's a head! ... Got ", heads, "Head(s) and", tails, "Tail(s) so far"
        elif coin == 1: # tails
            tails += 1
            print "Attempt #", x + 1, ": Throwing a coin... It's a tail! ... Got ", heads, "Head(s) and", tails, "Tail(s) so far"
    else:
        if coin == 0: # heads
            heads += 1
            print "Attempt #", x, ": Throwing a coin... It's a head! ... Got ", heads, "Head(s) and", tails, "Tail(s) so far"
        elif coin == 1: # tails
            tails += 1
            print "Attempt #", x, ": Throwing a coin... It's a tail! ... Got ", heads, "Head(s) and", tails, "Tail(s) so far"
print "Ending the program, Thank you!"