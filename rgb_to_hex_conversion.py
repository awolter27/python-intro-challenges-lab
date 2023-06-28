# The RGB function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# **Note**: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Option 1 from Eric Fithian:
# I believe he had to import something. I was unable to get this solution to work.
# from matplotlib.colors import rgb2hex


# def rgb(r, g, b):
#     return rgb2hex(r, g, b)


# Option 2 from Eric Fithian:
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
            if letters.get(num // 16):
                output += letters[num // 16]
            else:
                output += str(num // 16)
            if letters.get(num % 16):
                output += letters[num % 16]
            else:
                output += str(num % 16)
    return output


# Option 3 from Dylan Silvergate:
# I believe he had to import something. I was unable to get this solution to work.
# def rgb_hex_code(num):
#     hex_code = "#{:02x}{:02x}{:02x}".format(*num)
#     return hex_code


# rgb_values = (255, 255, 255)
# hex_color = rgb_hex_code(rgb_values)
# print(hex_color)


# Option 4 from John Joyce:
# def check_rgb(num):
#     if num < 0:
#         return 0
#     elif num > 255:
#         return 255
#     return num


# def rgb(r, g, b):
#     valid_rgb = tuple(map(check_rgb, (r, g, b)))
#     hex_string = "%02X%02X%02X" % (valid_rgb)
#     return hex_string


# rgb(255, 255, 255) => FFFFFF
print(rgb(255, 255, 255))

# rgb(255, 255, 300) => FFFFFF
print(rgb(255, 255, 300))

# rgb(0,-1,-300) => 000000
print(rgb(0, -1, -300))

# rgb(148, 0, 211))\ => 9400D3
print(rgb(148, 0, 211))
