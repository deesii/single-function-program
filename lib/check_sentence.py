def check_sentence(text):
    if type(text) != str:
        return False
    else:
        if len(text) == 0:
            return False

        #suitable_punctuation = "?!."
        if text[0] == text[0].upper() and text[-1] == '!' or text[-1] == "?" or text[-1] == '.':
            return True
        else:
            return False