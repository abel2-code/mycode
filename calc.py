#!/usr/bin/env python3

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("Choose an operation to perform")

outcome = 0

while True:
    operation = input("Valid operations are +, -, *, and /\n")

    if operation == '+':
       outcome = num1 + num2
       break
    elif operation == '-':
        outcome = num1 - num2
        break
    elif operation == '*':
        outcome = num1 * num2
        break
    elif operation == '/':
        outcome = num1 / num2
        break
    else: 
        print("Invalid operator")

print(f"{num1} {operation} {num2} = {outcome}")
