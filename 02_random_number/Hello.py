import random

x = random.randint(1,6)
y = random.random()

mylist = ["Rock", "Paper", "Scissors"]
z = random.choice(mylist)

cards = [1,2,3,4,5,6,7,8,9,"J","K","Q","A"]
random.shuffle(cards)
print(cards)
