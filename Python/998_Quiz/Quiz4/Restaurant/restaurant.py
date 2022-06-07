import random

mylist= ["arbys","wendys","tacobell"]
alist= ["burger","coke","fries"]
wlist= ["square","pepsi","wedges"]
tlist= ["taco","sprite","salad"]

y= input("Pick a restruant: "+ str(mylist))


if str(y)=="arbys":
    print("arbys menu items: "+ str(alist))
    print("suggested item: "+ str(alist[random.randrange(len(alist))]))
    
elif str(y)=="wendys":
    print("wendys menu items: "+ str(wlist))
    print("suggested item: "+ str(wlist[random.randrange(len(wlist))]))
        
elif str(y)=="tacobell":
    print("tacobell menu items: "+ str(tlist))
    print("suggested item: "+ str(tlist[random.randrange(len(tlist))]))
    
else:
    print("Enter one of the retraunts next time..")