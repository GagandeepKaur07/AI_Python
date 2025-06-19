"""#Practice Questions on RegEx (re Module in Python)
    # Beginner Level
#1. Write a regex to validate an email address.
import re
email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
def validate_email(email):
    if re.match(email_regex, email):
        return True
    return False
email = "example@example.com"
if validate_email(email):
    print(f"'{email}' is a valid email address.") #output:valid email
else:
    print(f"'{email}' is not a valid email address.")

print("_______________________________________________________________________________")
#2. Create a regex to match Indian mobile numbers in the format +91 9876543210 or 9876543210.
import re
mobile_regex = r'^(?:\+91[-\s]?)?[789]\d{9}$'
def validate_mobile_number(mobile_number):
    if re.match(mobile_regex, mobile_number):
        return True
    return False
test_numbers = [
    "+91 9876543210",  # Valid format with country code and space
    "9876543210",      # Valid format without country code
    "+91-9876543210",  # Valid format with country code and hyphen
    "98765432",        # Invalid (too short)
    "+92 9876543210",  # Invalid (wrong country code)
    "9187654321"       # Invalid (country code without '+' or space/hyphen)
]
for number in test_numbers:
    if validate_mobile_number(number):
        print(f"'{number}' is a valid mobile number.")
    else:
        print(f"'{number}' is not a valid mobile number.")

print("_______________________________________________________________________________")
#3. Write a regex to check if a string starts with "Hello" and ends with "World".
import re
pattern = r"^Hello.*World$"
def check_hello_world(string):
    if re.match(pattern, string):
        return True
    return False
test_strings = [
    "Hello, how are you today? World",    # Valid
    "HelloWorld",                        # Valid
    "Hello World",                       # Valid
    "Hello",                             # Invalid (does not end with World)
    "World Hello",                       # Invalid (does not start with Hello)
    "Hello there, World",                # Valid
    "worldHello"                         # Invalid (does not start with Hello)
]
for text in test_strings:
    if check_hello_world(text):
        print(f"'{text}' : matches the pattern.")
    else:
        print(f"'{text}' : does not match the pattern.")                    

print("_______________________________________________________________________________")
#4. Extract all numeric values from the string: "The order number is 12345 and the price is 6789."
import re
text = "The order number is 12345 and the price is 6789."
numbers = re.findall(r'\d+', text)
print(numbers) #output:[12345,6789]


print("_______________________________________________________________________________")
#5. Write a regex to validate a username with the following rules:- (Should start with an alphabet,- Can include numbers and underscores, - Length should be between 5 and 12 characters.)
import re
pattern = r'^[a-zA-Z][a-zA-Z0-9_]{4,11}$'
def validate_username(username):
    if re.match(pattern, username):
        return True
    else:
        return False
username = "user_123"
if validate_username(username):
    print(f"{username} is a valid username.")
else:
    print(f"{username} is not a valid username.")


print("_______________________________________________________________________________")
#6. Match all dates in the format dd/mm/yyyy in a given string.
import re
text = "The event will be held on 12/05/2023, and the deadline is 25/12/2025."
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
dates = re.findall(pattern, text)
print(dates)

print("_______________________________________________________________________________")
#7. Create a regex to find all words starting with a capital letter in a sentence
import re
sentence = "The quick Brown Fox jumps over the Lazy Dog."
pattern = r'\b[A-Z][a-z]*\b'
capital_words = re.findall(pattern, sentence)
print(capital_words)

print("_______________________________________________________________________________")
#8. Extract the domain names from a list of email addresses.
import re
emails = [
    "john.doe@example.com",
    "jane.smith@company.org",
    "info@website.co.uk",
    "contact@mydomain.net"
]
pattern = r'@([a-zA-Z0-9.-]+)'
domains = [re.search(pattern, email).group(1) for email in emails]
print(domains)


print("_______________________________________________________________________________")
#9. Write a regex to split a sentence into words, ignoring punctuations like , . ! ?.
import re
sentence = "Hello, world! How's everything going? Let's try this."
pattern = r'\b\w+\b'
words = re.findall(pattern, sentence)
print(words)


print("_______________________________________________________________________________")
#10. Validate a password that must:- ( Contain at least one uppercase letter,- Contain at least one lowercase letter,- Contain at least one digit,- Be at least 8 characters long.)
import re
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
def validate_password(password):
    if re.match(pattern, password):
        return True
    else:
        return False
password = "Password123"
if validate_password(password):
    print(f"{password} is a valid password.")
else:
    print(f"{password} is not a valid password.")



print("_______________________________________________________________________________")
#11. Match all IPv4 addresses in the format xxx.xxx.xxx.xxx, where each xxx is between 0-255.
import re
text = "Here are some IPs: 192.168.0.1, 255.255.255.255, 10.0.0.256, and 172.16.254.1."
pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
ipv4_addresses = re.findall(pattern, text)
print(ipv4_addresses)

print("_______________________________________________________________________________")
#12. Write a regex to find all hashtags (#hashtag) in a tweet.
import re
tweet = "Loving the new features in Python! #Python #Regex #CodeIsLife #AI"
pattern = r'#\w+'
hashtags = re.findall(pattern, tweet)
print(hashtags)


print("_______________________________________________________________________________")
#13. Extract the prices (e.g., $123.45) from a given text.
import re
text = "The prices are $123.45, $67.89, and $1000.50, while some items are $45."
pattern = r'\$\d+(?:\.\d{2})?'
prices = re.findall(pattern, text)
print(prices)


print("_______________________________________________________________________________")
#14. Validate a string containing time in hh:mm AM/PM format.
import re
pattern = r'^(0?[1-9]|1[0-2]):([0-5][0-9]) (AM|PM)$'
def validate_time(time_string):
    if re.match(pattern, time_string):
        return True
    else:
        return False    #output:valid time
time_string = "08:30 PM"
if validate_time(time_string):
    print(f"{time_string} is a valid time.")
else:
    print(f"{time_string} is not a valid time.")


print("_______________________________________________________________________________")
#15. Write a regex to identify repeated words in a sentence, such as "the the cat jumped".
import re
sentence = "the the cat jumped over the the dog"
pattern = r'\b(\w+)\s+\1\b'
repeated_words = re.findall(pattern, sentence, re.IGNORECASE)
print(repeated_words) #output:[the,the]


print("_______________________________________________________________________________")
#16. Extract all phone numbers in various formats: +91 9876543210, 987-654-3210, or (123) 456-7890.
import re
text = '''
Contact us at +91 9876543210 or 987-654-3210. 
You can also reach us at (123) 456-7890 or (555) 987-6543.
'''
pattern = r'(\+?\d{1,2}\s?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}'
phone_numbers = re.findall(pattern, text)
flat_phone_numbers = [''.join(number) for number in phone_numbers]
print(flat_phone_numbers)


print("_______________________________________________________________________________")
#17. Write a regex to find all HTML tags in a webpage source.
import re
html_source = '''
<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>Welcome to My Website</h1>
    <p>This is a <a href="#">link</a> in a paragraph.</p>
    <div class="container">
      <p>Another paragraph with <strong>bold text</strong>.</p>
    </div>
  </body>
</html>
'''
pattern = r'</?[\w\s="/\'.-]*>'
html_tags = re.findall(pattern, html_source)
print(html_tags)

print("_______________________________________________________________________________")
#18. Extract all URLs from a given paragraph.
import re
text = '''
Here are some links: https://www.example.com, http://test-site.org, and www.website.net. 
Don't forget about ftp://ftp.example.com, or even mailto:someone@example.com!
'''
pattern = r'https?://\S+|www\.\S+|ftp://\S+|mailto:\S+'
urls = re.findall(pattern, text)
print(urls)

print("_______________________________________________________________________________")
#19. Validate vehicle registration numbers in the format MP09 AB 1234.
import re
pattern = r'^[A-Z]{2}\d{2} [A-Z]{2} \d{4}$'
def validate_vehicle_registration(reg_number):
    if re.match(pattern, reg_number):
        return True
    else:
        return False
reg_number = "MP09 AB 1234"
if validate_vehicle_registration(reg_number):
    print(f"{reg_number} is a valid vehicle registration number.")
else:
    print(f"{reg_number} is not a valid vehicle registration number.")


print("_______________________________________________________________________________")
#20. Match all zip codes in a string that follow the format 12345 or 12345-6789.
import re
text = '''
Here are some zip codes: 12345, 67890-1234, and 98765-4321.
Invalid zip codes: 1234, 123456, 12345-123456.
'''
pattern = r'\b\d{5}(-\d{4})?\b'
zip_codes = re.findall(pattern, text)
print(zip_codes)



print("_______________________________________________________________________________")
#21. Extract all valid filenames with extensions like .txt, .csv, .jpg, etc., from a directory list.
import re
file_list = [
    "document.txt", "image.jpg", "spreadsheet.csv", "photo.png", 
    "archive.zip", "notes.pdf", "data123.txt", "file_with_extension.docx",
    "invalidfile", "another_image.jpg"
]
pattern = r'\b[\w\-_]+(?:\.(?:txt|csv|jpg|png|pdf|docx))\b'
valid_files = [filename for filename in file_list if re.match(pattern, filename)]
print(valid_files)


print("_______________________________________________________________________________")
#22. Validate credit card numbers that are 16 digits long and may include spaces or dashes.
import re
credit_cards = [
    "1234 5678 9876 5432",
    "1234-5678-9876-5432",
    "1234567898765432",
    "1234 5678 9876 543",
    "1234 5678 9876 54321"
]
pattern = r'^(?:\d{4}[-\s]?){3}\d{4}$'
def validate_credit_card(card_number):
    if re.match(pattern, card_number):
        return True
    else:
        return False
for card in credit_cards:
    if validate_credit_card(card):
        print(f"{card} is a valid credit card number.")
    else:
        print(f"{card} is not a valid credit card number.")

print("_______________________________________________________________________________")
#23. Write a regex to find all occurrences of a specific word in a text, ignoring case sensitivity.
import re
text = '''
Python is an amazing programming language. I love coding in Python.
Learning Python is fun and challenging.
'''
word = "python"
pattern = r'\b' + re.escape(word) + r'\b'
matches = re.findall(pattern, text, re.IGNORECASE)
print(matches)


print("_______________________________________________________________________________")
#24. Validate PAN numbers in the format ABCDE1234F (5 letters, 4 digits, 1 letter).
import re
pan_numbers = [
    "ABCDE1234F",  # Valid
    "A1BCD2345G",  # Invalid (contains a digit in the first part)
    "ABCDE12345",   # Invalid (missing last letter)
    "ABCDE12345F",  # Invalid (5 digits, should be 4 digits)
    "ABCDE1234@F"   # Invalid (contains special character)
]
pattern = r'^[A-Z]{5}\d{4}[A-Z]{1}$'
def validate_pan(pan_number):
    if re.match(pattern, pan_number):
        return True
    else:
        return False
for pan in pan_numbers:
    if validate_pan(pan):
        print(f"{pan} is a valid PAN number.")
    else:
        print(f"{pan} is not a valid PAN number.")


print("_______________________________________________________________________________")"""
#25. Create a regex to detect any strings that do not contain numeric characters.
import re
strings = [
    "HelloWorld",
    "Hello123",
    "abc123",
    "TestString",
    "1234",
    "NoNumbersHere"
]
pattern = r'^[^\d]*$'
def no_numbers(string):
    return bool(re.match(pattern, string))
for string in strings:
    if no_numbers(string):
        print(f'"{string}" does not contain any numeric characters.')
    else:
        print(f'"{string}" contains numeric characters.')
