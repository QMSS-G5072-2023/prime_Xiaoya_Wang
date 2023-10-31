from prime_xw2931.prime_xw2931 import is_prime


import sys
import os
sys.path.append("/Users/rr/Documents/GitHub/prime_Xiaoya_Wang")

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(11) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
