#!/usr/bin/env python
# coding: utf-8

# In[6]:


import re

if __name__ == '__main__':
    string = "YourString123"
    pattern = re.compile("[A-Za-z0-9]+")

    
    if pattern.fullmatch(string) is not None:
        print("Found match: " + string)
    else:
        
        print("No match")


# In[3]:


import re
text = input("Enter: ")
result = re.sub("[A-Za-z0-9]", '', text)
if len(result) == 0:
    print("Success")
else:
    print("Failure")


# In[4]:


def text_match(text):
        patterns = 'ab*?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbc"))


# In[5]:


def text_match(text):
        patterns = 'ab+?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))


# In[7]:


def text_match(text):
        patterns = 'ab?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))


# In[8]:


def text_match(text):
        patterns = 'ab{2,3}?'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("ab"))
print(text_match("aabbbbbc"))


# In[9]:


import re

sample_text = "ImportanceOfRegularExpressionsInPython"
result = re.findall(r'[A-Z][a-z]*', sample_text)

print(result)


# In[10]:


def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


# In[11]:


import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))


# In[12]:


import re
def text_match(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("aabbbbd"))
print(text_match("aabAbbbc"))
print(text_match("accddbbjjjb"))


# In[15]:


import re
def text_match(text):
        patterns = '^\w+'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The dog eats."))
print(text_match(" The dog eats."))


# In[16]:


import re
def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The dog eats."))
print(text_match("dog_Eats_food"))


# In[20]:


import re
def match_num(string):
    text = re.compile(r"^5")
    if text.match(string):
        return True
    else:
        return False
print(match_num('5-2345861'))
print(match_num('6-2345861'))


# In[21]:


import re
ip = "314.09.567.056"
string = re.sub('\.[0]*', '.', ip)
print(string)


# In[24]:





# In[25]:


import re

sample_text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

date_pattern = r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2}(?:st|nd|rd|th)?\s\d{4}\b'

dates_found = re.findall(date_pattern, sample_text)

print(dates_found)


# In[26]:


def search_words(text, searched_words):
    found_words = []
    for word in searched_words:
        if word in text:
            found_words.append(word)
    return found_words

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_words = ['fox', 'dog', 'horse']

result = search_words(sample_text, searched_words)
print("Found words:", result)


# In[27]:


import re

def find_word_locations(text, searched_word):
    found_locations = []
    pattern = re.compile(re.escape(searched_word))
    for match in pattern.finditer(text):
        found_locations.append(match.start())
    return found_locations

sample_text = 'The quick brown fox jumps over the lazy dog.'
searched_word = 'fox'

result = find_word_locations(sample_text, searched_word)
print("Found locations:", result)


# In[28]:


import re

def find_substrings(text, pattern):
    found_substrings = re.findall(pattern, text)
    return found_substrings

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

result = find_substrings(sample_text, pattern)
print("Found substrings:", result)


# In[29]:


import re

def find_occurrence_and_position(text, pattern):
    found_occurrences = []
    for match in re.finditer(pattern, text):
        found_occurrences.append((match.group(), match.start()))

    return found_occurrences

sample_text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'

result = find_occurrence_and_position(sample_text, pattern)
print("Found occurrences and positions:")
for occurrence, position in result:
    print(f"Occurrence: {occurrence}, Position: {position}")


# In[30]:


from datetime import datetime

def convert_date_format(date_str):
    
    original_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    
    new_date_str = original_date.strftime("%d-%m-%Y")
    
    return new_date_str


date_in_yyyy_mm_dd = "2023-07-16"


date_in_dd_mm_yyyy = convert_date_format(date_in_yyyy_mm_dd)


print("Original Date (yyyy-mm-dd):", date_in_yyyy_mm_dd)
print("Converted Date (dd-mm-yyyy):", date_in_dd_mm_yyyy)


# In[31]:


import re

def find_words_starting_with_a_or_e(text):
    pattern = r'\b[aAeE]\w+\b'
    found_words = re.findall(pattern, text)
    return found_words

sample_text = "Apples are delicious, but elephants are enormous."
result = find_words_starting_with_a_or_e(sample_text)
print("Words starting with 'a' or 'e':", result)


# In[32]:


def extract_numbers_with_positions(text):
    numbers_with_positions = []
    for index, char in enumerate(text):
        if char.isdigit():
            numbers_with_positions.append((char, index))
    return numbers_with_positions

sample_text = "Hello 123 World 456"
result = extract_numbers_with_positions(sample_text)
print("Numbers with their positions:")
for number, position in result:
    print(f"Number: {number}, Position: {position}")


# In[33]:


import re

def extract_max_numeric_value(text):
    numbers = [int(number) for number in re.findall(r'\d+', text)]
    if numbers:
        return max(numbers)
    else:
        return None

sample_text = "The maximum value is 42, and the minimum is 7."
max_value = extract_max_numeric_value(sample_text)

if max_value is not None:
    print("Maximum numeric value:", max_value)
else:
    print("No numeric values found in the text.")


# In[34]:


import re

def add_spaces_between_capital_words(text):
    pattern = r'([A-Z][a-z]+)'
    return re.sub(pattern, r' \1', text)

sample_text = "ThisIsAnExampleTextWithNoSpacesBetweenCapitalWords."
result = add_spaces_between_capital_words(sample_text)

print("Result:", result)


# In[35]:


import re

def find_uppercase_followed_by_lowercase(text):
    pattern = r'[A-Z][a-z]+'
    return re.findall(pattern, text)

sample_text = "ThisIsAnExampleTextWithMultipleSequences."
result = find_uppercase_followed_by_lowercase(sample_text)

print("Found sequences:", result)


# In[36]:


import re

def remove_duplicate_words(sentence):
    pattern = r'\b(\w+)\b(?:\s+\1\b)+'
    return re.sub(pattern, r'\1', sentence)

sample_sentence = "This is is a sample sentence with duplicate duplicate words."
result = remove_duplicate_words(sample_sentence)

print("Result:", result)


# In[37]:


import re

def is_string_ending_with_alphanumeric(text):
    pattern = r'^.*\w$'
    return re.match(pattern, text) is not None

sample_string = "Hello123"
result = is_string_ending_with_alphanumeric(sample_string)

if result:
    print("The string ends with an alphanumeric character.")
else:
    print("The string does not end with an alphanumeric character.")


# In[38]:


import re

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

sample_text = '''RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the
same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No
wo'''
hashtags = extract_hashtags(sample_text)

print("Extracted hashtags:", hashtags)


# In[39]:


import re

def remove_strange_symbols(text):
    pattern = r'<U\+[\da-fA-F]+>'
    return re.sub(pattern, '', text)

sample_text = '''@Jags123456 Bharat band on
28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are
all different party leaders'''
clean_text = remove_strange_symbols(sample_text)

print("Cleaned text:", clean_text)


# In[50]:


import re
def extract_dates_from_file(filename):
    with open(filename, 'r') as file:
        text = file.read()

    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    dates = re.findall(pattern, text)
    return dates

filename = "Ron was born on 12-09-1992 and he was admitted to school 15-12-1999"

dates_found = extract_dates_from_file(filename)

print("Dates extracted from the file:")
for date in dates_found:
    print(date)


# In[51]:


import re

def replace_space_comma_dot_with_colon(text):
    pattern = r'[ ,.]'
    return re.sub(pattern, ':', text)

sample_text = 'Python Exercises, PHP exercises.'
result = replace_space_comma_dot_with_colon(sample_text)

print("Output:", result)


# In[ ]:




