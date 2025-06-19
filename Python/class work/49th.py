A=float(input("Enter first Number"))
O=input("choose operator")
B=float(input("Enter second number"))
if O == "square root":
    print(f"{int(*A)}, of b : {int(B*B)}")
elif O == "power":
    print(A**B)
#elif O == "/":
  #  print(A/B)
#elif O == "*":
 #   print(A*B)
#elif O == "**":
 #   print(A**B)
else:
    print("please enter valid information")