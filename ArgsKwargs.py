# *args = allows you to pass a variable number of arguments to a function
# **kwargs = allows you to pass a variable number of keyword arguments to a function 

#*args example
#def display_name(*args):
#    for arg in args:
#        print(arg,end = " ")

#display_name("Dr.","Spongebob","Harold","Squarepants")

#**kwargs example
#def print_address(**kwargs):
#    for key,value in kwargs.values():
#        print(f"{key}: {value}")
    

#print_address(street = "Classic Lane",city = "Happytown",state = "UK",zip = "201301")


#Exercise 1
def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg,end = " ")
    print()
    
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('pobox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')}")
    

shipping_label("Dr.","Spongebob","Squarepants","III",
               street = "123 Classic lane",city ="Happy State",apt = "1001",pobox="PO:#1001",state = "UK",Zip = "201301")
