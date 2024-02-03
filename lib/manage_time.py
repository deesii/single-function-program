import math

def time_to_read( text):
    WORDS_PER_MINUTE = 200 
    words_list = text.split(" ")
    
    time_to_read_seconds = len(words_list)/(200/60)
    seconds = time_to_read_seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds//60
    seconds %=60

    return f"It will take approximately {round(hour)}h {round(minutes)}m and {round(seconds)}s to read this text assuming I can read 200 words a minute"
    

