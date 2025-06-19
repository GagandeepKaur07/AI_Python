import re
def demostrate_special_sequence():
    sample_text = """
    The quick brown fox over the lazy dog.
    foxes are wild animal . The dog quickly ran away.
    foxes are wild animals. The dog quickly ran away.
    My email is gagan323045@gmail.com and my number is (+91) 7697176917
    """

#1 \d Matches any digit (0-9)
    digit_pattern = r'\d+'
    print(f"digit (\\d) pattern '{digit_pattern}':", re.findall(digit_pattern,sample_text))

#2 \D Matches any non digit character
    non_digit_pattern = r'\D+'
    print(f"Non digit (\\D) Pattern '{non_digit_pattern}':",re.findall(non_digit_pattern,sample_text))

# 3 \w -Matches any word charecter (alphanumeric + underscore)
    word_char_pattern =r'\w+'
    print(f"Word character (\\w) Pattern '{word_char_pattern}' :", re.findall(word_char_pattern,sample_text))

# 4 \W -Matches any non-word chaecter 
    non_word_char_pattern = r'\\W+'
    print(f"Non word characer (\\W) pattern '{non_word_char_pattern}':", re.findall(non_word_char_pattern,sample_text))

# 5 \s 
    whitespace_pattern = r'\s+'
    print(f"on whitespace characer (\\s) pattern ' {whitespace_pattern}':",re.findall(whitespace_pattern,sample_text))

# 6 \S
    non_whitespace_pattern = r'\S+'
    print(f"on whitespace characer (\\S) pattern ' {non_whitespace_pattern}':",re.findall(non_whitespace_pattern,sample_text))

#7 \b
    word_boundary =r'\bfox\b'
    print(f"word boundary(\\b)pattern '{word_boundary}':", re.findall(word_boundary,sample_text))

# 8 \B
    non_word_boundary =r'quick\B'
    print(f"word boundary(\\B)pattern '{non_word_boundary}':", re.findall(non_word_boundary,sample_text))

def main():
    demostrate_special_sequence()

if __name__ == "__main__":
    main()