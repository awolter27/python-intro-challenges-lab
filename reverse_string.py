# Write a function reverse_string(string) that takes in a hyphenated string and returns the hyphenated string reversed.


def reverse_string(string):
    words = string.split("-")
    words.reverse()
    return "-".join(words)


# reverse_string('Go-to-the-store') => 'store-the-to-Go'
print(reverse_string("Go-to-the-store"))

# reverse_string('Jump-jump-for-joy') => 'joy-for-jump-Jump,'
print(reverse_string("Jump-jump-for-joy"))
