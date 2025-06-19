#single-quoted string
single_quoted = 'gagan,deep'

#string operations with single-quoted string
length = len(single_quoted)
upper_case = single_quoted.upper()
lower_case = single_quoted.lower()
contains_substring='d'in single_quoted
replace_text =single_quoted.replace("de","ga")
split_words= single_quoted.split()

#print all results
print("single_quoted",single_quoted)
print("length :",length)
print("upper_case",upper_case)
print("lower :",lower_case)
print("contains", contains_substring)
print("replace",replace_text)
print("string",split_words)
