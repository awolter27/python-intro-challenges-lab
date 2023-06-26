# Write a function to compute the `factorial` of a number. Given a whole number n, a factorial is the product of all whole numbers from 1 to n. 5! = 5 * 4 * 3 * 2 * 1


def factorial(n):
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total


# factorial(5) => 120
print(factorial(5))
