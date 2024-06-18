def calculator(number1, number2, operat):
    match operat:
        case "+":
            return number1 + number2
        case "-":
            return number1 - number2
        case "*":
            return number1 * number2
        case "/":
            return number1 / number2
        case "_":
            return "Invalid operator!"


num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operator = input("Enter the operator (+, -, *, /): ")
result = calculator(num1, num2, operator)
print("Result:", result)
