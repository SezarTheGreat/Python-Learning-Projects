temperatures = int(input("Enter a temperature: "))
def writer(temperature):
    with open("Text.txt","w") as file:
        for c in temperature:
            if c>273.15:
                f=c*9/5+32
                file.write(str(f)+ "\n")
writer(temperatures)