expression = input("Expression: ")
x, y, z = expression.split(" ")

num1 = float(x)
num2 = float(z)

match y:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2

print(f"{result:.1f}")
        
    
