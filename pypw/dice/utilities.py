"""TODO: write docstring"""
from __future__ import absolute_import, unicode_literals

import warnings

import pyparsing

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

def classname(obj):
    """Returns the name of an objects class"""
    return obj.__class__.__name__


def single(iterable):
    """Returns a single item if the iterable has only one item"""
    return iterable[0] if len(iterable) == 1 else iterable


def patch_pyparsing(packrat=True, arity=True):
    """Applies monkey-patches to pyparsing"""
    if packrat:
        enable_pyparsing_packrat()

    if arity:
        disable_pyparsing_arity_trimming()


def enable_pyparsing_packrat():
    """Enables pyparsing's packrat parsing, which is much faster for the type
    of parsing being done in this library"""
    warnings.warn("Enabled pyparsing packrat parsing", ImportWarning)
    pyparsing.ParserElement.enablePackrat()


def _trim_arity(func, maxargs=None):
    def wrapper(string, location, tokens):
        return func(string, location, tokens)
    return wrapper


def disable_pyparsing_arity_trimming():
    """When pyparsing encounters a TypeError when calling a parse action, it
    will keep trying the call the function with one less argument each time
    until it succeeds. This disables this functionality, as it catches
    TypeErrors raised by other functions and makes debugging those functions
    very hard to do."""
    warnings.warn("Disabled pyparsing arity trimming", ImportWarning)
    pyparsing._trim_arity = _trim_arity


def addevensubodd(name="", a=0, b=0, *args, **kwds):
    """Add even numbers, subtract odd ones. See http://1w6.org/w6 """
    def _subodd(a):
        if a % 2:
            return - a
        else:
            return a
    if b:
        return a + _subodd(b)
    return _subodd(a)
