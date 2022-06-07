mynumbers = [6,9,32,28,15,22,3,18]

minimum = mynumbers[0]
maximum = mynumbers[0]

for x in mynumbers:
    if x > maximum:
        maximum=x
    
for x in mynumbers:
    if x < minimum:
        minimum=x
    
avg = 0
for i in range(0, len(mynumbers)):
    avg= avg+mynumbers[i]
avg=avg/len(mynumbers)
print("Average: " + str(avg))

print("maximimum:", maximum )
print("mimimum:", minimum )
    
    
