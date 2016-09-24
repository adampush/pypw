from __future__ import absolute_import

from pyparsing import Literal

from py.test import raises

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

def test_enable_pyparsing_packrat_parsing():
    """Test that packrat parsing was enabled"""
    import pyparsing
    assert pyparsing.ParserElement._packratEnabled is True


def test_disable_pyparsing_arity_trimming():
    """Test that pyparsing._trim_arity has been replaced"""
    import pyparsing
    import dice.utilities
    assert pyparsing._trim_arity is dice.utilities._trim_arity


def test_disable_pyparsing_arity_trimming_works():
    """Tests that arity trimming has been disabled and parse actions with
    the wrong number of arguments will raise TypeErrors"""
    for func in [lambda a: None, lambda a, b: None, lambda a, b, c, d: None]:
        element = Literal('test').setParseAction(func)
        with raises(TypeError):
            element.parseString('test')
