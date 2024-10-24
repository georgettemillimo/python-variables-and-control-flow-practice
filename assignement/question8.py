# user input for the on the number of the day
dayNo = int(input("Enter a number (1-7): "))

# if elif statements to check the corresponding day of the week
if dayNo == 1:
    print("Sunday")
elif dayNo == 2:
    print("Tuesday")
elif dayNo == 3:
    print("Wednesday")
elif dayNo == 4:
    print("Thursday")
elif dayNo == 5:
    print("Friday")
elif dayNo == 6:
    print("Saturday")
elif dayNo == 7:
    print("Monday")
else:
    print("Invalid input")
