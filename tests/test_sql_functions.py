import pytest
import sqlite3

@pytest.fixture(scope="module")
def db_connection():
    """
    Pytest fixture that creates an in-memory SQLite database and registers two custom SQL functions:
    1) calculate_factorial(n): Returns the factorial of a non-negative integer n.
    2) is_palindrome(string): Returns 1 if 'string' is a palindrome, 0 otherwise.

    Yields:
        sqlite3.Connection: A connection to the in-memory SQLite database.
    """
    # Create an in-memory SQLite database
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    def factorial(n):
        """
        Compute the factorial of a non-negative integer n.

        Args:
            n (int): The non-negative integer whose factorial is to be computed.

        Returns:
            int: The factorial of n.

        Raises:
            ValueError: If n is negative.
        """
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    # Register the factorial function
    connection.create_function("calculate_factorial", 1, factorial)

    def is_palindrome(input_string):
        """
        Check if a given string is a palindrome.

        A palindrome check is performed by normalizing the string: 
        - removing all non-alphanumeric characters
        - converting to lowercase
        - comparing the string to its reverse

        Args:
            input_string (str): The string to be checked.

        Returns:
            bool (as int): 1 if the string is a palindrome, 0 otherwise.
        """
        normalized = ''.join(c.lower() for c in input_string if c.isalnum())
        return normalized == normalized[::-1]

    # Register the palindrome function
    connection.create_function("is_palindrome", 1, is_palindrome)

    yield connection  # Provide the connection to the tests

    # Cleanup after tests
    connection.close()

def test_factorial_of_0(db_connection):
    """
    Test that calculate_factorial(0) returns 1.
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT calculate_factorial(0)")
    result = cursor.fetchone()[0]
    assert result == 1, "Factorial of 0 should be 1"

def test_factorial_of_5(db_connection):
    """
    Test that calculate_factorial(5) returns 120.
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT calculate_factorial(5)")
    result = cursor.fetchone()[0]
    assert result == 120, "Factorial of 5 should be 120"

def test_factorial_of_10(db_connection):
    """
    Test that calculate_factorial(10) returns 3628800.
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT calculate_factorial(10)")
    result = cursor.fetchone()[0]
    assert result == 3628800, "Factorial of 10 should be 3628800"

def test_palindrome_true(db_connection):
    """
    Test that is_palindrome correctly identifies a known palindrome string.
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT is_palindrome('A man a plan a canal Panama')")
    result = cursor.fetchone()[0]
    assert result == 1, "Should correctly identify a palindrome"

def test_palindrome_false(db_connection):
    """
    Test that is_palindrome correctly identifies a non-palindrome string.
    """
    cursor = db_connection.cursor()
    cursor.execute("SELECT is_palindrome('Hello World')")
    result = cursor.fetchone()[0]
    assert result == 0, "Should correctly identify a non-palindrome"
