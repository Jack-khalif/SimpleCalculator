num1=float(input("First Number:"))
operation=input("Mathematical operation:")
num2=float(input("Second Number:")
)

if operation == "+":
    result = num1 + num2
elif operation =="-":
    result = num1 - num2
elif operation =="*":
    result = num1 * num2
elif operation =="/":
    result = num1 / num2
else:
    result = "invalid operation"

#print the result
print(f"{num1}{operation}{num2}={result}")
