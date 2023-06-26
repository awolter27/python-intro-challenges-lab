# Write a function called `letter_count` to count the letter occurrence in a string. Use a dictionary. You can iterate over a string one letter at a time using a for loop.

# for letter in "alpha":
#   print(letter)

# Create a dictionary with `dd = {}`. Assign values with `dd["foo"] = 1`.
# Check to see if a dictionary has a key using the `in` operator.

# Careful. Python requires that you insert a key into a dictionary before you try to modify it's value. If you try to access a dictionary at a key that hasn't been added you'll get an error and the program will crash. Remember to use an if statement to see if a key is "in" a dictionary before you try to read it!


def letter_count(word):
    letter_totals = {}
    for letter in word:
        if letter in letter_totals:
            letter_totals[letter] += 1
            print(letter)
            print(letter_totals)
            print(letter_totals[letter])
        else:
            letter_totals[letter] = 1
        print(letter_totals)


# letter_count('banana') => {'a': 3, 'b': 1, 'n': 2}
print(letter_count("banana"))
