x= input("Please enter line length: ")
y= input("Would you like your line to be horizontal or vertical: ")

if str(y)=="horizontal":
    for x in range(0,int(x)):
        print("*", end="")
    
elif str(y)=="vertical":
    for x in range(0,int(x)):
        print("*")
else:
    print("Enter vetical or horizontal next time..")