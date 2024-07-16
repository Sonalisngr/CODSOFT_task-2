def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1: Add(+)")
    print("2: Subtract(-)")
    print("3: Multiply(*)")
    print("4: Divide(/)")

    while True:
        choice = input("Enter choice (+,-,*,/): ")

        if choice in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '/':
                result = divide(num1, num2)
                if result == "Error! Division by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
