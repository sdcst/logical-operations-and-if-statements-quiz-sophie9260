"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
n = input("Enter a number ")
n = float(n)

nn = input("Enter a number ")
nn = float(nn)

question = "Is one of the numbers the hypotenuse of a right triangle?"
answer = input(question)

if answer == "yes":
    c = max(n,nn)
    a = min(n,nn)
    b = (c**2 - a**2)**0.5
    b = round(b,1)
    print(f"The value of the missing side is {b}.")
else:
    h = (n**2 + nn**2)**0.5
    h = round(h,1)
    print(f"The lenght of the hypotenuse is {h}.")