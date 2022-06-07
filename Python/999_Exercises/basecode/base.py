x= input("How many items would you like to buy? ")

a= int(0)

for a in range(0,int(x)):
    y= input("What item are you buying? ")
    z= int(input("How much was that item? "))
    a= a+z
    print("Thanks for buying " + y)
    
print("The total amount is "+ str(a))
    