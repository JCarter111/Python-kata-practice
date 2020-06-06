# Kata practice from codewars
# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b.

#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:

#array_diff([1,2,2,2,3],[2]) == [1,3]

# import the Python unit test module
import unittest

def array_diff(a, b):
    # remove all elements in list b from list a
    # if an element in list b occurs in list a more than
    # once remove all instances from list a
    difference =[]
    return difference

class arrayDiff(unittest.TestCase):
    # kata tests
    # Test.describe("Basic Tests")
    # Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    # Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    # Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    # Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    # Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

    # test number is zero
    def test_number_zero_returns_zero(self):
       self.assertEqual(array_diff([1,2],[1]),[2])
    # test for single multiple of 3
    #def test_four_returns_three(self):
    #    self.assertEqual(array_diff(4),3)
    # test number three should return total of zero
    #def test_three_returns_zero(self):
    #   self.assertEqual(array_diff(3),0)
    # test number five should only return 3, not include 5
    #def test_five_returns_three(self):
    #    self.assertEqual(array_diff(5),3)
    # test for a single multiple of 5 (will also have multiple of 3)
    # test six
    #def test_five_returns_eight(self):
    #    self.assertEqual(countMultiples3And5(6),8)
    # test in the kata spec
    # number = 10, return value = 23
    #def test_ten_returns_twentythree(self):
    #    self.assertEqual(countMultiples3And5(10),23)
    # test for a large number
    #def test_thirtyeight_returns_358(self):
    #    self.assertEqual(countMultiples3And5(38),329)
    # test negative number
    #def test_minusthirtyeight_returns_minus358(self):
    #    self.assertEqual(countMultiples3And5(-38),-329)
    # test number = 1
    #def test_one_returns_zero(self):
    #    self.assertEqual(countMultiples3And5(1),0)

    # error handling tests
    # test that an error is raised if a non-integer number is 
    # provided
    #def test_noninteger_raises_error(self):
    #    with self.assertRaises(TypeError):
    #        countMultiples3And5(9.5) 
    #    with self.assertRaises(TypeError):
    #        countMultiples3And5("hello")
    #    with self.assertRaises(TypeError):
    #        countMultiples3And5([6,7])
    #    with self.assertRaises(TypeError):
    #        countMultiples3And5(True)
    
if __name__ == "__main__":
    unittest.main()