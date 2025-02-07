import pytest
import sqlite3

# Fixture to set up the database connection
@pytest.fixture(scope="module")
def db_connection():
    # Create an in-memory SQLite database
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Define and register the factorial function
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    connection.create_function("calculate_factorial", 1, factorial)

    # Define and register the palindrome function
    def is_palindrome(input_string):
        normalized = ''.join(c.lower() for c in input_string if c.isalnum())
        return normalized == normalized[::-1]

    connection.create_function("is_palindrome", 1, is_palindrome)

    yield connection  # Provide the connection to the tests

    connection.close()  # Cleanup after tests

def test_factorial_of_0(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT calculate_factorial(0)")
    result = cursor.fetchone()[0]
    assert result == 1, "Factorial of 0 should be 1"

def test_factorial_of_5(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT calculate_factorial(5)")
    result = cursor.fetchone()[0]
    assert result == 120, "Factorial of 5 should be 120"

def test_factorial_of_10(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT calculate_factorial(10)")
    result = cursor.fetchone()[0]
    assert result == 3628800, "Factorial of 10 should be 3628800"

def test_palindrome_true(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT is_palindrome('A man a plan a canal Panama')")
    result = cursor.fetchone()[0]
    assert result == 1, "Should correctly identify a palindrome"

def test_palindrome_false(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT is_palindrome('Hello World')")
    result = cursor.fetchone()[0]
    assert result == 0, "Should correctly identify a non-palindrome"
