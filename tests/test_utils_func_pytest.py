
import pytest
from utils.utils_func import is_prime
'''
python -m pytest tests\test_utils_func_pytest.py
'''
def test_is_prime_ok():
    for i in [2, 3, 5, 7, 11, 13, 17, 19]:
        assert is_prime(i) == True

def test_is_prime_no():
    for i in [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]:
        assert is_prime(i) == False

def test_is_prime_negative():
    assert is_prime(-1) == False

def test_is_prime_raise_typeerror():
    with pytest.raises(TypeError):
        is_prime('string')