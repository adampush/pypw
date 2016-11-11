import unittest
from pypw import roll_d6


class Roll_d6_Test_Case(unittest.TestCase):
    """Tests for `pypw.py`."""

    def test_roll_six_dice(self):
        """If we roll six d6, do we get a list of six d6 numbers back?"""
        self.assertTrue(len(roll_d6(6)) == 6)

    def test_roll_one_hundred_dice(self):
        """If we roll one hundred d6, do we get a list of one hundred d6 numbers?"""
        self.assertTrue(len(roll_d6(100)) == 100)

    def test_roll_zero_hundred_dice(self):
        """If we roll zero d6, do we get a list of zero d6 numbers?"""
        self.assertTrue(len(roll_d6(0)) == 0)

    def test_returns_list_of_ints(self):
        """If we do a roll, do we get a list of integers back?"""
        # Make a test roll
        testroll = roll_d6(1000)
        # Check if test roll is a list
        self.assertIsInstance(testroll, list)
        # Check if each item in test roll is an int
        for x in testroll:
            self.assertIsInstance(x, int)

    def test_dice_roll_d6_stats(self):
        """Are we rolling d6 type dice and is number distribution correct?"""
        hist = [0 for i in range(6)]
        N = 6000
        for roll in roll_d6(N):
            # Always should be greater than or equal to one
            self.assertGreaterEqual(roll, 1)
            # Always should be less than or equal to six
            self.assertLessEqual(roll, 6)
            # Increment appropriate histogram bucket
            hist[roll - 1] += 1
        # Expected number of hits for each possible outcome is N/6 for Nd6
        # e.g. 1000 of each outcome expected for 6000 rolls
        count = 1
        for outcome in hist:
            # print('Count of outcome {} is {}'.format(count, outcome))
            count += 1
            self.assertLessEqual(outcome, N/6 + 200)
            self.assertGreaterEqual(outcome, N/6 - 200)

if __name__ == '__main__':
    unittest.main()
