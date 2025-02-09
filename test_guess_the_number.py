import pytest
from guess_the_number import simple_random

def test_random_number():
    seed = 42
    num1 = (simple_random(seed) % 100) + 1
    num2 = (simple_random(seed + 1) % 100) + 1
    assert num1 != num2  # Проверка, что числа меняются
