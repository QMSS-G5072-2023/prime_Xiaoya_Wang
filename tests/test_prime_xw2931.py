from prime_xw2931 import prime_xw2931
import sys
import os


def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(11) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
