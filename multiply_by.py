# Write a function called `multiply_by` that takes a list and a number, and returns the list of numbers multiplied by that number.


def multiply_by(list, number):
    new_list = []
    for num in list:
        multiplied_number = num * number
        new_list.append(multiplied_number)
    return new_list


# multiply_by([1, 2, 3], 5) => [5, 10, 15]
print(multiply_by([1, 2, 3], 5))

# multiply_by([1, 2, 3], 5) => [10, 20, 30]
print(multiply_by([1, 2, 3], 10))
