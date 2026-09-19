
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    op = input("Choose an operator (+, -, *, /): ")
except ValueError:
    print("This is not a number")
except ZeroDivisionError:
    print("Enter a proper number")


if op == "+":
    print(add(num1, num2))
  
elif op == "-":
    print(sub(num1, num2))
  
elif op == "*":
    print(mult(num1, num2))
  
elif op == "/":
    print(divide(num1, num2))
    