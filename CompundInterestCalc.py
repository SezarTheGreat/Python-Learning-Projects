principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter the principple amount: "))
    if principle <=0:
        print("Principle cannot be zero.")

while rate <=0:
    rate = float(input("Enter the rate : "))
    if rate <=0:
        print("Rate cannot be zero.")

while time <=0:
    time = float(input("Enter the time amount: "))
    if time <=0:
        print("Time cannot be zero.")
        
total = principle * pow((1+ rate / 100), time)
print(f"Balance after {time} year/s: Rs.{total:.2f}")