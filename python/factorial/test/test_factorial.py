import pytest
from factorial.factorial import factorial

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120
    assert factorial(3) == 6
    assert factorial(10) == 3628800

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(ValueError):
        factorial(-100)
        def test_factorial_large_number():
            assert factorial(20) == 2432902008176640000

        def test_factorial_type_error():
            with pytest.raises(TypeError):
                factorial(3.5)
            with pytest.raises(TypeError):
                factorial("5")
            with pytest.raises(TypeError):
                factorial(None)