#This script is similar to the original store storeclerk script but was made to use no dependencies of
# a text file and now this script has not text file dependencies in it.

address = ["Flat Floor Street", "18", "New York"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}
fruits = ("pear","apple","orange","mandarin","watermelon","pomegranate","dragonfruit","avocado")

print(address[0], address[1])
pin = int(input("\nEnter your pin: "))
pin = pin.lower()

if pin in pins.values():
    print("Access granted")
    fruit = input("Enter a fruit: ")
    if fruit in fruits:
        print(f"{fruit} is in the list.")
    else:
        print(f"{fruit} is not in the list.")
else:
    print("Access denied.")