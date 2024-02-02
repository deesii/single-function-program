from lib.check_sentence import *

#Given an empty string, returns False
def test_input_is_an_empty_string():
    result = check_sentence("")
    assert result == False

#Given a text that starts with capital letter and end with punctuation mark, it returns True
def test_where_text_starts_with_capital_ends_with_suitable_punc_mark():
    result = check_sentence("Hello, today is a very cloudy day!")
    assert result == True

#Given a text that starts with capital letter but doesnt end with suitable punctuation mark, return False
def test_where_text_starts_with_capital_but_doesnt_end_with_suitable_punc_mark():
    result = check_sentence("Hello, today is a very cloudy day")
    assert result == False

#Given a text that doesnt start with capital letter but ends with suitable punctuation mark, return False
def test_where_text_doesnt_start_with_capital_but_ends_with_suitable_punc_mark():
    result = check_sentence("hello, today is a very cloudy day!")
    assert result == False

#Given a text which includes multiple punctuation and has a starting capital letter but doesnt have an ending punctuation mark. Outputs False
def test_where_text_has_multiple_punctuation_with_but_first_and_last_letters_are_correct():
    result = check_sentence("Bonjour, today? is a very! cloudy day!")
    assert result == True

#Given a text is not a string, it is a list, returns False
def test_where_input_is_a_list():
    result = check_sentence(['B','s', 'd', '?'])
    assert result == False

#Given a text is not a string, returns False
def test_where_input_is_not_string():
    result = check_sentence({'Adam': 'apple', 'Donna': 'pear!'})
    assert result == False