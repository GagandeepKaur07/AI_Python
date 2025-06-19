A=float(input("Enter first Number"))
O=input("choose operator")
B=float(input("Enter second number"))
if O == "+":
    print(A+B)
elif O == "-":
    print(A-B)
elif O == "/":
    print(A/B)
elif O == "*":
    print(A*B)
elif O == "**":
    print(A**B)
else:
    print("please enter valid information")