from lib.manage_time import *

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

"""
Given an empty string it will return a string that says it will take 0 seconds to read

"""

def test_no_text_ouputs_string_with_0_how_long_it_takes():
    result = time_to_read("")
    assert result == "It will take approximately 0h 0m and 0s to read this text assuming I can read 200 words a minute"


"""
Given a list of words that it outputs the string with number of words 
"""

def test_text_all_alphabet_returns_how_long_it_takes():
    result = time_to_read("hello WORLD love you!")
    assert result == "It will take approximately 0h 0m and 1s to read this text assuming I can read 200 words a minute"

"""
Given a mix of words in the text to include both numerical information it will consider it and will outpiut the string to say how long it will take to read
"""

def test_text_mixed_alpha_and_numberical_how_long_it_takes():

    result = time_to_read("I was 30 years old yesterday")
    assert result == "It will take approximately 0h 0m and 2s to read this text assuming I can read 200 words a minute"


"""
Test that it will include individual punctuation & in the middle of the text and count those as words
"""

def test_text_include_ampersand_counts_as_separate_how_long_it_takes():

    result = time_to_read("hello & goodbye, world")
    assert result == "It will take approximately 0h 0m and 1s to read this text assuming I can read 200 words a minute"



"""
Given that there is numbers and punctuation together, it will only count it as one word
"""

def test_text_words_with_punctuation_together_count_as_one_word():

    result = time_to_read("The potato cost £4.56 to make")
    assert result == "It will take approximately 0h 0m and 2s to read this text assuming I can read 200 words a minute"


"""
Given a really long bit of text it will return a string that says it will take minutes and seconds also!
"""
def test_really_long_bit_of_text():
    result = time_to_read(" ".join("word" for i in range(16350)))
    assert result == "It will take approximately 1h 21m and 45s to read this text assuming I can read 200 words a minute"

# def test_text_words_with_punctuation_together_count_as_one_word_blobby():

#     result = time_to_read("The potato cost £4.56 to make")
#     assert result == "It will take approximately 0h 0m and 2s to read this text assuming I can read 200 words a minute"

