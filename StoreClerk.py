address = ["Flat Floor Street", "18", "New York"]
pins = {"Mike":1234, "Joe":1111, "Jack":2222}

print(address[0], address[1])

pin = int(input("\nEnter your pin: "))

def find_in_file(f):    
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "\nThat fruit is in the list."
    else:
        return "\nNo such fruit found!"
            
if pin in pins.values():
    fruit = input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("\nIncorrect pin!") 
    print("This info can be accessed only by: ")
    for key in pins.keys():
        print(key)
#This store clerk project is has an issue that is namely the issue of file handling as the file handling part is actually not able to work in this code...
