#This is a c homework question in my end sem practical question and I am doing it in python just for fun and also because I got that question wrong :(

num = int(input("Enter a number to check if the following number is a palinindrome or not: "))
original_num = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num //10

if original_num == rev:
    print(f"The number {rev} is a palindrome")
else:
    print(f"The number {rev} is not a palindrome")
