import random
word_list=[]
with open('allow_wordle.txt') as f:
   for line in f:
    l= line.strip()
    print(l)
    word_list.append(l)

num = random.randrange(12972)
answer= word_list[num]
print(answer)

for i in range(0,6):
    guess= input("Guess a word!")
    if guess == answer:
        print("You Won!!")
        break
    else:
        print("Guess again!")