"""Generate passwords using a simplified diceware method.

This module provides functions to generate passwords using a somewhat simplified diceware method. Special characters
and numerals are not currently supported, but could be added manually after password is generated.

Example of basic usage:
    >>> pypw.generate(6)
    13312 -> grasp
    13233 -> given
    16432 -> unit
    13621 -> lake
    15432 -> skid
    13165 -> fruit
    GraspGivenUnitLakeSkidFruit
"""
from __future__ import absolute_import, print_function, unicode_literals

from pyparsing import ParseException

import pypw.dice as dice
import csv
import os

__all__ = ['roll', 'ParseException']
__author__ = "Adam Push"
__version__ = '0.1'

# This code should get executed on import. This will read in the tab-delimited wordlist file and convert it into a
# dictionary keyed on numerical codes so that we can easily look up words that match our rolls.
# TODO: we are doing the same thing three times here, could consolidate. Perhaps turn into function so can unit-test
sep = os.sep
file_path = os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_1.txt'
with open(file_path, 'r') as file:
    list_of_lists = list(csv.reader(file, delimiter='\t'))
    WORD_LIST_EFF_SMALL_1 = {list_item[0]: list_item[1] for list_item in list_of_lists}

file_path = os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_2.txt'
with open(file_path, 'r') as file:
    list_of_lists = list(csv.reader(file, delimiter='\t'))
    WORD_LIST_EFF_SMALL_2 = {listItem[0]: listItem[1] for listItem in list_of_lists}

file_path = os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_large_wordlist.txt'
with open(file_path, 'r') as file:
    list_of_lists = list(csv.reader(file, delimiter='\t'))
    WORD_LIST_EFF_LARGE = {listItem[0]: listItem[1] for listItem in list_of_lists}

# TODO: I think these constants should be relocated to just after the import statements
DIE_STRING_EFF_SMALL = '4d6'  # Roll 4d6 per roll if the wordlist is one of the two EFF "small" lists
DIE_STRING_EFF_LARGE = '5d6'  # Roll 5d6 per roll if the wordlist is the large EFF list (not implemented)
# For some reason the source txt file for the EFF small wordlist #1 has only four digits that vary but it has one
# constant digit in the MSB position that is constant=1.
EFF_SMALL_1_PREFIX_HACK = '1'

DEFAULT_NUM_WORDS = 6  # Default number of words is 6... avoid magic numbers


def generate(num_words=DEFAULT_NUM_WORDS, word_list_to_use=WORD_LIST_EFF_SMALL_1):
    """Generate a diceware password. If called with no arguments, generates a
    six-word password using the EFF "Small Wordlist #1."

    :type num_words: integer
    :param word_list_to_use:
    :param num_words:
    :return:
    """

    if word_list_to_use == WORD_LIST_EFF_SMALL_1 or WORD_LIST_EFF_SMALL_2:
        die_string_to_use = DIE_STRING_EFF_SMALL
    elif word_list_to_use == WORD_LIST_EFF_LARGE:
        die_string_to_use = DIE_STRING_EFF_LARGE
    else:
        die_string_to_use = DIE_STRING_EFF_SMALL

    # TODO: this is ugly but works, maybe split into two separate expressions for readability
    code_list = [''.join([str(die) for die in roll(die_string_to_use)]) for i in range(0, num_words)]

    if word_list_to_use == WORD_LIST_EFF_SMALL_1:
        password_word_list = [word_list_to_use[EFF_SMALL_1_PREFIX_HACK + code_string] for code_string in code_list]
    else:
        password_word_list = [word_list_to_use[code_string] for code_string in code_list]

    # After we are done, print the constructed password to the stdout.
    for a, b in zip(code_list, password_word_list):
        print("{} --> {}".format(a, b))
    print(''.join([word.title() for word in password_word_list]))


def roll(string, single=True, verbose=False):
    """Roll dice using dice notation (e.g. 2d6)

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
