def make_snippet(words: str):
    words_list = words.split(" ")
    if len(words_list) <= 5:
        return words
    else:
        return " ".join(words_list[0:5]) + "..."