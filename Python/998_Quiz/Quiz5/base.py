x = input("Use a sentence to tell me your favorite number! Ex. My favorite number is 23! ")
y = input("What is your age: ")

a=0
b=1

mylist = []
for i in range(0,len(x)):    
    if x[a:b] == "0":
        mylist.append("0")
    elif x[a:b] == "1":
        mylist.append("1")
    elif x[a:b] == "2":
        mylist.append("2")
    elif x[a:b] == "3":
        mylist.append("3")
    elif x[a:b] == "4":
        mylist.append("4")
    elif x[a:b] == "5":
        mylist.append("5")
    elif x[a:b] == "6":
        mylist.append("6")
    elif x[a:b] == "7":
        mylist.append("7")
    elif x[a:b] == "8":
        mylist.append("8")
    elif x[a:b] == "9":
        mylist.append("9")
    a=a+1
    b=b+1

print(mylist)
    

