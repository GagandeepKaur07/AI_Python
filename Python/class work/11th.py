# 1 to 50 Question
#1. Write a program to print a grocery list containing five items, each on a new line. Also, display a thank-you message in a separate paragraph.
grocery_list= "1. Sugar\n2. Salt\n3. Flour\n4. Oil\n5. Coffee"
Greeting="Thankyou"
print(grocery_list)
print(Greeting)

print("________________________________________________________________________________________________")
#2.Write a program to calculate and print the total cost of 3 apples, 2 bananas, and 4 oranges if their prices are $2, $1, and $3, respectively.
Apple=3
Banana=2
Oranges=4
Apple*=2
Banana*=1
Oranges*=3
All_fruit=Apple+Banana+Oranges
print("Total cost of Apples:",Apple)
print("Total cost of Bananas:",Banana)
print("Total cost of Oranges:",Oranges)
print(All_fruit)

print("________________________________________________________________________________________________")
#3.Display a message to a user that includes their name and the current year in the format: "Hello [Name], welcome to the year [Year]!".
Name=input("Enter your name:")
Year=input("Year")
print("Hello",Name)
print("Welcome to the year" ,Year)

print("________________________________________________________________________________________________")
#4.Write a program to calculate the area of a circle and include a single-line comment explaining each step.
    #first we take value of Redius.
r=5
    #Than we put the value in the formula of ara of circle.
area=3.14*r**2
    #than print the area fo circle.
print("The area of a circle",area)

print("________________________________________________________________________________________________")
#5.Create a program to calculate the simple interest for given principal, rate, and time values. Use multiple single-line comments to explain the formula.

#first we take Principale ammount
    #principle ammount is 250000
    #Rate is 7
    #Time is 12
    #The formula of simple interest is SI=p*r*t/100
    #first we take values
principle=250000
rate=7
time=12
    #than we put the value in formula
SI=principle*rate*time/100
    #than we display the SI
print("Simple intrest :" ,SI)

print("________________________________________________________________________________________________")
#6.Write a program to print a poem or a paragraph about a favorite memory using triple-quoted string literals.
favorite_memory ='''
In the quiet of the summer's glow,
I wandered where the soft winds blow.
By the lakeside, we stood so still,
Watching time bend to nature's will.

The sun above, a golden hue,
Reflected in the waters too.
We laughed and talked, hearts so free,
The world around us, just you and me.

A memory etched in the softest light,
A moment captured, forever bright.
Though seasons change and years may fly,
That summer day will never die.
'''
print(favorite_memory)

print("________________________________________________________________________________________________")
#7.Create a program to store a user’s name, age, and favorite color in variables and print them in a formatted sentence.
Name=input("Enter name")
Age=input("Enter age")
Favorite_color=input("Enter favorite color")
print("The user name is :",Name)
print("Age of user is :",Age)
print("Favorite color of user is :",Favorite_color)

print("________________________________________________________________________________________________")
#8.Write a program to calculate the distance between two points (2, 3) and (4, 7) using the distance formula.
a1,b1=2,3
a2,b2=4,7
result=((a2-a1)**2+(b2-b1)**2)**0.5
print("the distance between two points is:",result)

print("________________________________________________________________________________________________")
#Q 10.Write a program to calculate the average age of a group of students and demonstrate implicit type conversion in the calculation.
gagan,deep,bittu,simran,shivani,bhawna = 20 ,30 ,22 ,33 ,40 ,35 
average=gagan+deep+bittu+simran+shivani+bhawna
total=average/6
print(total)

print("________________________________________________________________________________________________")
#11.Create a program that converts a user's input (in string format) into integers and calculates the total sum of three entered numbers.
x=int(input("Enter first number     ;"))
y=int(input("Enter second number     ;"))
z=int(input("Enter third number     ;"))
sum= x+y+z
print("total is ",sum)

print("________________________________________________________________________________________________")
#12.Write a program to calculate the monthly salary of an employee, given their basic pay, allowances (20% of basic), and tax deductions (10% of basic).
emp= 25000
allo=emp*0.20
tax=emp*0.10

total=emp+allo-tax
print(total)

print("________________________________________________________________________________________________")
#13. Write a program where a product's price is updated using assignment operators based on discounts and taxes.
p_price= 30000
dis= p_price*0.20
p_price -= dis
print("Discount",dis)
tax = p_price *0.10
p_price += tax
print("Tax",tax)
print("total is :", p_price)

#14.Write a program to compare the prices of two items and determine which one is more expensive
HP =65000
Acer = 75000

if HP > Acer:
    print("HP :" , HP)
else:
    print("Acer :" , Acer)

#15.Create a program that checks if a student is eligible for a scholarship based on their grade (>=90) and attendance (>=75%).
xyz = input("enter your Name")
mrks = float(input("Enter Your Marks"))
attd = float(input("Enter you Attandance percentage"))

elig= mrks >=90 and attd >=75
print("thank you for information ",xyz, "Scholarship", elig)

#16.Write a program that calculates the result of a binary AND, OR, and XOR operation for two given integers.
a=bin(60)
b=bin(13)
c=a and b
print("Binary C", c)
print("Binary B", b)
print("Binary A", a)

d=a or b

print("Binary D", d)
print("Binary B", b)
print("Binary A", a)

e ={a}^{b}
print("Binary E", e)
print("Binary B", b)
print("Binary A", a)

#Q 17.Write a program to check whether a word exists in a paragraph using the in operator.
favorite_memory=("""In the quiet of the summer's glow,
I wandered where the soft winds blow.
By the lakeside, we stood so still,
Watching time bend to nature's will.

The sun above, a golden hue,
Reflected in the waters too.
We laughed and talked, hearts so free,
The world around us, just you and me.

A memory etched in the softest light,
A moment captured, forever bright.
Though seasons change and years may fly,
That summer day will never die.""")

print(favorite_memory)
print("etched" in favorite_memory)

#Q 18.Write a program that takes the user's height and weight as input and calculates their Body Mass Index (BMI).
h=float(input("Enter your height "))
w=float(input("Enter your weight"))

bmi= w/h**2

bmi //= w/h**2
print(int(bmi))

#Q 19.Write a program to display a receipt format showing items, their quantities, and prices in a neat, tabular format.
list= """Quantity  items\t\t Price(rs)\n 1(ltr)\t  Milk \t\t 65 \t\n 2(kg)    sugar\t\t 80 \t 
 1(kg)\t  Tea \t\t 200 \t\n 2 (gm)\t  Cardamom \t 15\t
 1(ltr)\t  Water \t 20\t\n 3(pckt)  Biscuit  \t 30 \t\n\n Total \t\t\t\'410\'"""
print(list)

#Q 20.Write a program to calculate the total marks and percentage of a student for 5 subjects and display the result.
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

# Q 21.Write a program that checks whether two dates (entered as day, month, year) are the same or different.
date1 = input("enter 1st date that you want to compare")
date2 = input("enter 1st date that you want to compare")
cmp= date1 == date2
print ("the date is:",cmp)

# Q 22.. Write a program that checks whether a store is open based on the day of the week and the time entered by the user.
A=input("Enter day that you want to chech the shop is opened or closed :")
a="monday"
b="tuesday"
c="wednesday"
d="thursday"
e="friday"
f="saturday"
g="sunday"
if A == a or A == b or A == c or A == d or A == e :
    print(A,"Open 10 am to 8 pm")
else:
    print(A,"closed full day ")

# Q 26.Write a program to create a shopping list for a party with at least 7 items. Add a header and footer to the output using string concatenation to make it look like a formal checklist.
header="This is the list for party......"
list= """   Items\t\t\n1. Cake\t\t\n2. Biscuit\t\t\n3. Decoration item\t\t\n4. Namkeen\t\t\n5. plates-glasses\t\t\n6. Chocolates\t\t\n7. Cold-drinks
"""
print(header)
print(list)
footer="No more things need....."
print(footer)

# Q 27.. Calculate the cost of purchasing 5 apples, 3 bananas, and 2 oranges, but this time include a 5% sales tax in the total price. Display the price before and after the tax.
Apple=5
Banana=3
Oranges=2
Apple*=3
Banana*=2
Oranges*=4
All_fruit=Apple+Banana+Oranges
tax=All_fruit+0.5
print("Total cost of Apples:",Apple)
print("Total cost of Bananas:",Banana)
print("Total cost of Oranges:",Oranges)
print("cost without Tax : ",All_fruit)
print("cost after applying Tax : ",tax)

# Q 28.Write a program that asks the user for their first and last name and the current year, then outputs: “Hello [First Name] [Last Name], you’re exploring Python in [Year]!”
f_name=input("Enter your First Name here: ")
l_name=input("Enter your Last Name here: ")
year=input("Enter current Year")
print(f"Hello {f_name} {l_name}, you're exploring Python in {year} ")

# Q 29.Create a program that calculates the volume of a sphere, including a single-line comment for each step. Use the formula \( V = \frac{4}{3} \pi r^3 \), where \( \pi = 3.14 \) and \( r \) is the radius entered by the user.
r=int(input("Enter radious that you want to calculatetheir volume of sphere :"))
form=(4/3)*3.14*r**3 #at first we take radius of sphere from the user then put formula and then we get answer;
print(form)

#Q 30.Write a program to calculate the compound interest (A = P(1 + r/n)\(^{nt}\)) for given principal, rate, time, and number of times interest is compounded annually. Explain the steps using comments.
p=float(input("Enter Principal:"))
r=float(input("Enter Rate:"))
t=float(input("Enter Time:"))
I=r/t
A=(p*(1+I)**t)
print("The compound Intrest is ",A)

# Q 31.. Print a favorite quote or a speech excerpt using triple-quoted string literals. Include a header and footer created using string repetition (e.g., '*' * 20).
head="the poem of Season"
favorite_memory=("""In the quiet of the summer's glow,
I wandered where the soft winds blow.
By the lakeside, we stood so still,
Watching time bend to nature's will.

The sun above, a golden hue,
Reflected in the waters too.
We laughed and talked, hearts so free,
The world around us, just you and me.

A memory etched in the softest light,
A moment captured, forever bright.
Though seasons change and years may fly,
That summer day will never die.""")
print(head)
print(favorite_memory)
footer="conclusion :- The sun above, a golden hue,Reflected in the waters too.We laughed and talked, hearts so free "
print(footer)

#Q 32.Create a program where the user enters their name, city, and dream job. Use formatted strings to output a creative sentence about their aspirations.
name=input("Enter your Name here: ")
city=input("Enter your city here: ")
dreamjob=input("Enter Dream job")
print(f"Hello {name} your city is {city}, and your Dream job is {dreamjob} you can achive it just do hard work and believe in your self. ")

#Q 33.Write a program that calculates the distance between two points entered by the user as coordinates (x1, y1) and (x2, y2). Display the formula as part of the output.
a1= int(input("Enter A1 distance :"))
b1 = int(input("Enter B1 distance :"))
a2= int(input("Enter A2 distance :"))
b2=int(input("Enter B2 distance :"))
form= ((a2-a1)**2+(b2-b1)**2)**0.5
print("((a2-a1)**2+(b2-b1)**2)**0.5 - this is formula we use in this calculation\n")
print( form)

#Q 34.Create a program that stores the names of three cities and their landmarks in variables and formats them into a neat paragraph
city1="Indore"
cl1="Rajwada"
city2="Agra"
cl2="Tajmahal"
city3="Delhi"
cl3="redfort"
print(f"Hello todays information are : \n city 1 {city1} and landmark is {cl1} \n city 1 {city2} and landmark is {cl2} \n city 1 {city3} and landmark is {cl3} \n ")

#Q 35.Write a program that calculates the average marks of five students. Use only implicit type conversion to calculate the result and display it.
gagan,deep,bittu,simran,shivani,bhawna = 20 ,30 ,22 ,33 ,40 ,35 
averagemrks=gagan+deep+bittu+simran+shivani+bhawna
aygM=averagemrks/6
print("the average marks are",aygM)

#Q 36.Create a program that asks the user for four numbers (in string format) and calculates their product after converting them into integers. Display each number's type before and after conversion.
a=float(input("Enter first Number"))
b=float(input("Enter second Number"))
c=float(input("Enter third Number"))
d=float(input("Enter fourth Number"))
p=(a*b*c*d)
print("Before ;",p)
print("after ;",int(p))

#Q 37.Write a program to calculate an employee's annual salary, considering basic pay, allowances (25% of basic), and tax deductions (15% of basic). Output the gross and net salary.
basic_pay= 25000
annual_pay=basic_pay*12
Allowances=basic_pay*0.25
tax=basic_pay*0.15
net_sal=basic_pay+Allowances-tax
print("Allowance",Allowances)
print("annual_pay",annual_pay)
print("net salary",net_sal)

#Q 38.Create a program where the price of a product is increased by a discount first (20%) and then a tax (10%) using appropriate assignment operators.
prod=22000
print(prod)
dis=prod*0.20
prod -=dis
print("D",prod)
tax=prod*0.10
prod += tax
print("T",prod)
print("P T P",prod)

#Q 39.Write a program to compare the prices of three items and determine which one is the cheapest and most expensive.
hp =65000
apple = 75000
acer = 80000

# Cheapest
    
print("Cheapest:-")
if apple < hp and apple < acer:
    print("Apple: ",apple)
elif hp < apple  and hp < acer:
    print("HP: ",hp)
else:
    print("Acer", acer)

# Expensive
print("Expensive:-")
if apple > hp and apple > acer:
    print("Apple: ",apple)
elif hp > apple  and hp > acer:
    print("HP: ",hp)
else:
    print("Acer", acer)


#Q 40.Create a program to check if a student qualifies for a special award if their grades are above 85% and their participation is greater than 90%. Include a clear explanation of the criteria.
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


#Q 41.Write a program to calculate the binary AND, OR, and XOR of three given integers. Display the results along with their binary representations
a= bin(15)
b=bin(30)
b1=bin(45)
c = a and b and b1
d = a or b or b1
e = {a} ^ {b} ^ {b1}
print("A: ",a)
print("B: ",b)
print("B1: ",b1)
print("C: ",c)
print("D: ",d)
print("E: ",e)

#Q 42.Write a program that checks if a specific phrase exists in a given paragraph. The user should provide the paragraph and the phrase to be searched.
para=input("Enter your paragraph")
sear=input("You can search any word from it by typing that word")
if sear in para:
    print("Yes")
else:
    print("data not found")

#Q 43.. Create a program to calculate a user's Body Mass Index (BMI). Display the BMI in a message that includes whether they are underweight, normal, or overweight based on the BMI range.
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

#Q 44.Write a program to display a receipt format that includes the store name, items purchased, quantities, prices, and the total amount due. Use tab characters for alignment.
list= """Store name\titems   Quantity\t Price(rs)\tDue Amount \n\npanchal store   Milk\t 1(ltr)  \t 65 \t\t20\t\t\npandya store\tsugar\t 2(kg)\t\t 80 \t\t30\t 
Pandya store\tTea\t 1(kg) \t\t 200 \t\t100 \nPandya store\tCardamom 2(gm)\t\t 15\t\t -
Pandya store\tWater \t 1(ltr)  \t 20\t\t20\nRamesh kirana\tBiscuit\t 3(pckt)  \t 30 \t\t-\n\nTotal \t\t\t\t\t'410\'\t\t\'170\'"""
print(list)

#Q 45.Calculate and display the percentage and grade of a student in five subjects. Grades should be assigned based on the percentage range: A (>=90%), B (>=80%), C (>=70%), and F (<70%).
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
elif per >80:
    print("B grade")
elif per >70:
    print("C grade")
else:
    print("Fail")

#Q 46.Write a program to check if two dates (entered as day, month, year) are the same or different. Output the dates in a readable format.
date1 = input("enter 1st date that you want to compare")
date2 = input("enter 1st date that you want to compare")
cmp= date1 == date2
print ("the date is:",cmp)
if date1==date2:
    print(date1)
else:
    print(date2, " and ", date1 ," are not same")

#Q 47.Create a program to determine if a store is open based on the user’s input for the current day and time. Assume the store has different timings for weekdays and weekends.
A=input("Enter day that you want to chech the shop is opened or closed :")
a="monday"
b="tuesday"
c="wednesday"
d="thursday"
e="friday"
f="saturday"
g="sunday"
if A == a or A == b or A == c or A == d or A == e :
    print(A,"Open 10 am to 8 pm")
else:
    print(A,"open 12pm-2pm ")

#Q 49.Create a program for a scientific calculator that performs square root, power, and absolute value operations. Allow the user to input the numbers for these calculations.
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

#50.. Write a program to update the prices of three products. If a price is below $20, increase it by 15%; if it's between $20 and $50, increase it by 10%; if it's above $50, increase it by 5%. Display the updated prices.
def update_price(price):
    if price < 20:
        return price * 1.15  # Increase by 15%
    elif 20 <= price <= 50:
        return price * 1.10  # Increase by 10%
    else:
        return price * 1.05  # Increase by 5%
    # List of original prices of three products
prices = [18.99, 35.50, 60.00]
    # Updating prices
updated_prices = [update_price(price) for price in prices]
    # Displaying updated prices
for i, price in enumerate(updated_prices, 1):
    print(f"Updated price of product {i}: ${price:.2f}")









