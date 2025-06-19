#1. Write a Python program to check if a given number is positive, negative, or zero.  
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("__________________________________________________________________________________")
#2. Write a program to determine whether a given integer is even or odd.  
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

print("__________________________________________________________________________________")
#3. Create a program to find the maximum of two numbers using conditional statements.  
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The maximum number is {num1}.")
elif num2 > num1:
    print(f"The maximum number is {num2}.")
else:
    print("Both numbers are equal.")

print("__________________________________________________________________________________")
#4. Write a Python script to check whether a person is eligible to vote based on their age (18 years or older).  
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("__________________________________________________________________________________")
#5. Write a program to determine whether a given character is a vowel or a consonant.  
char = input("Enter a character: ")
if char in 'a,e,i,o,u':
    print(f"The character '{char}' is a vowel.")
elif char :
    print(f"The character '{char}' is a consonant.")
else:
    print("Invalid input. Please enter a letter.")

print("__________________________________________________________________________________")
#6. Check if a number is divisible by both 5 and 11. Print an appropriate message.  
number = int(input("Enter a number: "))
if number % 5 == 0 and number % 11 == 0:
    print(f"The number {number} is divisible by both 5 and 11.")
else:
    print(f"The number {number} is not divisible by both 5 and 11.")

print("__________________________________________________________________________________")
#7. Write a program to compare three numbers and display the largest one.  
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}.")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}.")
else:
    print(f"The largest number is {num3}.")

print("__________________________________________________________________________________")
#8. Write a program to classify a number as "small" if it’s less than 10 and "large" if it’s greater than 10.  
number = float(input("Enter a number: "))
if number < 10:
    print("The number is small.")
elif number > 10:
    print("The number is large.")
else:
    print("The number is exactly 10.")

print("__________________________________________________________________________________")
#9. Write a program to check if a year is a leap year.  
year = int(input("Enter a year: "))
if year % 4 == 0 :
    print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")

print("__________________________________________________________________________________")
#10. Take a user input for temperature and display "Hot" if the temperature is above 30°C and "Cold" otherwise.  
temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("Hot")
else:
    print("Cold")

print("__________________________________________________________________________________")
#11. Write a program to determine whether a given number is a multiple of 3 or a multiple of 7.  
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 7 == 0:
    print(f"The number {number} is a multiple of both 3 and 7.")
elif number % 3 == 0:
    print(f"The number {number} is a multiple of 3.")
elif number % 7 == 0:
    print(f"The number {number} is a multiple of 7.")
else:
    print(f"The number {number} is neither a multiple of 3 nor 7.")

print("__________________________________________________________________________________")
#12. Write a program to display the grade of a student based on their marks:(- Marks >= 90: A ,- Marks >= 80: B ,- Marks >= 70: C,- Marks >= 60: D ,- Marks < 60: F)  
marks = float(input("Enter the marks of the student: "))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"The grade of the student is: {grade}")

print("__________________________________________________________________________________")
#13. Write a program to calculate and display the absolute difference between a given number and 21. If the number is greater than 21, return double the absolute difference.  
def absolute_difference(num):
    diff = abs(num - 21)  # Calculate the absolute difference between the number and 21
    if num > 21:
        return diff * 2  # If the number is greater than 21, return double the difference
    return diff
number = int(input("Enter a number: "))  # Input a number
result = absolute_difference(number)  # Call the function with the input number
print(f"The result is: {result}")  # Display the result

print("__________________________________________________________________________________")
#14. Write a Python program to check if a given triangle is equilateral, isosceles, or scalene based on its side lengths
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a == b == c:
    print("Equilateral Triangle") 
elif a == b and b == c or a == c:
    print("Isosceles Triangle")  
elif a!=b and b!=c or a!=c:
    print("Scalene Triangle")  
else:
    print("Not a valid triangle")

print("__________________________________________________________________________________")
#15. Create a program that checks if a given three-digit number is an Armstrong number. (Hint: 153 is Armstrong because \(1^3 + 5^3 + 3^3 = 153\)). 
num = int(input("Enter a three-digit number: "))
    # Calculate the sum of the cubes of its digits
armstrong_sum = sum(int(digit)**3 for digit in str(num))
    # Check if the number is an Armstrong number
if num == armstrong_sum:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.") 

print("__________________________________________________________________________________")
#16. Write a Python program to check whether a given character is uppercase, lowercase, a digit, or a special character.  
char = input("Enter a character: ")
if char.isupper():
    print(f"{char} is an uppercase letter.")
elif char.islower():
    print(f"{char} is a lowercase letter.")
elif char.isdigit():
    print(f"{char} is a digit.")
else:
    print(f"{char} is a special character.")

print("__________________________________________________________________________________")
#17. Write a program to accept two numbers and print "Equal" if they are the same, otherwise print "Not Equal."  
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 == num2:
    print("Equal")
else:
    print("Not Equal")

print("__________________________________________________________________________________")
#18. Write a program to check if the given day number (1–7) corresponds to a weekday or a weekend. (e.g., 1 = Monday, 7 = Sunday).  
day_number = int(input("Enter a day number (1-7): "))
if day_number == 1:
    print("Monday - Weekday")
elif day_number == 2:
    print("Tuesday - Weekday")
elif day_number == 3:
    print("Wednesday - Weekday")
elif day_number == 4:
    print("Thursday - Weekday")
elif day_number == 5:
    print("Friday - Weekday")
elif day_number == 6:
    print("Saturday - Weekend")
elif day_number == 7:
    print("Sunday - Weekend")
else:
    print("Invalid day number! Please enter a number between 1 and 7.")

print("__________________________________________________________________________________")
#20. Write a Python program to determine if a number is within the range 1–100 (inclusive).
num = int(input("Enter a number: "))
if 1 <= num <= 100:
    print(f"{num} is within the range 1-100.")
else:
    print(f"{num} is outside the range 1-100.")

print("__________________________________________________________________________________")
#21. Write a Python program to check if three angles form a valid triangle (sum = 180°).  
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the second angle: "))
angle3 = float(input("Enter the third angle: "))
if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")

print("__________________________________________________________________________________")
#22. Write a program to determine the largest of four numbers using conditional statements.  
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    largest = num1
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    largest = num2
elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    largest = num3
else:
    largest = num4
print(f"The largest number is: {largest}")

print("__________________________________________________________________________________")
#23. Write a Python program to calculate electricity charges based on the following:(- Units <= 100: Free , - 101–200: Rs. 2 per unit,- 201–500: Rs. 5 per unit, - Units > 500: Rs. 10 per unit )
units = float(input("Enter the number of electricity units consumed: "))
if units <= 100:
    charge = 0
    print(f"charge is {charge}")
elif 101< units <200: 
    charge= units*2
    print(f"charge is{charge}")
elif 201< units < 500: 
    charge = units*5 
    print(f"charge is{charge}")
else: 
   units >500
   charge=units*10
   print(f"charge is {charge}")
   

print("__________________________________________________________________________________")
# 24. Take two integers as input. If the first number is greater, calculate their sum; otherwise, calculate their difference.  
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
if num1 > num2:
    result = num1 + num2 
else:
    result = abs(num1 - num2) 
print(f"The result is: {result}")

print("__________________________________________________________________________________")
#25. Write a Python program to simulate a simple calculator that takes two numbers and an operator (+, -, *, /) as input and performs the appropriate operation.
a=int(input("enter a first num: "))
b=int(input("enter second num: "))
op= input("enter opertaor :")
if op =='+':
    print(f"addition:{a+b}")
elif op =='-':
    print(f"{a-b}")
elif op == '*':
    print(f"{a*b}")
elif op =='/':
    print(f"{a/b}")
else :
    print("could you please enter vaild opertor")

print("__________________________________________________________________________________")

#Weekly Questions for Practice (23th - 27th Dec)
#1. Write a program to print numbers from 1 to 10 using a while loop. 
num=1
while num<=10:
    print(num)
    num +=1

print("__________________________________________________________________________________")
#2. Create a program to find the sum of all even numbers between 1 and 50 using a while loop.  
num= 2
sum_even_num=0
while num <= 50:
    sum_even_num +=num
    num +=2
print("the sum of all even number between 1 to 50 is: ",sum_even_num)

print("_..._"*25)
#3. Write a program that repeatedly asks the user for input until they enter the word "stop". Print all the inputs as a list.  
inputs = []
while True:
    user_input = input("Enter something (or type 'stop' to quit): ")
    if user_input.lower() == 'stop':
        break
    inputs.append(user_input)
print("You entered the following inputs:")
print(inputs)


print("_..._"*25)
#4. Create a program using a while loop that calculates the factorial of a given number
num = int(input("Enter a number to calculate its factorial: "))
factorial = 1
while num > 1:
    factorial *= num  
    num -= 1
print(f"The factorial is: {factorial}")

print("_..._"*25)
#5. Write a program using a for loop to print the multiplication table of a given number.  
num = int(input("Enter a number to print its multiplication table: "))
print(f"Multiplication table of {num} is:")
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

print("_..._"*25)
#6. Create a program to calculate the sum of all elements in a list using a for loop.  
numbers = [10, 20, 30, 40, 50]
total_sum = 0
for num in numbers:
    total_sum += num 
print(f"The sum of all elements in the list is: {total_sum}")


print("_..._"*25)
#7. Write a program using a for loop to find the largest number in a given list of numbers
numbers = [10, 45, 23, 89, 32, 100, 5]
largest_number = numbers[0]
for num in numbers:
    if num > largest_number:  
        largest_number = num  
print(f"The largest number in the list is: {largest_number}")

print("_..._"*25)
#8. Write a program to display all vowels in a given string using a for loop. 
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_list = []
for char in input_string:
    if char in vowels: 
        vowel_list.append(char)
print("Vowels in the given string:", vowel_list)

print("_..._"*25)
#9. Create a list of 10 numbers and write a program to reverse the list without using the reverse() method.  
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
reversed_numbers = []
for num in numbers:
    reversed_numbers.insert(0, num) 
print("Reversed list:", reversed_numbers)

print("_..._"*25)
#10. Write a program to count the occurrences of each element in a list and display the result as a dictionary.  
elements = [1, 2, 2, 3, 4, 4, 4, 5, 6, 2, 3]
count_dict = {}
for element in elements:
    if element in count_dict:
        count_dict[element] += 1  
    else:
        count_dict[element] = 1  
print("Occurrences of each element:", count_dict)


print("_..._"*25)
#11. Create a list of 5 strings and write a program to find the longest string in the list.  
strings = ["apple", "banana", "kiwi", "strawberry", "cherry"]
longest_string = strings[0]
for string in strings:
    if len(string) > len(longest_string):
        longest_string = string 
print("The longest string in the list is:", longest_string)

print("_..._"*25)
#12. Write a program to merge two lists and remove duplicate elements from the final list.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
merged_list = list1 + list2
unique_list = list(set(merged_list))
print("Merged list with unique elements:", unique_list)

print("_..._"*25)
#13. Write a program to create a tuple with numbers and find the second largest number in the tuple.  
numbers_tuple = (10, 20, 30, 40, 50, 60, 70, 280, 190)
unique_numbers = list(set(numbers_tuple))
unique_numbers.sort()
second_largest = unique_numbers[-2]  
print("The second largest number in the tuple is:", second_largest)

print("_..._"*25)
#14. Create a program to convert a tuple into a list, add 3 elements to the list, and convert it back into a tuple. 
original_tuple = (10, 20, 30, 40)
temp_list = list(original_tuple)
temp_list.append(50)
temp_list.append(60)
temp_list.append(70)
new_tuple = tuple(temp_list)
print("Original Tuple:", original_tuple)
print("New Tuple after adding elements:", new_tuple)


print("_..._"*25)
#15. Write a program to count how many times a specific element appears in a tuple.  
numbers_tuple = (10, 20, 30, 20, 40, 20, 20,20, 50)
element_to_count = 20
count = numbers_tuple.count(element_to_count)
print(f"The element {element_to_count} appears {count} times in the tuple.")

print("_..._"*25)
#16. Write a program to check if a given string is a palindrome (reads the same forward and backward).  
input_string = input("Enter a string: ")
input_string = input_string.lower()
if input_string == input_string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

print("_________________________________________________________________________________________________")
#17. Create a program to count the number of vowels, consonants, digits, and spaces in a string.  
input_string = input("Enter a string: ")
vowels_count = 0
consonants_count = 0
digits_count = 0
spaces_count = 0
vowels = "aeiouAEIOU"
for char in input_string:
    if char.isdigit():  
        digits_count += 1
    elif char.isalpha(): 
        if char in vowels:  
            vowels_count += 1
        else: 
            consonants_count += 1
    elif char == ' ':  
        spaces_count += 1
print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonants_count}")
print(f"Digits: {digits_count}")
print(f"Spaces: {spaces_count}")

print("_________________________________________________________________________________________________")
#18. Write a program to replace all spaces in a string with underscores.  
input_string = input("Enter a string: ")
modified_string = input_string.replace(" ", "_")
print("Modified string:", modified_string)

print("_________________________________________________________________________________________________")
#19. Write a program to find the first non-repeating character in a string.  
input_string = input("Enter a string: ")
for char in input_string:
    if input_string.count(char) == 1:
        print(f"The first non-repeating character is: {char}")
        break
else:
    print("No non-repeating character found.")

print("_________________________________________________________________________________________________")
#20. Create two sets of numbers and write a program to find their union, intersection, and difference.  
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
print("Set 1:", set1)
print("Set 2:", set2)
print("Union of Set 1 and Set 2:", union)
print("Intersection of Set 1 and Set 2:", intersection)
print("Difference between Set 1 and Set 2:", difference)

print("_________________________________________________________________________________________________")
#21. Write a program to remove duplicate elements from a list using a set.  
input_list = [1, 2, 3, 4, 5, 2, 2, 4, 4, 3, 6, 7, 1]
unique_list = list(set(input_list))
print("List without duplicates:", unique_list)

print("_________________________________________________________________________________________________")
#22. Create a program to check if one set is a subset of another set.  
set1 = {1, 2, 3, 4}
set2 = {2, 3} 
if set2.issubset(set1):
    print("Set2 is a subset of Set1.") #output:set2 is a subset of set1
else:
    print("Set2 is not a subset of Set1.")

print("_________________________________________________________________________________________________")
#23. Write a program to create a dictionary where keys are numbers from 1 to 5, and values are their squares. 
squares_dict = {}
for i in range(1, 6):
    squares_dict[i] = i ** 2  
print(squares_dict)

print("_________________________________________________________________________________________________")
#24. Create a program to merge two dictionaries and handle duplicate keys by summing their values.  
dict1 = {1: 10, 2: 20, 3: 30}
dict2 = {2: 15, 3: 25, 4: 40}
merged_dict = dict1.copy()  
for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value  #output:{1: 10, 2: 35, 3: 55, 4: 40}
    else:
        merged_dict[key] = value  
print("Merged dictionary:", merged_dict)


print("_________________________________________________________________________________________________")
#25. Write a program to sort a dictionary by its values in ascending order.
my_dict = {3: 30, 1: 10, 8: 40, 4: 20}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary by values (ascending):", sorted_dict)