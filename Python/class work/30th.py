p = float(input("Enter Principal:"))
r = float(input("Enter Rate:"))
t = float(input("Enter Time:"))
I = r/t
A = (p*(1+I)**t)
print("The compound Intrest is ", A)
