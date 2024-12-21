email = input("Enter your emaik: ")
index = email.index("@")
username = email[0:index]
domain = email[index + 1:]
print(f"Your username is {username} and domain is {domain}.")