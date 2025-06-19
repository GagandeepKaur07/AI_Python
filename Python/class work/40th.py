N=input("Enter your Name")
p=float(input("Enter your Physics Marks"))
c=float(input("Enter your chemisrty Marks"))
m=float(input("Enter your Maths Marks"))
h=float(input("Enter your Hindi Marks"))
e=float(input("Enter your English Marks"))
pr=float(input("enter your Participation Marks"))
print(N)
total=p+c+m+h+e
print(f"{N } your Marks is {total}")
per=total/5
print(f"Your Percentage is : {per}")
if per > 85 and pr>90:
    print("student qualifies for a special award ")
else:
    print("No award for you keep it up for the next time ")

