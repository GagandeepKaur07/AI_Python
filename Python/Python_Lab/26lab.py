month=input("enter the month name :")
if month == "january" or month== "march" or month == "may" or month == "july" or month == "august" or month == "october" or month == "december":
    days =31
elif month == "april" or month == "june" or month == "september" or month == "november":
    days=30
elif month == "february":
    days = 28 or 29
else:
    days= "invalid month name"

print(f"the number of days in the month {month.capitalize()} is : {days}")