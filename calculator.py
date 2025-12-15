import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def percentage(a, b):
    return (a / b) * 100

def factorial(a):
    return math.factorial(a)

def trigonometry(choice, angle):
    rad = math.radians(angle)
    if choice == 1:
        return math.sin(rad)
    elif choice == 2:
        return math.cos(rad)
    elif choice == 3:
        return math.tan(rad)

while True:
    print("\n--- Multifunction Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Factorial")
    print("9. Trigonometry")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Calculator Closed")
        break

    elif choice in [1, 2, 3, 4, 5, 7]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(a, b))
        elif choice == 2:
            print("Result:", subtract(a, b))
        elif choice == 3:
            print("Result:", multiply(a, b))
        elif choice == 4:
            print("Result:", divide(a, b))
        elif choice == 5:
            print("Result:", power(a, b))
        elif choice == 7:
            print("Result:", percentage(a, b), "%")

    elif choice == 6:
        a = float(input("Enter number: "))
        print("Result:", square_root(a))

    elif choice == 8:
        a = int(input("Enter number: "))
        print("Result:", factorial(a))

    elif choice == 9:
        print("1. Sin")
        print("2. Cos")
        print("3. Tan")
        t = int(input("Choose function: "))
        angle = float(input("Enter angle in degrees: "))
        print("Result:", trigonometry(t, angle))

    else:
        print("Invalid choice")
