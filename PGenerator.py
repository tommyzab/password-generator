import random
import string
import argparse

# Declaring letters, numbers & unique symbols (used a tuple because it's immutable)
lower_case = tuple(string.ascii_lowercase)
upper_case = tuple(string.ascii_uppercase)
numbers = tuple(x for x in range(0, 10))
symbols = tuple(string.punctuation)


# The function that creates the whole password
def generate(length: int, duplicates: bool, symbol: bool, number: bool, lower: bool, upper: bool):
    temp_list = []
    generated_password = []

    # Filling up the temporary list with the wanted values
    if upper:
        temp_list.extend(upper_case)
    if lower:
        temp_list.extend(lower_case)
    if number:
        temp_list.extend(numbers)
    if symbol:
        temp_list.extend(symbols)

    pass_len = 0

    # Creating a random password based on the values are stored in temp_list into a new list
    while pass_len < length:
        # A random character
        letter = random.choice(temp_list)

        # Non repeated values
        # Preventing duplicates until we reach the maximum options for unique values (for long passwords)
        if duplicates and pass_len < len(temp_list) and letter in generated_password:
            continue

        generated_password.append(letter)
        pass_len += 1

    return "".join(map(str, generated_password))

# (CLI) argeparse configuration
def build_argparse():
    parser = argparse.ArgumentParser(usage='use "python %(prog)s --help" for more information',
                                     description='Password Generator - To dismiss any group of characters, '
                                                 'include their flag while calling the script')

    required_named = parser.add_argument_group('required named arguments')
    required_named.add_argument('-l', '--length', type=int, required=True, metavar='',
                                help='The length of the password')

    parser.add_argument('-D', '--duplicates', required=False, action='store_false', help='Duplicates')
    parser.add_argument('-U', '--upper', required=False, action='store_false', help='Upper case letters')
    parser.add_argument('-L', '--lower', required=False, action='store_false', help='Lower case letters')
    parser.add_argument('-N', '--number', required=False, action='store_false', help='Numbers')
    parser.add_argument('-S', '--symbol', required=False, action='store_false', help='Symbols')

    return parser.parse_args()


if __name__ == '__main__':
    print('\n' + 'Password Generator'.center(50, '*'))

    args = build_argparse()

    # Letting the user know that if the inserted number has no length, there won't be any output
    assert args.length > 0, 'Password length has to be strictly positive'
    
    # The returned value (printed password)
    print(f'\n Generated password: {generate(**vars(args))} \n')
