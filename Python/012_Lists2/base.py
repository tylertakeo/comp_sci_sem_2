import random

y= int(input("How many random number would you like? "))

numbers = []

x= (int(random.randrange(9)))

for y in range(y):
    numbers.append(random.randrange(9))
print(numbers, end="")