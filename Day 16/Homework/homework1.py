# 2) შექმენით ფუნქცია რომელიც არგუმენტებად მიიღებს range()'ის არგუმენტებს (start'ს და end'ს) და გამოატანინეთ რიცხვები პირველი რიცხვიდან მეორე რიცხვამდე for loop'ის მეშვეობით
def print_range(start, end):
    for i in range(start, end + 1):
        print(i)

# Test case
print_range(1, 5)  # Output: 1 2 3 4 5

# 3) შექმენით ფუნქცია რომელიც არგუმენტებად მიიღებს სახელს, გვარს, ასაკს და აკადემიას. გამოატანინეთ შემდეგი წინადადება: My name is ..., my surname is ..., I study in ....
def introduce(name, surname, age, academy):
    print(f"My name is {name}, my surname is {surname}, I am {age} years old, I study in {academy}.")

# Test case
introduce("giorgi", "chaduneli", 15, "Goal Orinated Academy")  
# Output: My name is John, my surname is Doe, I am 15-16 years old, I study in Goal Orinated Academy

# 4) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სახელს და გვარს და გამოიტანს მისალმებას
def greet(name, surname):
    print(f"Hello, {name} {surname}!")

# Test case
greet("giorgi", "chaduneli")  # Output: Hello, giorgi chaduneli

# 5) შექმენით ფუნქცია რომელიც დააბრუნებს 2 რიცხვის ჯამს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს
def sum_two_numbers(a, b):
    return a + b

# Test case
result = sum_two_numbers(5, 10)
print(result)  # Output: 15

# 6) შექმენით ფუნქცია რომელიც დააბრუნებს 3 რიცხვის ნამრავლს, შემდეგ კი დაბრუნებული მნიშვნელობა მიანიჭეთ ცვლადს
def multiply_three_numbers(a, b, c):
    return a * b * c

# Test case
result = multiply_three_numbers(2, 3, 4)
print(result)  # Output: 24

# 7) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს საჭმელების list'ს და გამოიტანს ყველას ცალ-ცალკე
def print_foods(foods):
    for food in foods:
        print(food)

# Test case
foods_list = ["Pizza", "Burger", "Salad", "Pasta"]
print_foods(foods_list)
# Output: 
# Pizza
# Burger
# Salad
# Pasta
