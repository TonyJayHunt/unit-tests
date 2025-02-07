
def reverse_string(input_string: str) -> str:
    """
    Reverses the given string.
    :param input_string: The string to be reversed.
    :return: The reversed string.
    """
    return input_string[::-1]

def is_palindrome(input_string: str) -> bool:
    """
    Checks if a given string is a palindrome.
    :param input_string: The string to be checked.
    :return: True if the string is a palindrome, False otherwise.
    """
    stripped_string = ''.join(filter(str.isalnum, input_string)).lower()
    return stripped_string == stripped_string[::-1]

def factorial(n: int) -> int:
    """
    Calculates the factorial of a given number.
    :param n: A non-negative integer.
    :return: The factorial of the number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n: int) -> int:
    """
    Calculates the nth Fibonacci number.
    :param n: The position in the Fibonacci sequence.
    :return: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative indices.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b