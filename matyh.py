try:
    a = float(input("Enter First number: "))
    b = float(input("Enter Second number: "))

    print(f"Addition of two numbers: {a + b}")
    print(f"Subtraction of two numbers: {a - b}")
    print(f"Multiplication of two numbers: {a * b}")
    print(f"Division of two numbers: {a / b}")
except Exception as e:
    print(f"An error occurred: {e}")
