"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print 
out a message of congratulations to the winner, 
and ask if the players want to start a new game)"""

a = raw_input("Rock,paper,scissors ")
b = raw_input("Rock,paper,scissors ")
if a=="rock" and b =="scissors":
    print "player a wins"
elif a=="rock" and b =="paper":
    print "player b wins"
elif a=="rock" and b=="rock":
    print "no one wins"  
elif a =="paper" and b =="paper": 
    print "no one wins" 
elif a=="paper" and b=="rock":
    print "player a wins"
elif a=="paper" and b=="scissors":
    print "player b wins"
