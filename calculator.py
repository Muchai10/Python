a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = input("Enter a mathematical operator i.e (+ - * /): ")

if c == '+':
    result = a + b
    print(f"{a} + {b} = {result}")
elif c == '-':
    result = a - b
    print(f"{a} - {b} = {result}")
elif c == '*':
    result = a * b
    print(f"{a} * {b} = {result}")
elif c == '/':
    if b == 0:
        print("Error! Division by zero is not allowed")
    else:
        result = a / b
        print(f"{a} / {b} = {result}")
else:
    print("Invalid operator")

