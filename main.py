from calculator import Calculator

def main():
    calc = Calculator()

    print("Welcome to the calculator!")
    print("Choose operation: add, subtract, multiply, divide")

    op = input("Operation: ").strip().lower()
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == "add":
        result = calc.add(a, b)
    elif op == "subtract":
        result = calc.subtract(a, b)
    elif op == "multiply":
        result = calc.multiply(a, b)
    elif op == "divide":
        result = calc.divide(a, b)
    else:
        print("Unknown operation.")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()