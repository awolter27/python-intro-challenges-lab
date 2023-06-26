# Write a function called `print_contacts` that takes a dictionary of key-value pairs for names and phone numbers, then outputs the `name` with the contact info.
# Try iterating over a dictionary with a for loop and printing out what values come back.

contacts = {"Brian": "333-333-3333", "Lenny": "444-444-4444", "Daniel": "777-777-7777"}


# Option 1:
# def print_contacts(dictonary):
#     for key in dictonary:
#         print(f"{key} has a phone number of {dictonary[key]}")


# Option 2:
def print_contacts(dictonary):
    for key, val in dictonary.items():
        print(f"{key} has a phone number of {val}")


# print_contacts(contacts) =>
# Brian has a phone number of 333-333-3333
# Lenny has a phone number of 444-444-4444
# Daniel has a phone number of 777-777-7777
print_contacts(contacts)
