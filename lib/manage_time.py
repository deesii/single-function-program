import math

def time_to_read( text):
    WORDS_PER_MINUTE = 200 
    words_list = text.split(" ")
    time_to_read_seconds = len(words_list)/(200/60)
    

    return f"It will take approximately 0m and {round(time_to_read)}s to read this text assuming I can read 200 words a minute"
    

