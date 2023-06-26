# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.


def create_phone_number(array):
    print(
        f"({str(array[0])}{str(array[1])}{str(array[2])}) {str(array[3])}{str(array[4])}{str(array[5])}-{str(array[6])}{str(array[7])}{str(array[8])}{str(array[9])}"
    )


# createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => returns "(123) 456-7890"
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
