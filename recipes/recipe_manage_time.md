# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def time_to_read(text):
    """takes the text and outputs a text which includes the time it takes to read the text

    Parameters: (list all parameters and their types) # not sure whether parameters mean just a string... or the different variations of parameters... )
        text: a string containing words (e.g. "hello WORLD")
        words_per_minute: integer
        numbers: a string containing numbers (e.g 5 )
        alphanumeric: a string with a mix of number and letters e.g (56yo)
        punctuation:


    Returns: (state the return value and its type)
        a string with the number of minutes and seconds (e.g. ["It will take you 4 minutes and 30 seconds to read this text assuming I can read 200 words per minute"])

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text containing only alphabets, it outputs a string that includes the time it takes to read the text
"""
time_to_read("hello WORLD love you!") => "It will take approximately 0m and 1s to read this text assuming I can read 200 words a minute"

"""
Given a mix of words in the text to include both numerical information it will consider it and will outpiut the string to say how long it will take to read
"""
time_to_read("I was 30 years old yesterday") => "It will take approximately 0m 8s to read this text assuming I can read 200 words a minute"
"""
Test that it will include individual punctuation & in the middle of the text and count those as words
"""
time_to_read("hello & goodbye, world") => "It will take approximately 0m 6s to read this text assuming I can read 200 words a minute"

"""
Given that there is numbers and punctuation together, it will only count it as one word
"""
time_to_read("The potato cost £4.56 to make") => "It will take approximately 0m 8s to read this text assuming I can read 200 words a minute"


"""
Given an empty string it will return a string that says it will take 0 seconds to read
"""
time_to_read("") => "It will take approximately 0m 0s to read this text assuming I can read 200 words a minute"

"""
Given a really long bit of text it will return a string that says it will take minutes and seconds also!
"""
time_to_read("bla..bla...bla...blaa ") => "It will take approximately 1m 2s to read this text assuming I can read 200 words a minute"

"""



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a list of words that it outputs the string with number of words 
"""
time_to_read("hello WORLD love you!") => "It will take approximately 0m and 5s to read assuming I can read 200 words a minute"

def test_no_text_ouputs_string_with_0_how_long_it_takes():
    result = time_to_read("")
    assert result == "It will take approximately 0m and 5s to read assuming I can read 200 words a minute"
```

Ensure all test function names are unique, otherwise pytest will ignore them!
