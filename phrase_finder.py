# Write a function phrase_finder(words, phrase), that takes in a list of words and a string representing a phrase. The function should return True if the phrase can be formed by a pair of words from the list. The function should return False if the phrase cannot be formed by any pair of words.


def phrase_finder(words, phrase):
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if (
                words[i] + " " + words[j] == phrase
                or words[j] + " " + words[i] == phrase
            ):
                return True
    return False


# phrase_finder(['world', 'prep', 'hello', 'bootcamp'], 'bootcamp prep') => True
print(phrase_finder(["world", "prep", "hello", "bootcamp"], "bootcamp prep"))

# phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'bootcamp prep') => True
print(phrase_finder(["world", "bootcamp", "hello", "prep"], "bootcamp prep"))

# phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello world') => True
print(phrase_finder(["world", "bootcamp", "hello", "prep"], "hello world"))

# phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello prep') => True
print(phrase_finder(["world", "bootcamp", "hello", "prep"], "hello prep"))

# phrase_finder(['world', 'bootcamp', 'hello', 'prep'], 'hello goodbye') => False
print(phrase_finder(["world", "bootcamp", "hello", "prep"], "hello goodbye"))
