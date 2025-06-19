N=input("Enter your Name")
p=float(input("Enter your Physics Marks"))
c=float(input("Enter your chemisrty Marks"))
m=float(input("Enter your Maths Marks"))
h=float(input("Enter your Hindi Marks"))
e=float(input("Enter your English Marks"))
print(N)
total=p+c+m+h+e
print(f"{N } your Marks is {total}")
per=total/5
print(f"Your Percentage is : {per}")
if per > 90:
    print("A Grade")
elif per <33 and per>60 :
    print("B grade")
else:
    print("C grade")