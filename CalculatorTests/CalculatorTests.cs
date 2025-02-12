using NUnit.Framework;
using System;
using Allure.Net.Commons;  // Make sure your NuGet references are correct.
using NUnit.Allure.Attributes;
using NUnit.Allure.Core;

namespace CalculatorTests
{
    /// <summary>
    /// A simple Calculator implementation to demonstrate unit tests.
    /// </summary>
    public class Calculator
    {
        public int Add(int x, int y) => x + y;

        public int Subtract(int x, int y) => x - y;

        public int Multiply(int x, int y) => x * y;

        public double Divide(int x, int y)
        {
            // Throw an exception if dividing by zero.
            if (y == 0)
                throw new DivideByZeroException("Cannot divide by zero.");

            // Cast to double to preserve fractional results.
            return x / (double)y;
        }
    }

    [TestFixture]
    [AllureNUnit] // Enables Allure reporting for this fixture
    public class CalculatorTests
    {
        private Calculator _calculator;

        [SetUp]
        public void Setup()
        {
            // Initialize Calculator before each test
            _calculator = new Calculator();
        }

        [Test(Description = "Tests the addition of two integers.")]
        [AllureTag("Calculator", "Addition")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestAddition()
        {
            // Expected: 2 + 3 = 5
            Assert.AreEqual(5, _calculator.Add(2, 3), "Addition result should be 5.");
        }

        [Test(Description = "Tests the subtraction of two integers.")]
        [AllureTag("Calculator", "Subtraction")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestSubtraction()
        {
            // Expected: 3 - 2 = 1
            Assert.AreEqual(1, _calculator.Subtract(3, 2), "Subtraction result should be 1.");
        }

        [Test(Description = "Tests the multiplication of two integers.")]
        [AllureTag("Calculator", "Multiplication")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestMultiplication()
        {
            // Expected: 2 * 3 = 6
            Assert.AreEqual(6, _calculator.Multiply(2, 3), "Multiplication result should be 6.");
        }

        [Test(Description = "Tests the division of two integers resulting in a fractional value.")]
        [AllureTag("Calculator", "Division")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestDivision()
        {
            // Expected: 5 / 2 = 2.5
            // If you're concerned about floating-point rounding, you can add a tolerance:
            // Assert.AreEqual(2.5, _calculator.Divide(5, 2), 0.000001);
            Assert.AreEqual(2.5, _calculator.Divide(5, 2), "Division result should be 2.5.");
        }

        [Test(Description = "Tests division by zero exception handling.")]
        [AllureTag("Calculator", "DivisionByZero")]
        [AllureSeverity(SeverityLevel.critical)]
        public void TestDivisionByZero()
        {
            // Verify that dividing by zero throws the correct exception
            Assert.Throws<DivideByZeroException>(() => _calculator.Divide(5, 0), 
                "Dividing by zero should throw a DivideByZeroException.");
        }
    }
}
