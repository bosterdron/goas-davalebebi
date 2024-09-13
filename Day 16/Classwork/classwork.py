# 1) შექმენით ფუნქცია რომელიც დააბრუნებს "Hello world!"ს
def hello_world():
    return "Hello world!"

# Test case
print(hello_world())  # Output: Hello world!

# 2) შექმენით ფუნქცია რომელიც დააბრუნებს "Hello (person name)"ს
def hello_person(name):
    return f"Hello {name}!"

# Test case
print(hello_person("John"))  # Output: Hello John!

# 3) შექმენით ფუნქცია რომელიც დააბრუნებს 2 რიცხვის ნამრავლს
def multiply(a, b):
    return a * b

# Test case
print(multiply(3, 4))  # Output: 12

# 4) შექმენით ფუნქცია რომელიც დააბრუნებს 3 რიცხვის ჯამს
def sum_three(a, b, c):
    return a + b + c

# Test case
print(sum_three(1, 2, 3))  # Output: 6

# 5) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს მომხმარებლის ასაკს და გამოიტანს სრულწლოვანია თუ არა
def is_adult(age):
    if age >= 18:
        return "სრულწლოვანი"
    else:
        return "არ არის სრულწლოვანი"

# Test case
print(is_adult(20))  # Output: სრულწლოვანი
print(is_adult(15))  # Output: არ არის სრულწლოვანი

# 6) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს მომხმარებლის ქულას (range(1, 100)'ში) და გამოუტანს ჩააბარა თუ არა (ჩაბარებული აქვს თუ ქულა 80'ზე მეტია)
def did_pass(score):
    if score > 80:
        return "ჩააბარა"
    else:
        return "ვერ ჩააბარა"

# Test case
print(did_pass(85))  # Output: ჩააბარა
print(did_pass(75))  # Output: ვერ ჩააბარა

# 7) დახაზეთ 4 კვადრატი იგივენაირად როგორც მე დავხაზე კლასში, გამოიყენეთ for loopები და ფუნქციები.
from turtle import *

# ფუნქცია კვადრატის დასახაზად
def draw_square(size):
    for _ in range(4):
        forward(size)
        right(90)

# ძირითადი ციკლი 4 კვადრატის დასახატად
for _ in range(4):
    draw_square(100)
    right(90)  # თითო კვადრატის დასრულების შემდეგ მიმართულების შეცვლა

# ტერტლ გრაფიკის ფანჯრის დახურვა
exitonclick()
