def code_snippet(str):
    sentence_list = str.split()
    if len(sentence_list) <= 5:
        return str
    else:
        return " ".join(sentence_list[0:5]) + "..."
