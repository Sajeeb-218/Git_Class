def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def percent(num1, num2):
    return num1 * (num2 / 100)

def power(num1, num2):
    return num1 ** num2

def main():
    num1 = float(input())
    num2 = float(input())
    operation = input("Enter Operation(+, -, *, /, %, ^): ")
    if operation == "+":
        print("Result: ", add(num1, num2))
    elif operation == "-":
        print("Result: ", sub(num1, num2))
    elif operation == "*":
        print("Result: ", multi(num1, num2))
    elif operation == "/":
        print("Result: ", div(num1, num2))
    elif operation == "%":
        print("Result: ", percent(num1, num2), "%")
    elif operation == "^":
        print("Result: ", power(num1, num2))

main()