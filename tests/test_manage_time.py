from lib.manage_time import *

# As a user
# So that I can manage my time
# I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

"""
Given an empty string it will return a string that says it will take 0 seconds to read

"""

def test_no_text_ouputs_string_with_0_how_long_it_takes():
    result = time_to_read("")
    assert result == "It will take approximately 0m and 0s to read this text assuming I can read 200 words a minute"


"""
Given a list of words that it outputs the string with number of words 
"""

def test_text_all_alphabet_returns_how_long_it_takes():
    result = time_to_read("hello WORLD love you!")
    assert result == "It will take approximately 0m and 1s to read this text assuming I can read 200 words a minute"

"""
Given a mix of words in the text to include both numerical information it will consider it and will outpiut the string to say how long it will take to read
"""

def test_text_mixed_alpha_and_numberical_how_long_it_takes():

    result = time_to_read("I was 30 years old yesterday")
    assert result == "It will take approximately 0m and 2s to read this text assuming I can read 200 words a minute"


"""
Test that it will include individual punctuation & in the middle of the text and count those as words
"""

def test_text_include_ampersand_counts_as_separate_how_long_it_takes():

    result = time_to_read("hello & goodbye, world")
    assert result == "It will take approximately 0m and 1s to read this text assuming I can read 200 words a minute"



"""
Given that there is numbers and punctuation together, it will only count it as one word
"""

def test_text_words_with_punctuation_together_count_as_one_word():

    result = time_to_read("The potato cost £4.56 to make")
    assert result == "It will take approximately 0m and 2s to read this text assuming I can read 200 words a minute"


"""
Given a really long bit of text it will return a string that says it will take minutes and seconds also!
"""
def really_long_bit_of_text():
    result = time_to_read("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat.")
    assert result == "It will take approximately 1m 2s to read this text assuming I can read 200 words a minute"