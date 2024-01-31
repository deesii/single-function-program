from lib.code_snippet import *

# Design

# A function called make_snippet that takes a string as an argument and returns the first five words and then a '...' if there are more than that.

## given an empty string return an empty string

def test_given_empty_string_return_empty_string():
    result = code_snippet("")
    assert result == ""

# given string with 4 words, return the original string

def test_given_string_4_words_return_original():
    assert code_snippet("Sometimes, London is grey.") == "Sometimes, London is grey."

# given string with 5 words, return the original string
    
def test_given_string_5_words_return_original():
    assert code_snippet("I wish I could fly.") == "I wish I could fly."


# given string with more than 5 words, return the original string and "..."
    
def test_given_string_more_10_words_return_first_5_words_and_elipsis():
    assert code_snippet("The dragon whispered in his ears and it terrified him!") == "The dragon whispered in his..."


