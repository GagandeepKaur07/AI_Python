# Task 1: Implementation of math Module 
import math
print("Square root of 25 :",math.sqrt(25))
print("Factorial of 5:",math.factorial(5))
print("Value of pi:",math.pi)
print("cosine of 45 degree",math.cos(math.radians(45)))

# Task 2  Implementation of datetime Module
import datetime
now= datetime.datetime.now()
print("Current date and time:",now)

d=datetime.date(2024,8,27)
print("specific date :",d)

delta=now-datetime.datetime(2024,1,1)
print("Days since January 1, 2024",delta.days)

formatted_dates =now.strftime("%Y-%m-%d %H:%M:%S")
print("formatted",formatted_dates)
