h=float(input("Enter your height "))
w=float(input("Enter your weight"))

bmi= w/(h**2)

#bmi //= w/h**2
print(int(bmi))
if bmi <= 16:
    print("you are underweight eat healthy food to boost up your weight and keep healthy")
elif 18.5 < bmi <=24.9 :
    print(" you are normal weight stay healthy")
else:
    print("you are over weight do focus on your health be on diet and loss your weight") 