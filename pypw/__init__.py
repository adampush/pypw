from __future__ import absolute_import, print_function, unicode_literals

from pyparsing import ParseException

import dice
import csv
import os

__all__ = ['roll', 'ParseException']
__author__ = "Adam Push"
__version__ = '0.1'

# This code should get executed on import. This will read in the tab-delimited wordlist file and convert it into a
# dictionary keyed on a numerical code so that we can easily look up words that match our rolls.
sep = os.sep
list_of_lists = list(csv.reader(open(os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_1.txt',
                                     'r'), delimiter='\t'))
WORD_LIST_EFF_SMALL_1 = dict()
for listItem in list_of_lists:
    WORD_LIST_EFF_SMALL_1[listItem[0]] = listItem[1]

list_of_lists = list(csv.reader(open(os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_2.txt',
                                     'r'), delimiter='\t'))
WORD_LIST_EFF_SMALL_2 = dict()
for listItem in list_of_lists:
    WORD_LIST_EFF_SMALL_2[listItem[0]] = listItem[1]

list_of_lists = list(csv.reader(open(os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_large_wordlist.txt',
                                     'r'), delimiter='\t'))
WORD_LIST_EFF_LARGE = dict()
for listItem in list_of_lists:
    WORD_LIST_EFF_LARGE[listItem[0]] = listItem[1]

DIE_STRING_EFF_SMALL = '4d6'  # Roll 4d6 per roll if the wordlist is one of the two EFF "small" lists
DIE_STRING_EFF_LARGE = '5d6'  # Roll 5d6 per roll if the wordlist is the large EFF list (not implemented)

# For some reason the source txt file for the EFF small wordlist #1 has only four digits that vary but it has one
# constant digit in the MSB position that is constant=1.
EFF_SMALL_1_PREFIX_HACK = '1'

DEFAULT_NUM_WORDS = 6  # Default number of words is 6... avoid magic numbers


def generate(num_words=DEFAULT_NUM_WORDS, word_list_to_use=WORD_LIST_EFF_SMALL_1):
    """

    :type num_words: int
    :param word_list_to_use:
    :param num_words:
    :return:
    """

    roll_list = []  # A List for storing roll results (as strings)
    constructed_password = ''  # Empty string which will become the password eventually
    # For each desired word, do a dice roll, look up a match in a word list, and store results.
    for i in range(0, num_words):
        # TODO: eliminate redundancy in these if/elif cases
        if word_list_to_use == WORD_LIST_EFF_SMALL_1:
            # Roll the "appropriate" number of dice for the chosen word list
            dice_roll_list = dice.roll(DIE_STRING_EFF_SMALL)
            # word_code_str will become a code string of N characters, each character is a numeral representing one die
            # result. This must be seeded with a prefix character '1' because we are using the EFF "small" wordlist and
            # all its entries start with a '1' for some reason.
            word_code_str = EFF_SMALL_1_PREFIX_HACK
            # The roll is returned as a list of individual numbers (die results) so concatenate each die number as a
            # string to form a single N-digit code number
            for die in dice_roll_list:
                word_code_str += str(die)
            # Store the N-digit code in a list
            roll_list.append(word_code_str)  # TODO: this is not used. Do something with it?
            # Use the Convert matching word to Title Case and append to password string variable
            constructed_password += str(WORD_LIST_EFF_SMALL_1[word_code_str]).title()
            print(word_code_str + ' -> ' + WORD_LIST_EFF_SMALL_1[word_code_str])
        elif word_list_to_use == WORD_LIST_EFF_SMALL_2:
            # Roll the "appropriate" number of dice for the chosen word list
            dice_roll_list = dice.roll(DIE_STRING_EFF_SMALL)
            # word_code_str will become a code string of N characters, each character is a numeral representing one die
            # result.
            word_code_str = ''
            # The roll is returned as a list of individual numbers (die results) so concatenate each die number as a
            # string to form a single N-digit code number
            for die in dice_roll_list:
                word_code_str += str(die)
            # Store the N-digit code in a list
            roll_list.append(word_code_str)  # TODO: this is not used. Do something with it?
            # Use the Convert matching word to Title Case and append to password string variable
            constructed_password += str(WORD_LIST_EFF_SMALL_2[word_code_str]).title()
            print(word_code_str + ' -> ' + WORD_LIST_EFF_SMALL_2[word_code_str])
        elif word_list_to_use == WORD_LIST_EFF_LARGE:
            # Roll the "appropriate" number of dice for the chosen word list
            dice_roll_list = dice.roll(DIE_STRING_EFF_LARGE)
            # word_code_str will become a code string of N characters, each character is a numeral representing one die
            # result. This must be seeded with a prefix character '1' because we are using the EFF "small" wordlist and
            # all its entries start with a '1' for some reason.
            word_code_str = ''
            # The roll is returned as a list of individual numbers (die results) so concatenate each die number as a
            # string to form a single N-digit code number
            for die in dice_roll_list:
                word_code_str += str(die)
            # Store the N-digit code in a list
            roll_list.append(word_code_str)  # TODO: this is not used. Do something with it?
            # Use the Convert matching word to Title Case and append to password string variable
            constructed_password += str(WORD_LIST_EFF_LARGE[word_code_str]).title()
            print(word_code_str + ' -> ' + WORD_LIST_EFF_LARGE[word_code_str])
        else:
            pass
    # After we are done, print the constructed password to the stdout.
    print(constructed_password)


def roll(string, single=True, verbose=False):
    """

    :param string:
    :param single:
    :param verbose:
    :return:
    """

    return dice.roll(string, single, verbose)


def test():
    """This is just a test function for playing with things."""

    print(os.path.dirname(__file__))

    sep = os.sep
    lol = list(csv.reader(open(os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_1.txt', 'r'),
                          delimiter='\t'))
    print(lol)
