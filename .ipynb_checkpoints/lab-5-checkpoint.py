import random as rand
name = input("What is your name? ")
age = int(input("Enter your age: "))

print("Hello, " + name[::-1] + " who is " + str((age * 1.5)) + " years old.")