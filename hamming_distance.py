# In information theory, the hamming distance refers to the count of the differences between two strings of equal length. It is used in computer science for such things as implementing 'fuzzy search' capability.

# Write a function named hammingDistance that accepts two arguments which are both strings of equal length.
# The function should return the count of the symbols (characters, numbers, etc.) at the same position within each string that are different.
# If the strings are not of the same length, the function should return float('nan'). Note: There is no native not a number type, but it can be cast through float() or imported from the python math library.


def hamming_distance(str1, str2):
    if len(str1) == len(str2):
        total = 0
        count = len(str1) - 1
        while count >= 0:
            if str1[count] == str2[count]:
                count -= 1
            else:
                total += 1
                count -= 1
        return total
    else:
        return float("nan")


# hamming_distance('abc', 'abc') => 0
print(hamming_distance("abc", "abc"))

# hamming_distance('a1c', 'a2c') => 1
print(hamming_distance("a1c", "a2c"))

# hamming_distance('!!!!', '****') => 4
print(hamming_distance("!!!!", "****"))

# hamming_distance('abc', 'ab') => nan
print(hamming_distance("abc", "ab"))
