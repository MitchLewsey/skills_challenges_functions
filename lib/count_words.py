def count_words(words):
    words_list = [word for word in words.split(" ")]
    words_list_no_spaces = [w for w in words_list if w != ""]
    return len(words_list_no_spaces)