from random import randint

def roll_d6():
    print(randint(1,6))

def roll_d10():
    print(randint(1,10))

def roll_d20():
    print(randint(1,20))

d6 = 0
d10 = 0
d20 = 0

while d6 != 10:
    d6 += 1 
    roll_d6()

print("\n")
while d10 != 10:
    d10 += 1
    roll_d10()

print("\n")
while d20 != 10:
    d20 += 1
    roll_d20()