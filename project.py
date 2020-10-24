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

result = 0

if operator == '+':
    result = first_number + second_number
if operator == '-':
    result = first_number - second_number
if operator == '*':
    result = first_number * second_number
if operator == '/':
    result = first_number / second_number

print(str(first_number) + ' ' + operator + ' ' + str(second_number) + ' = ' + str(result))

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
