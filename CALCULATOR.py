def add(x, y):
    return x + y
def subtract(x, y):
    return x - y    
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

print("=== Simple Calculator ===")
print("Select operation:")
print("1. Add(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. Divide(/)")

op = input("Enter Your Choice (+, -, *, /): ")
Number1 = float(input("Enter first number: "))
Number2 = float(input("Enter second number: "))

if op == '+':
    result = add(Number1, Number2)
elif op == '-':
    result = subtract(Number1, Number2)
elif op == '*':
    result = multiply(Number1, Number2)
elif op == '/':
    result = divide(Number1, Number2)
else:
    result = "Invalid operation selected."
print("Result:", result)
