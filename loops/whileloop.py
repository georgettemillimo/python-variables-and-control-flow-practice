"""
While condition
    #code to execute
    #fullfilment of the condition

characteristics
    1.Variable affected by the loop
    2. the variable used to fulfill the condition

"""
count = 0
while count < 5:
    print(count)

    #incrementor /decrementor depends on the condition block
    count += 1


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]

]


for row in matrix:
    for element in row:
        print(element, end=' ')
    print()