# The RGB function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# **Note**: Your answer should always be 6 characters long, the shorthand with 3 will not work here.


def rgb(r, g, b):
    letters = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    output = ""
    tup = r, g, b
    for num in tup:
        if num <= 0:
            output += "00"
        elif num >= 255:
            output += "FF"
        else:
            output += letters[num // 16]
            else:
                output += str(num // 16)
            if letters.get(num % 16):
                output += letters[num % 16]
            else:
                output += str(num % 16)
    return output


# rgb(255, 255, 255) => FFFFFF
print(rgb(255, 255, 255))

# rgb(255, 255, 300) => FFFFFF
print(rgb(255, 255, 300))

# rgb(0,-1,-300) => 000000
print(rgb(0, -1, -300))

# rgb(148, 0, 211))\ => 9400D3
print(rgb(148, 0, 211))
