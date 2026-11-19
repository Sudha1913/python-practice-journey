print("BASIC CALCULATOR")
num1=float(input("Enter the first number:\n"))
operator=input("Enter the operator(+,-,*,/):")
if (operator!="+" and operator!="-" and operator!="*" and operator!="/"):
    print("Invalid operator. Please enter +, -, *, or /.")
else:
    num2=float(input("Enter the second number:\n"))
    if(operator=="+"):
        print(num1+num2)
    elif(operator=="-"):
        print(num1-num2)
    elif(operator=="*"):
        print(num1*num2)
    elif(operator=="/"):
        if(num2==0):
            print("Error: Division by zero is not allowed.")
        else:
            print(num1/num2)
