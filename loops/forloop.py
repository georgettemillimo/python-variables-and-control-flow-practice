fruits = ["apple", "banana", "cherry"]
print(len(fruits))


def convert_Caps(fruit):

    #logic to make each print out caps
    print("In function",fruit)
    return fruit.upper()

for fruit in fruits:
    print(fruit)
    print (convert_Caps(fruit))

##range method range (stop) mandaory / range(start, stop, step)

for i in range(1,11,2): #starts at 1 steps 2 times upto 10
    print(i)

for i in range(15, 0, -2):  # starts at 1 steps 2 times upto 10
    print(i)

