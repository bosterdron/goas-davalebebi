number1 = float(input("Please enter the first number: "))
number2 = float(input("Please enter the second number: "))

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2 if number2 != 0 else "undefined (division by zero)"

print(f"{number1} + {number2} = {addition}")
print(f"{number1} - {number2} = {subtraction}")
print(f"{number1} * {number2} = {multiplication}")
print(f"{number1} / {number2} = {division}")