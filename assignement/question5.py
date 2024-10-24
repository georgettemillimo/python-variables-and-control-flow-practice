# Ask the user to input their age
age = int(input("Please Enter your age: "))

# if elif control to determine whether they are a minor, adult, or senior
if age < 18:
    print("Ooops!! You are a minor.")
elif 18 <= age <= 65:
    print("Congratulations..!!! You are an adult.")
else:
    print("Hurray!!! You are a senior.")
