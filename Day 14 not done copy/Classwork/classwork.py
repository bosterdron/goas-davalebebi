list1 = [1]
list2 = [2, 3]
list3 = [4, 5, 6]
list4 = [7, 8, 9, 10]
list5 = [11, 12, 13, 14, 15]

print("List 1:", list1[0], list1[-1])
print("List 2:", list2[0], list2[1], list2[-1], list2[-2])
print("List 3:", list3[0], list3[1], list3[2], list3[-1], list3[-2], list3[-3])
print("List 4:", list4[0], list4[1], list4[2], list4[3], list4[-1], list4[-2], list4[-3], list4[-4])
print("List 5:", list5[0], list5[1], list5[2], list5[3], list5[4], list5[-1], list5[-2], list5[-3], list5[-4], list5[-5]) 

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sum_second_last = numbers[1] + numbers[-1]
difference_second_last = numbers[-2] - numbers[0]
product_fifth_sixth = numbers[4] * numbers[5]

print("Sum of second and last element:", sum_second_last)
print("Difference of second last and first element:", difference_second_last)
print("Product of fifth and sixth elements:", product_fifth_sixth)


my_list = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original list:", my_list)

my_list[2] = "grape"
my_list[3] = "fig"
print("Modified list:", my_list)