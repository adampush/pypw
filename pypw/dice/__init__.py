"""A library for parsing and evaluating dice notation."""

from __future__ import absolute_import, print_function, unicode_literals

from pyparsing import ParseException

import dice.elements
import dice.grammar
import dice.utilities

"""The MIT License (MIT)

Copyright (c) 2013 Sam Clements

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

__all__ = ['roll', 'ParseException']
__author__ = "Sam Clements <sam@borntyping.co.uk>"
__version__ = '1.1.0'


def roll(string, single=True, verbose=False):
    """Parses and evaluates a dice expression"""
    ast = dice.grammar.expression.parseString(string, parseAll=True)
    if verbose:
        dice.elements.Element.verbose = True
    result = [element.evaluate_cached(verbose=verbose) for element in ast]
    if single:
        return dice.utilities.single(result)
    return result
