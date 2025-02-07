using NUnit.Framework;
using System;
using Allure.Net.Commons;  // Correct namespace for SeverityLevel
using NUnit.Allure.Attributes;
using NUnit.Allure.Core;

namespace CalculatorTests
{
    [TestFixture]
    [AllureNUnit]
    public class CalculatorTests
    {
        private Calculator _calculator;

        [SetUp]
        public void Setup()
        {
            _calculator = new Calculator();
        }

        [Test(Description = "Tests the addition of two integers.")]
        [AllureTag("Calculator", "Addition")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestAddition()
        {
            Assert.AreEqual(5, _calculator.Add(2, 3));
        }

        [Test(Description = "Tests the subtraction of two integers.")]
        [AllureTag("Calculator", "Subtraction")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestSubtraction()
        {
            Assert.AreEqual(1, _calculator.Subtract(3, 2));
        }

        [Test(Description = "Tests the multiplication of two integers.")]
        [AllureTag("Calculator", "Multiplication")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestMultiplication()
        {
            Assert.AreEqual(6, _calculator.Multiply(2, 3));
        }

        [Test(Description = "Tests the division of two integers.")]
        [AllureTag("Calculator", "Division")]
        [AllureSeverity(SeverityLevel.normal)]
        public void TestDivision()
        {
            Assert.AreEqual(2.5, _calculator.Divide(5, 2));
        }

        [Test(Description = "Tests division by zero exception handling.")]
        [AllureTag("Calculator", "DivisionByZero")]
        [AllureSeverity(SeverityLevel.critical)]
        public void TestDivisionByZero()
        {
            Assert.Throws<DivideByZeroException>(() => _calculator.Divide(5, 0));
        }
    }
}
