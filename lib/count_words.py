def count_words(str):
    # import string

    # punctuation = string.punctuation

    #length_string = len(str.split())


    no_punct_string = "".join(filter(lambda x : x.isalpha() or x.isdigit() or x.isspace(),str))

    length_string = len(no_punct_string .split())

    return length_string
    