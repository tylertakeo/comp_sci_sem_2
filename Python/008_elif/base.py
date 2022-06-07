x= input("Enter a number: ")
y= input("Enter another number: ")
z= "="
a= input("Enter an operation: ")
c= int(x)+int(y)
d= int(x)-int(y)
e= int(x)*int(y)
f= int(x)%int(y)

if str(a)=="+":
    print(str(x)+str(a)+str(y)+z+str(c))
elif str(a)=="-":
    print(str(x)+str(a)+str(y)+z+str(d))
elif str(a)=="*":
    print(str(x)+str(a)+str(y)+z+str(e))
elif str(a)=="%":
    print(str(x)+str(a)+str(y)+z+str(f))
else:
    print("Please enter an actual operation next time..")