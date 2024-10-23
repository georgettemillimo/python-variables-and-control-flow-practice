# user input for the lengths of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Determine the type of triangle
if side1 == side2 == side3:
    print("This triangle is Equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("This triangle is Isosceles.")
else:
    print("This triangle is Scalene.")
