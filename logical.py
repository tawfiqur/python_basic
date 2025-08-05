"""
Logical operator
and, or, not
"""
age = int(input("Enter your age: "))
has_license = input("Do you have license? (Y/N): ")

if has_license == "Y" or has_license == "y":
    licence = 1
elif has_license == "N" or has_license == "n":
    licence = 0

if age >= 18 and licence:
    print("You can drive a car")
elif age >= 18 and not licence:
    print("You can't drive a car")
