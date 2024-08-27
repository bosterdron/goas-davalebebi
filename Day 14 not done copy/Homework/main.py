i = 1
while i <= 100:
    if i >= 50 and i <= 60:
        i += 1
        continue
    print(i)
    i += 1


i = 1
total = 0
while total < 50:
    total += i
    print(f"Adding {i}, total is now {total}")
    i += 1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


score = int(input("Enter your score: "))

if 90 <= score <= 100:
    print("Grade A")
elif 80 <= score <= 89:
    print("Grade B")
elif 70 <= score <= 79:
    print("Grade C")
elif 60 <= score <= 69:
    print("Grade D")
else:
    print("Grade F")


age = int(input("Enter your age: "))

if age < 13:
    print("You are kid")
elif 13 <= age < 20:
    print("You are teenager")
else:
    print("You are grown up")
