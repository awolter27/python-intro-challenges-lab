# Write a function even_range(start, end) that returns an list containing all even numbers between 'start' and 'end' in sequential order.


def even_range(start, end):
    even_nums = []
    for i in range(start, (end + 1)):
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums


# even_range(13, 20) => [14, 16, 18, 20]
print(even_range(13, 20))

# even_range(4, 11) => [4, 6, 8, 10]
print(even_range(4, 11))

# even_range(8, 5) => []
print(even_range(8, 5))
