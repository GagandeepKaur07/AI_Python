# my_string="Hello, Edunet!"
# print("Original string:", my_string)
# print("First character: ",my_string[0])
# print("Last character: ",my_string[-1])

# # Task 2 : Implementation of String Concatenation and Repetition
# str1="gagan"
# str2="deep"
# concate=str1+" "+str2
# repeated=concate*3
# print("Concatenated string:", concate)
# print("Repeated string: ", repeated)

# # Task 3 : Implementation of String Case Manipulation
my_string="day,Today"
# upper=my_string.upper()
# lower=my_string.lower()
# title=my_string.title()
# swapcase_str=my_string.swapcase()
# print("upper :", upper)
# print("lower :", lower)
# print("title :", title)
# print("swapcase :", swapcase_str)

# Task 4: Implementation of Searching in Strings
# substring="today"
# found=my_string.find(substring)
# print(found)
# if found != -1:
#     print(f"Substring {substring} found at index {found}")
# else:
#     print(f"Substring {substring} not found")

# task 5 : Implementation of Replacing Substrings
new_string= my_string.replace("Today","World")
print ("String after replacement :", new_string)

# Task 6 : Implementation of Replacing Substrings
name="deep"
age=20
formatted=f"my name is {name} and i am {age} year old ."
print("formatted string .",formatted)

# Task 7: Implementation of Trimming and Padding Strings
padded=my_string.center(20,"*")
trimmed=" extra space ".strip()
print("padded string : ",padded)
print("trimmed: ",trimmed)

# Task 8: Implementation of Splitting and Joining Strings
sen="python is fun" 
words=sen.split()
join='_'.join(words)
print("Splitted words ;",words)
print("join sentence :", join)

# Task 9 : Implementation of Counting Characters
char_count=my_string.count("o")
print(f"character 'o' appers {char_count} times in the string")

# Task 10 : Implementation of Checking String Properties
is_alpha="hello".isalpha()
is_digit="12345".isdigit()
is_alnum="hello123".isalnum()
is_space=" ".isspace()
print("is 'hello' alphabetic? ",is_alpha)
print("is '12345' alphabetic? ",is_digit)
print("is 'hello123' alphabetic? ",is_alnum)
print("is '   ' alphabetic? ",is_space)