# Kata practice from codewars
# https://www.codewars.com/kata/546e2562b03326a88e000020/train/python

# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer
# codewars Kata for me to use in practising list comprehension type Python statements

import unittest

def square_digits(num):
    # find square of every integer in num
    # return these as an integer
    # e.g. num = 823, return 1649
    # placeholder pass
    # num is an integer, convert to list or string
    # use list of string to find every square value
    squares = [str(int(x)**2) for x in str(num)]
    squares_string = int("".join(squares))
    return squares_string

class squareDigits(unittest.TestCase):
    
    # tests from kata
    # test.assert_equals(square_digits(9119), 811181)
    
    # test square is returned for one integer
    def test_one_integer_square_returned(self):
        self.assertEqual(square_digits(2),4)
    # test string of integers returns squares
    def test_integer_string_returns_squares(self):
        self.assertEqual(square_digits(9119),811181)

if __name__ == "__main__":
    unittest.main()