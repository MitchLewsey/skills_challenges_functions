from lib.make_snippet import *
import pytest

"""
When passing four words
Return the same four words unchanged
"""

def test_calling_four_words_returns_only_same_four_words():
    actual = make_snippet("one two three four")
    expected = "one two three four"
    assert actual == expected

"""
When passing five words
Return the same five word unchanged
"""

def test_calling_five_words_returns_only_same_five_words():
    actual = make_snippet("one two three four five")
    expected = "one two three four five"
    assert actual == expected

"""
When passing more than five words
Return only the first five words and append '...'
"""

def test_calling_six_words_returns_only_five_words_and_ellipsis():
    actual = make_snippet("one two three four five six")
    expected = "one two three four five..."
    assert actual == expected

"""
When passing just a space character
Return only a space character
"""

def test_passing_an_space_characters_returns_space_character():
    actual = make_snippet(" ")
    expected = " "
    assert actual == expected

"""
When passing a long string with no spaces
Return the same string unchanged
"""

def test_one_string_no_spaces_same_string_returned():
    actual = make_snippet("asdoand,ad,asd,m,m13e;1414k121pk2j12md")
    expected = "asdoand,ad,asd,m,m13e;1414k121pk2j12md"
    assert actual == expected