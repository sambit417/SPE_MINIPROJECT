#!/usr/bin/python3
import math

def square_root(num):
    result = math.sqrt(num)
    print(result)
    return result

def factorial(num):
    result = math.factorial(num)
    print(result)
    return result

def natural_logarithm(num):
    result = math.log(num, math.e)
    print(result)
    return result

def power_function(base, exponent):
    result = math.pow(base, exponent)
    print(result)
    return result

def main():
    print("Choose any of these options 1/2/3/4 to calculate:")
    print("1. Square Root of a number")
    print("2. Factorial of a number")
    print("3. Natural Logarithm of a number")
    print("4. Power Function of a number")

    choice = int(input("Enter your choice"))

    if choice == 1:
        num = float(input("Enter a number: "))
        if num<0:
            print ("invalid number")
        else:
            square_root(num)
    elif choice == 2:
        num = int(input("Enter a number: "))
        factorial(num)
    elif choice == 3:
        num = float(input("Enter a number: "))
        natural_logarithm(num)
    elif choice == 4:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        power_function(base, exponent)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

