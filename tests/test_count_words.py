#design
#A function called count_words that takes a string as 
#an argument and returns the number of words in that string.
#assumed & is not counted as a word! 

from lib.count_words import *

# test that it will return 0 from an empty string
def test_given_empty_string_return_zero():
    assert count_words("") == 0

# test that it will return the length 4 for a sentence of 4 words
    
def test_given_4_words_return_4():
    assert count_words("Hello you are great")

# test that will ignore apostrophes and count the word as a single word
    
def test_given_apostrophes_to_ignore_and_return_number_as_if_separate_word():
    assert count_words("Hello, it's cold outside.") == 4


# test_given_punctuation_in_between_words_to_ignore_those_and_return_count_as_if_not_present
    
def test_given_punctuation_in_between_words_to_ignore_those_and_return_count_as_if_not_present():
    assert count_words("He waited ... and there was no response") == 7

def test_given_multiple_spaces_return_count_as_if_not_present():
    assert count_words("He waited  and there was no response") == 7