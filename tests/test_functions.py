import pytest
from code.functions import reverse_string, is_palindrome, factorial, fibonacci

def test_reverse_string():
    """
    Unit test for reverse_string function.
    Tests different scenarios, including empty strings and single characters.
    """
    assert reverse_string("hello") == "olleh"
    assert reverse_string("world") == "dlrow"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("Python") != "Python"

def test_is_palindrome():
    """
    Unit test for is_palindrome function.
    Tests palindromic and non-palindromic strings.
    """
    assert is_palindrome("madam") is True
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("No lemon, no melon") is True

def test_factorial():
    """
    Unit test for factorial function.
    Tests basic cases and edge conditions like 0 and negative input.
    """
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(3) == 6
    with pytest.raises(ValueError):
        factorial(-1)

def test_fibonacci():
    """
    Unit test for fibonacci function.
    Tests specific values in the Fibonacci sequence and invalid inputs.
    """
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    with pytest.raises(ValueError):
        fibonacci(-1)