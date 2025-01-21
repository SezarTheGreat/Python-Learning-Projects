#Part 1-Calculate the factorial of a given number.
#Part 2-Find the number of trailing zeros in that factorial.

def fact(n):
    fact = 1
    if n == 0 or n == 1:
        return 1
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact

def trail(n):
    count = 0
    i = 5
    while (n//i != 0):
        count += int(n/i)
        i = i*5
    return count

def main():
    n = int(input("Enter a number: "))
    print(f"The fact is: {fact(n)}")
    print(f"The number of trailing zeros is: {trail(n)}")

if __name__ == "__main__":
    main()