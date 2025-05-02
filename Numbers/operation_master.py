num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input(str("Enter operation (+, -, /, //, %, **): "))




if op == "+":
    print(f"Result: {num1 + num2}")

elif op == "-":
    print(f"Result: {num1 - num2}")

elif op == "*":
    print(f"Result: {num1 * num2}")
    
elif op == "/":
    if num2 != 0:   
        print(f"Result: {num1 / num2}")
    else:  
        print("Error: Division by zero is not allowed.")

elif op == "//":
    if num2 != 0:   
        print(f"Result: {num1 // num2}")
    else:  
        print("Error: Division by zero is not allowed.")
        
elif op == "%":
    if num2 != 0:   
        print(f"Result: {num1 % num2}")
    else:  
        print("Error: Division by zero is not allowed.")
        
elif op == "**":
    print(f"Result: {num1 ** num2}")

else:
    print("Error: Invalid operation. Please enter one of the following: +, -, *, /, //, %, **")
    
    
print("Thank you for using the calculator!")