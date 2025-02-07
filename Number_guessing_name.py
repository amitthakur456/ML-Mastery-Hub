import math

def scientific_calculator():
    print("Scientific Calculator")
    print("Available Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (√)")
    print("7. Logarithm (log)")
    print("8. Trigonometric Functions (sin, cos, tan)")
    
    choice = input("Enter the operation number: ")

    if choice in ["1", "2", "3", "4", "5"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "1":
            print(f"Result: {num1 + num2}")
        elif choice == "2":
            print(f"Result: {num1 - num2}")
        elif choice == "3":
            print(f"Result: {num1 * num2}")
        elif choice == "4":
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Division by zero!")
        elif choice == "5":
            print(f"Result: {num1 ** num2}")

    elif choice == "6":
        num = float(input("Enter the number: "))
        if num >= 0:
            print(f"Result: {math.sqrt(num)}")
        else:
            print("Error: Cannot calculate square root of a negative number.")

    elif choice == "7":
        num = float(input("Enter the number: "))
        if num > 0:
            print(f"Result: {math.log(num)}")
        else:
            print("Error: Logarithm undefined for non-positive values.")

    elif choice == "8":
        angle = float(input("Enter the angle in degrees: "))
        radians = math.radians(angle)
        print(f"sin({angle}) = {math.sin(radians)}")
        print(f"cos({angle}) = {math.cos(radians)}")
        print(f"tan({angle}) = {math.tan(radians)}")

    else:
        print("Invalid choice!")

# Run the calculator
scientific_calculator()
