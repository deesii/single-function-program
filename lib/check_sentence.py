def check_sentence(text):
    #refactoring:
    #suitable_punctuation = "?!."
    return type(text) == str and len(text) > 0 and text[0] == text[0].upper() and text[-1] in '!?.'
