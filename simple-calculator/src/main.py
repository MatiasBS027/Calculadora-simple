from calculator import add, subtract, multiply, divide

def main():
    print("Simple Calculator")
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = add(x, y)
    elif operation == '-':
        result = subtract(x, y)
    elif operation == '*':
        result = multiply(x, y)
    elif operation == '/':
        try:
            result = divide(x, y)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid operation")
        return

    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
    