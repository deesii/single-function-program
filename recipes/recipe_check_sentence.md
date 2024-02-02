# {{PROBLEM}} Function Design Recipe
## 1. Describe the Problem
#As a user
#So that I can improve my grammar
#I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

```python
# EXAMPLE

def check_sentence(text):
    return True or False

````
# Nouns: Text, Capital letter, punctuation mark
# Verbs: Verify

# Input: parameter = Text(string)
# Output: True or False (boolean)

# Assumptions:
# Suitable punctuation = .!?



## 3. Create Examples as Tests

"Given an empty string, returns False"
check_sentence("") -> output: False

"Given a text is not a string, returns False"
check_sentence([G, !]) -> output: False

"Given a text that starts with capital letter and end with suitable punctuation mark, it returns True"
check_sentence("Hello, today is a very cloudy day!") -> output: True

"Given a text that starts with capital letter but doesnt end with suitable punctuation mark"
check_sentence("Hello, today is a very cloudy day,") -> output: False

"Given a text that doesnt start with a capital letter but end with suitable punc. mark"
check_sentence("hello, today is a very cloudy day.") -> output: False

"Given a text which includes multiple punctuation and has a starting capital letter but doesnt have an ending punctuation mark. Outputs False"
check_sentence("Hello, today is! a very cloudy day.") -> output: False

"Doesnt output True or False?"

## 4. Implement the Behaviour # see the test file.

test_starts_with_capital_letter_and_ends_with_punc()