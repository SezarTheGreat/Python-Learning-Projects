correct_password = "1234"
name = input("Enter Name: ")
surname=input("Enter Surname: ")
password = input("Enter the password: ")

while correct_password !=password:
    password = input("Wrong Password!\nEnter again: ")
message = "Hi %s %s you are logged in." %(name,surname)
print(message)