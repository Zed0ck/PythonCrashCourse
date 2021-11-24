# Lottery
from random import choice

lotteries = ['a', 'f', 'r', 'q', 1, 6, 42, 24, 2, 15, 25, 33, 31, 7]
first_up = choice(lotteries)
second_up = choice(lotteries)
third_up = choice(lotteries)
fourth_up = choice(lotteries)

print("Any ticket matching these four numbers or letters win!")
print(f"\t{first_up}")
print(f"\t{second_up}")
print(f"\t{third_up}")
print(f"\t{fourth_up}")