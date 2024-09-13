# 2) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
a = 10
b = 5
print(a + b)  # Output: 15

# 3) შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია (ასევე კომენტარის სახით აღწერეთ რა არის კონკატენაცია).
str1 = "Hello"
str2 = "World"
# კონკატენაცია არის ორი ან მეტი სტრინგის შეერთება ერთ სტრინგში
print(str1 + " " + str2)  # Output: "Hello World"

# 4) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)
x = 10
y = 3
result = x / y
print(result)  # Output: 3.3333333333333335
# ახსნა: division ოპერაცია ავტომატურად კონვერტირდება float ტიპში, რასაც ჰქვია "implicit conversion".

# 5) გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი
print(5 == 5)  # True
print(5 != 3)  # True
print(7 > 3)   # True
print(4 < 6)   # True
print(8 >= 8)  # True
print(2 <= 4)  # True

# 6) შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2)
print(5 + 5 == 8 + 2)  # True

# 7) გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა (სულ უნდა იყოს რვა, გაიხსენეთ ნასწავლიდან)
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# 8) შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი
print(5 > 3 and 2 < 4)   # True
print(10 == 10 or 5 < 3) # True
print(8 != 8 and 4 > 2)  # False
print(7 <= 7 or 9 > 10)  # True
print(not (6 < 5))       # True

# 9) შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
for i in range(1, 11):
    print(i)

# 10) შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
for num in numbers:
    sum_of_numbers += num
print(sum_of_numbers)  # Output: 15

# 11) შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
string = "Hello, World!"
for char in string:
    print(char)

# 12) შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
i = 1
while i <= 10:
    print(i)
    i += 1

# 13) შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
i = 1
while i <= 100:
    if 50 <= i <= 60:
        i += 1
        continue
    print(i)
    i += 1

# 14) შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.
i = 1
total = 0
while total < 50:
    total += i
    i += 1
print(total)  # Output: 55 (as it exceeds 50 after adding 10)

# 15) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაპრინტავს ეს რიცხვი თუ იყოფა 3ზე ან 5ზე ან ორივეზე
def check_divisibility(num):
    if num % 3 == 0 and num % 5 == 0:
        print(f"{num} იყოფა როგორც 3ზე, ასევე 5ზე")
    elif num % 3 == 0:
        print(f"{num} იყოფა 3ზე")
    elif num % 5 == 0:
        print(f"{num} იყოფა 5ზე")
    else:
        print(f"{num} არ იყოფა არც 3ზე და არც 5ზე")

# Test case
check_divisibility(15)  # Output: 15 იყოფა როგორც 3ზე, ასევე 5ზე

# 16) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა გამოითვალე ამ სიის საშუალო არითმეტიკული.
def average(numbers):
    return sum(numbers) / len(numbers)

# Test case
print(average([1, 3, 4, 5, 2]))  # Output: 3.0

# 17) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე sting,თქვენი მოვალეობაა ყოველ მეორე ინდექსე მყოფი ასო გახადოს დიდი (upper).
def alternate_upper(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i].lower()
    return result

# Test case
print(alternate_upper("hello"))  # Output: HeLlO

# 18) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა შექმნათ ახალი სია და ამ ახალ სიაში გამოიტანოთ ყოველი რიცხვის კვადრატი (append).
def square_numbers(numbers):
    squared = []
    for num in numbers:
        squared.append(num ** 2)
    return squared

# Test case
print(square_numbers([3, 12, 5, 2, 6]))  # Output: [9, 144, 25, 4, 36]