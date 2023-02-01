

<!DOCTYPE html>
<html>

<body>
  <h1>Simple Calculator</h1>
  <p>This is a basic calculator program that performs addition, subtraction, multiplication, and division operations.</p>
  
  <h2>Usage</h2>
  <p>To use this calculator, follow these steps:</p>
  <ol>
    <li>Enter the first number</li>
    <li>Enter the second number</li>
    <li>Enter the operator (+, -, *, or /)</li>
  </ol>
  
  <h2>Code</h2>
  <p>Here is the code for the calculator:</p>
  <pre>
  <code>
def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2  
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

result = calculator(num1, num2, operator)
print("Result:", result)
  </code>
  </pre>
  
  <h2>Dependencies</h2>
  <p>This program does not require any additional dependencies or libraries.</p>
  
  <h2>Contact</h2>
  <p>If you have any questions or concerns, please feel free to reach out to us.</p>
</body>
</html>
