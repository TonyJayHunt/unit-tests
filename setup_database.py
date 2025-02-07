import sqlite3

def create_functions():
    """
    Creates the SQLite database and the necessary SQL functions.
    """
    connection = None
    try:
        # Connect to SQLite (creates the database if it doesn't exist)
        connection = sqlite3.connect("test_db.sqlite")
        cursor = connection.cursor()

        # Create a factorial function using SQLite's deterministic custom functions
        def factorial(n):
            if n < 0:
                raise ValueError("Factorial is not defined for negative numbers.")
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        # Register the factorial function in SQLite
        connection.create_function("calculate_factorial", 1, factorial)

        # Create a palindrome function
        def is_palindrome(input_string):
            normalized = ''.join(c.lower() for c in input_string if c.isalnum())
            return normalized == normalized[::-1]

        # Register the palindrome function in SQLite
        connection.create_function("is_palindrome", 1, is_palindrome)

        print("Functions created successfully in SQLite database.")

    except Exception as error:
        print(f"Error: {error}")

    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    create_functions()
