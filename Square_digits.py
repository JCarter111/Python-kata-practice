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
    # number must be an integer
    # integer number could be negative
    # if number is not an integer
    # raise an error
    # note Boolean value for number is interpreted as 0 or 1
    # but can cause code failure
    # raise error if Boolean value provided
    if not(isinstance(num,int)) or isinstance(num,bool):
        raise TypeError("Please provide an integer number")
    # num is an integer, convert to list or string
    # use list of string to find every square value
    squares = int("".join([str(int(x)**2) for x in str(num)]))
    return squares

class squareDigits(unittest.TestCase):
    
    # tests from kata
    # test.assert_equals(square_digits(9119), 811181)
    
    # test square is returned for one integer
    def test_one_integer_square_returned(self):
        self.assertEqual(square_digits(2),4)
    # test larger integer returns squares
    def test_integer_returns_squares(self):
        self.assertEqual(square_digits(9119),811181)

    # test what happens if num is larger than the maximum integer values
    #def test_large_number_returns_squares(self):
    #    self.assertEqual(square_digits(21574864912),412549166436168114)
    # error handling tests
    # test that an error is raised if a non-integer number is 
    # provided
    def test_noninteger_raises_error(self):
        with self.assertRaises(TypeError):
            square_digits(9.5) 
        with self.assertRaises(TypeError):
            square_digits("hello")
        with self.assertRaises(TypeError):
            square_digits([6,7])
        with self.assertRaises(TypeError):
            square_digits(True) 
        #with self.assertRaises(TypeError):
        #    square_digits(2323232323231212312312424)

if __name__ == "__main__":
    unittest.main()