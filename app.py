def add_numbers(a, b):
    return a + b
def substract_numbers(a, b):
    return a - b
def divide_numbers(a, b):
    return a / b

print("This calculator can help you to add, substract or divide numbers")
print("Choose the operation first and then write numbers")

choice = input("Enter 1(add), 2(substract) or 4(divide) to choose: ")
if choice == "1":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print(f"The result is: {result}")
elif choice == "2":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = substract_numbers(num1, num2)
    print(f"The result is: {result}")
elif choice == "4":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = divide_numbers(num1, num2)
    print(f"The result is: {result}")
else:
    print("Not valid. Choose 1, 2 or 4.")