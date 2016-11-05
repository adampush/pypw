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

import pypw.dice as dice
import csv
import os
import random

__author__ = "Adam Push"
__version__ = '0.1'

DIE_STRING_EFF_SMALL = '4d6'  # Roll 4d6 per roll if the wordlist is one of the two EFF "small" lists
DIE_STRING_EFF_LARGE = '5d6'  # Roll 5d6 per roll if the wordlist is the large EFF list
DICE_NUM_EFF_SMALL = 4
DICE_NUM_EFF_LARGE = 5
# For some reason the source txt file for the EFF small wordlist #1 has only four digits that vary but it has one
# constant digit in the MSB position that is constant=1.
EFF_SMALL_1_PREFIX_HACK = '1'

DEFAULT_NUM_WORDS = 6


# This code should get executed on import. This will read in the tab-delimited wordlist file and convert it into a
# dictionary keyed on numerical codes so that we can easily look up words that match our rolls.
def _import_word_lists(file_path):
    with open(file_path, 'r') as file:
        list_of_lists = list(csv.reader(file, delimiter='\t'))
        return {list_item[0]: list_item[1] for list_item in list_of_lists}

# Create word list dictionaries
sep = os.sep
file_path = os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_1.txt'
WORD_LIST_EFF_SMALL_1 = _import_word_lists(file_path)

file_path = os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_small_wordlist_2.txt'
WORD_LIST_EFF_SMALL_2 = _import_word_lists(file_path)

file_path = os.path.dirname(__file__) + sep + 'wordlists' + sep + 'eff_large_wordlist.txt'
WORD_LIST_EFF_LARGE = _import_word_lists(file_path)


def generate(num_words=DEFAULT_NUM_WORDS, word_list_to_use=WORD_LIST_EFF_LARGE):
    """Generate a diceware password. If called with no arguments, generates a
    six-word password using the EFF "Large Word List."

    :type num_words: integer
    :param word_list_to_use:
    :param num_words:
    :return:
    """

    # Decide which word list to use based on function argument
    # if word_list_to_use is WORD_LIST_EFF_SMALL_1:
    #     die_string_to_use = DIE_STRING_EFF_SMALL
    # elif word_list_to_use is WORD_LIST_EFF_SMALL_2:
    #     die_string_to_use = DIE_STRING_EFF_SMALL
    # elif word_list_to_use is WORD_LIST_EFF_LARGE:
    #     die_string_to_use = DIE_STRING_EFF_LARGE
    # else:
    #     die_string_to_use = DIE_STRING_EFF_SMALL

    if word_list_to_use is WORD_LIST_EFF_SMALL_1:
        die_string_to_use = DICE_NUM_EFF_SMALL
    elif word_list_to_use is WORD_LIST_EFF_SMALL_2:
        die_string_to_use = DICE_NUM_EFF_SMALL
    elif word_list_to_use is WORD_LIST_EFF_LARGE:
        die_string_to_use = DICE_NUM_EFF_LARGE
    else:
        die_string_to_use = DICE_NUM_EFF_SMALL

    # Create code list from die rolls
    code_list = []
    for i in range(num_words):
        # code_list.append(''.join([str(die) for die in roll(die_string_to_use)]))
        code_list.append(''.join([str(die) for die in roll_d6(die_string_to_use)]))

    # Older, less readable way to create code list from die rolls
    # code_list = [''.join([str(die) for die in roll(die_string_to_use)]) for i in range(0, num_words)]

    # Use the code list to look up words in the word list and add them to the password list. If the word list is
    # "EFF Small #1", apply the "prefix hack" to prepend each word code with a prefix (this is due to the word
    # list file being a little wonky). TODO: should fix the source wordlist file so we do not have to do this.
    if word_list_to_use is WORD_LIST_EFF_SMALL_1:
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

    # TODO: using the dice library is way overkill. Rewrite to just use "random" module

    return dice.roll(string, single, verbose)


def roll_d6(num_dice):
    """Roll a number of six-sided dice and return the results.

    :param num_dice: Number of dice to roll
    :return: A List containing numdice 1d6 die roll results.
    """

    result = []
    for i in range(num_dice):
        result.append(random.randint(1, 6))

    return result
