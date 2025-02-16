import random
import string

letters = list(string.ascii_lowercase + string.ascii_uppercase)
number = [1,2,3,4,5,6,7,8,9,0]
symbols = list(string.punctuation)

print("Python Password Generator(Although hard pass)")
nr_letters = int(input("How many letters would you like in your password:\n"))
nr_numbers = int(input("How many numbers would you like :\n"))
nr_symbols = int(input("How many symbols would you like :\n"))

password_list = []

for char in range(0,nr_letters):
    password_list.append(random.choice(letters))

for char in range(0,nr_numbers):
    password_list.append(random.choice(number))

for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char