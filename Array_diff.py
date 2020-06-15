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
    # create a new list to store the result of subtracting items in 
    # list b from list a, initially this list contains the same
    # items as a
    # Note: need to use copy here to copy
    # list a by value so that result_list can
    # be modified without a being modified
    result_list = a.copy()

    # loop through list b and remove each item in list b from list a
    # if the values in b are present in a
    for x in b:
        for y in a:
             if x == y: 
                result_list.remove(x)

    # alternative method of looping through the lists   
    # for x in range(len(b)):
    #    for y in range(len(a)):
    #        if b[x] == a[y]:
    #            result_list.remove(b[x])

    return result_list
    

class arrayDiff(unittest.TestCase):
    # kata tests
    # Test.describe("Basic Tests")
    # Test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
    # Test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
    # Test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
    # Test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
    # Test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")

    # test that one number in array b can be removed from array a
    def test_one_number_removed_from_a(self):
        self.assertEqual(array_diff([1,2],[1]),[2])
    # test repeated number in array a is retained and single no. in b removed
    def test_one_number_removed_a_retains_multiple_numbers(self):
        self.assertEqual(array_diff([1,2,2],[1]),[2,2])
    # test repeated number in a is removed if it is present as a single number in b
    def test_multiple_numbers_removed_from_a_single_number_in_b(self):
        self.assertEqual(array_diff([1,2,2],[2]),[1])
    # test two numbers present in b and a are both removed leaving empty list
    def test_two_number_in_b_both_removed(self):
        self.assertEqual(array_diff([1,2], [1,2]),[])
    # test blank list to remove, nothing is removed from a
    def test_no_numbers_to_remove_a_remains_same(self):
        self.assertEqual(array_diff([1,2,2],[]),[1,2,2])
    # test number not present in a but is in b
    def test_number_in_b_not_in_a(self):
        self.assertEqual(array_diff([3,3,4,5,3],[10]),[3,3,4,5,3])
    # test a contains nothing, a stays the same
    def test_no_numbers_in_a_stays_same(self):
        self.assertEqual(array_diff([],[1,2]),[])
    # test works with characters as well as numbers
    def test_non_numeric_characters(self):
        self.assertEqual(array_diff([1,"e",5,"j"],[1,"e"]),[5,"j"])
    
if __name__ == "__main__":
    unittest.main()
