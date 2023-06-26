# Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
import math


def is_prime(num):
    # Since 2 is the smallest prime number, we know any num < 2 is false.
    if num < 2:
        return False
    # Since 2 is the only even number that is also a prime number, if num != 2 and == odd, it's false
    if num % 2 == 0 and num != 2:
        return False
    # We are going to start at 3 and iterate up through every odd number until we hit the square root.
    for n in range(3, int(math.sqrt(num)), 2):
        if num % n == 0:
            return False
    return True


# is_prime(2) => True
print(is_prime(2))

# is_prime(3) => True
print(is_prime(3))

# is_prime(4) => False
print(is_prime(4))

# is_prime(29) => True
print(is_prime(29))

# is_prime(200) => False
print(is_prime(200))
