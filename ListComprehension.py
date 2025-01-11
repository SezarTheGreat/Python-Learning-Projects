#List Comprehension: A concise way to create a list in python which is more compact than traditional loops
#                    [expression for value in iterable if condition]

#Traditional loop structure.
doubles = []
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

#List Comprehension structure.
triples = [x * 3 for x in range(1,11)]
quads = [x * 4 for x in range(1,11)]
squares = [x *x for x in range(1,11)]
print(triples)
print(quads)
print(squares)

#List comprehension in strings...
fruits = ["apples","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruits)
print(fruit_chars)

#List comprehension in numbers...
numbers = [1,-2,3,-4,5,-6]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2== 0]
odd_nums = [num for num in numbers if num % 2 == 1]
print(positive_nums)

#grade listing program...
grades = [85,75,45,55,90,51,60,30]
passing_grades = [grade for grade in grades if grade >= 60]
passing_grades = [grade for grade in grades if grade <= 60]