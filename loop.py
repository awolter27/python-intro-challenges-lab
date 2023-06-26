# Write a function called `p_times` that takes a `statement` and a `num` as inputs, and outputs the `statement` some `num` of times to the console.

# Option 1:
# def p_times(statement, num):
#     count = 1
#     while count <= num:
#         print(str(statement))
#         count += 1


# Option 2:
def p_times(statement, num):
    for n in range(num):
        print(n, statement)


# Option 3:
# def p_times(statement, num):
#     while num > 0:
#         print(statement)
#         num -= 1
#     return statement


# p_times("Hello there", 1) =>
# Hello there
p_times("Hello there", 1)

# p_times("Hello there", 3) =>
# Hello there
# Hello there
# Hello there
p_times("Hello there", 3)
