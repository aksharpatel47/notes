import pytest
from fizz_buzz import fizz_buzz


def test_fizzbuzz(input, output):
    assert fizz_buzz(input) == output


def test_canCallFizzBuzz():
    fizz_buzz(1)


def test_returns1WhenPassed1():
    assert fizz_buzz(1) == "1"


def test_returns2WhenPassed2():
    assert fizz_buzz(2) == "2"


def test_returnsFizzWhenPassed3OrMultipleOf3():
    assert fizz_buzz(3) == "Fizz"
    assert fizz_buzz(6) == "Fizz"


def test_returnsBuzzWhenPassed5OrMultipleOf5():
    assert fizz_buzz(5) == "Buzz"
    assert fizz_buzz(10) == "Buzz"


def test_returnsFizzBuzzWhenPassed15():
    assert fizz_buzz(15) == "FizzBuzz"


class TestMe:
    def test_me(self):
        assert True

    def test_me2(self):
        assert True
