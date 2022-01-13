#WPE Wk1: ISBN Validator
#Author: JRig
#Date: 01/11/2022

from sys import exit
from textwrap import dedent

def validate_isbn(isbn):

    if len(isbn) == 12 or len(isbn) == 13:
        base = 0
        last_digit = 0
        num = []

        for idx, number in isbn:
            if idx % 2 == 0:
                base += int(number)*3
                num.append(number)
            elif idx == 13:
                last_digit = int(number)
            else:
                base += int(number)
                num.append(number)

        added_digit = 10 - (base % 10)

        num.append(str(added_digit))
        num = ''.join(num)

        if len(isbn) == 12:
            print(f"The ISBN is: {num}")
            validate_isbn(list(enumerate(num, start=1)))
        else:
            if added_digit == last_digit:
                print("The ISBN is valid.")
                return True
            else:
                print("The ISBN is not valid.")
                return False
    else:
        print("The ISBN is not valid.")
        return False

def validate_digit(string):

    old_string = list(string)
    new_string = []

    for char in old_string:
        if char.isdigit():
            new_string.append(char)
        else:
            continue
    new_string = ''.join(new_string)

    return new_string

while True:
    print(dedent("""
    \n\t\tWelcome to the ISBN Validator!
    \t\tInput an ISBN to determine if it is valid or not.
    \t\tConversely, enter a 12 digit serial number to create a Valid ISBN.
    \t\tEnter 'EXIT' to quit.
    """))

    isbn = input("\n> ")

    if 'exit' in isbn.lower():
        exit(1)
    else:
        isbn = validate_digit(isbn)
        isbn = list(enumerate(isbn, start=1))
        validate_isbn(isbn)
