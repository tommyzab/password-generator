import random
import string
import argparse

# Declaring letters, numbers & unique symbols (used a tuple because it's immutable)
lower_case = tuple(string.ascii_lowercase)
upper_case = tuple(string.ascii_uppercase)
numbers = tuple(x for x in range(0, 10))
symbols = tuple(string.punctuation)


# Adding cli arguments with the 'argparse' module
parser = argparse.ArgumentParser(usage='use "%(prog)s --help" for more information', description='Password Generator - To dismiss any group of characters, include their flag while calling the script')
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-l', '--length', type=int, required=True, metavar='', help='The length of the password')
parser.add_argument('-D', '--duplicates', required=False, action='store_false', help='Duplicates')
parser.add_argument('-U', '--upper', required=False, action='store_false', help='Upper case letters')
parser.add_argument('-L', '--lower', required=False, action='store_false', help='Lower case letters')
parser.add_argument('-N', '--number', required=False, action='store_false', help='Numbers')
parser.add_argument('-S', '--symbol', required=False, action='store_false', help='Symbols')
args = parser.parse_args()


def Generate(**kwargs):
    
    temp_list = []
    generated_password = []

    # Filling up the temporary list with the wanted values
    if args.upper == True:
        temp_list.extend(upper_case)
    if args.lower == True:
        temp_list.extend(lower_case)
    if args.number == True:
        temp_list.extend(numbers)
    if args.symbol == True:
        temp_list.extend(symbols)
    
    # Randomly creating a password from the values within the temp_list into a new list
    while len(generated_password) < args.length:
        letter = random.choice(temp_list)
        # Non repeated values
        if args.duplicates == True:
            # till we reach the maximum options for unique values
            if len(generated_password) < len(temp_list):
                if letter in generated_password:
                    continue
        generated_password.append(letter)
    
    return print("".join(map(str, generated_password)))


if __name__ == '__main__':
    # Inserting a new line for a cleaner output (nothing more really)
    print("")
    
    # Letting the user know that if the inserted number has no length, there won't be any output
    if args.length < 1:
        print("Please enter a valid number that could represent a length for the new password")
    
    Generate(**vars(args))

