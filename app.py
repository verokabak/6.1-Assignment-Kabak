def add_numbers(a, b):
    return a + b
def substract_numbers(a, b):
    return a - b

print("This calculator can help you to add or substract numbers")
print("Choose the operation first and then write numbers")

choice = input("Enter 1(add) or 2(substract) to choose: ")
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
else:
    print("Not valid. Choose 1 or 2.")