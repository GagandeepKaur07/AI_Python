import re


def demonstrate_metacharacter():
    sample_text = """
    The quick brown fox over the lazy dog.
    foxes are wild animal . The dog quickly ran away.
    foxes are wild animals. The dog quickly ran away.
    My email is gagan323045@gmail.com and my number is (+91) 7697176917"""
# Task 2: Demonstrate various metacharacters
    dot_p = r'The.quick'
    print(f" Dot (.) Pattern '{(dot_p)}' :", re.findall(dot_p, sample_text))

# 2 ________________________________________________
    caret_pattern = r'^The'
    dollar_pattern = r'dog.$'
    print(f"Start of String (^) Pattern '{{caret_pattern }}' :", re.match(
        caret_pattern, sample_text))
    print(f"End of String ($) Pattern '{{dollar_pattern}}' : ", re.search(
        dollar_pattern, sample_text))

# 3 ________________________________________________
    asterisk_pattern = r'fox*'
    plus_pattern = r'fox+'
    print(f"Asterisk (*) pattern '{{asterisk_pattern}}':",
          re.findall(asterisk_pattern, sample_text))
    print(f"Plus (+) Pattern ' {{ plus_pattern}}' : ",
          re.findall(plus_pattern, sample_text))

# 4 ________________________________________________
    question_pattern = r'fox?'
    print(f"Question mark ? pattern' {{question_patern}}' :", re.findall(
        question_pattern, sample_text))

# 5 ________________________________________________
    braces_pattern = r'fo{2}'
    print(f"Brace ({{}}) Pattern '{{braces_pattern}}' :",
          re.findall(braces_pattern, sample_text))

# 6 ________________________________________________
    square_brackets_pattern = r'[Ff]ox'
    print(f"Square Brackets ([]) pattern '{{square_bracket_pattern}}' :", re.findall(
        square_brackets_pattern, sample_text))

# 7 ________________________________________________
    pipe_pattern = r'fox|dog'
    print(f"pipe | pattern '{{pice_pattern}}' :", re.findall(pipe_pattern,sample_text))

# 8 ________________________________________________
    backslash_pattern=r'\.'
    print(f"Baskslash (\\) pattern '{{backslash_pattern}}' :", re.findall(backslash_pattern,sample_text))

# 9 ________________________________________________
    email_pattern = r'\b\w+@\w+\b'
    phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
    print(f"Email pattern '{{email_pattern}}' :", re.findall(email_pattern,sample_text))
    print(f"Phone pattern '{{phone_pattern}}' :", re.findall(phone_pattern,sample_text))

# 10 _______________________________________________
def main():
    demonstrate_metacharacter()
if __name__ == "__main__":
    main()