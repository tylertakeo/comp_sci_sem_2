import random


with open('People.txt') as f:
    for line in f:
        l = line.strip()
        print(l)

with open('Compliment.txt') as f:
    for line in f:
        l = line.strip()
        print(l)


peoplenum= ranom.range(0,len(people_list))
compnum= random.randrange(0,len(comp_list))
print()
print(people_list[peoplenum] + " " + comp_list[compnum])
