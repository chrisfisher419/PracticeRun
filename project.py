def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y

def calculate(first_number, second_number, operator):
    if operator == '+':
        return add(first_number, second_number)
    if operator == '-':
        return subtract(first_number, second_number)
    if operator == '*':
        return multiply(first_number, second_number)
    if operator == '/':
        return divide(first_number, second_number)

if __name__ == '__main__':
    print("This app is a super basic calculator.")

    print("Enter the first number: ")
    first_number = int(input())

    print(" + for addition")
    print(" - for subtraction")
    print(" * for multiplication")
    print(" / for division")
    print("Enter an operator: ")
    operator = input()

    print("Enter the second number: ")
    second_number = int(input())

    result = calculate(first_number, second_number, operator)

    print(str(first_number) + ' ' + operator + ' ' + str(second_number) + ' = ' + str(result))