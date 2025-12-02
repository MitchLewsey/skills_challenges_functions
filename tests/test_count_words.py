from lib.count_words import *

"""
When passing in 3 words
Returns 3 as int
"""

def test_passing_three_words_returns_three():
    actual = count_words("one two three")
    expected = 3
    assert actual == expected

def test_passing_in_one_word_returns_one():
    actual = count_words("one")
    expected = 1
    assert actual == expected

def test_passing_in_one_long_string_no_spaces_returns_one():
    actual = count_words("21me,2e1'12'23t09@£$%^&*()")
    expected = 1
    assert actual == expected

def test_separating_words_with_more_than_one_space():
    actual = count_words("one  two  three")
    expected = 3
    assert actual == expected