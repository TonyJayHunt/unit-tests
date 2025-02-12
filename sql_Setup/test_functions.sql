-- Unit Tests using pgTAP
BEGIN;
SELECT plan(5);

-- Test case: Factorial of 0
SELECT is(calculate_factorial(0), 1, 'Factorial of 0 should be 1');

-- Test case: Factorial of 5
SELECT is(calculate_factorial(5), 120, 'Factorial of 5 should be 120');

-- Test case: Factorial of 10
SELECT is(calculate_factorial(10), 3628800, 'Factorial of 10 should be 3628800');

-- Test case: Palindrome check
SELECT ok(is_palindrome('A man a plan a canal Panama'), 'Correctly identifies a palindrome');
SELECT ok(NOT is_palindrome('Hello World'), 'Correctly identifies a non-palindrome');

SELECT * FROM finish();
ROLLBACK;
