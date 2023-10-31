import math

def is_prime(n):
    """
    Determine whether a number is a prime number.

    Parameters:
    n (int): The number to be checked for primality.

    Returns:
    bool: True if 'n' is a prime number, False otherwise.

    Example:
    >>> is_prime(11)
    True
    >>> is_prime(4)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
