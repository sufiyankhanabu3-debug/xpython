# Calculator 
print ("==========Calculator==========")
num1=float(input("Enter First Number: "))
num2=float(input("Enter Second Number: "))
print ("==============================")
print("Addition. +")
print("Subtraction. for -")
print("Multiple. for *")
print("Divide. for /")

op = input("\n Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operation")