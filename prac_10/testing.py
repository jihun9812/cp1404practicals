import doctest
from prac_06.car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter and ending with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("python is fun")
    'Python is fun.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    """
    # Capitalize the first letter and ensure the phrase ends with a period
    phrase = phrase.capitalize()  # Capitalize the first letter
    if not phrase.endswith('.'):  # Add period if it doesn't end with one
        phrase += '.'
    return phrase


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    car_default = Car()
    assert car_default.fuel == 0, "Car default fuel is not set correctly"
    car_custom = Car(fuel=10)
    assert car_custom.fuel == 10, "Car custom fuel is not set correctly"

# run_tests()


# Uncomment this line to run doctests
doctest.testmod()
