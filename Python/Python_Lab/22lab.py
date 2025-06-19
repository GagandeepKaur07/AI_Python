'''#task 1
temp = int(input("Enter Temperature"))
if temp <0:
    print("It is freezing....")

#task 2
num =int(input("Enter a number:"))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#task 3
grade=float(input("Enter your marks :"))
if grade >=90:
    print("Grade A")
elif grade >=80:
    print("Grade B")
elif grade >=70:
    print("Grade C")
else:
    print("Grade f")'''

#task 4
num =int(input("Enter a number : "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print(f"{num} Positive ")
else:
    print(f"{num} is negative")