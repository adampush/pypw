from __future__ import absolute_import

from dice.elements import Integer, Roll, Dice, Total
from dice import roll

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

class TestElements(object):
    def test_integer(self):
        assert isinstance(Integer(1), int)

    def test_dice_from_iterable(self):
        d = Dice.from_iterable((2, 6))
        assert d.amount == 2 and d.sides == 6

    def test_dice_from_string(self):
        d = Dice.from_string('2d6')
        assert d.amount == 2 and d.sides == 6

    def test_roll(self):
        amount, sides = 6, 6
        assert len(Roll.roll(amount, sides)) == amount
        assert (1 * sides) <= sum(Roll.roll(amount, sides)) <= (amount * sides)


class TestEvaluate(object):
    def test_cache(self):
        """Test that evaluation returns the same result on successive runs"""
        roll('6d(6d6)t')
        ast = Total(Dice(6, Dice(6, 6)))
        assert ast.evaluate_cached() is ast.evaluate_cached()
