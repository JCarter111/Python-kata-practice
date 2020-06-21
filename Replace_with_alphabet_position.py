
# codewars python kata
# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# import the Python unit test module
import unittest
# import module to generate random numbers for use in testing
import random

def alphabet_position(text):

    # convert each character in text to lower case
    # remove spaces from text string - replace function
    # only need to convert alphabetic characters, ignore e.g. "."
    # match against lower case alphabet list
    # find position in the list of the match and use this to determine 
    # alphabet position, which is position in list + 1 
    # as list position starts from 0

    lookupString = "abcdefghijklmnopqrstuvwxyz"
    returnList =[]
    returnString = ""
    if len(text) > 0:
        for item in text:
            # use the look up string to find the position in the alphabet
            # of the current letter
            # need to add 1 to the position returned because position starts at zero
            # convert the current item to lowercase before using the lookup string
            # convert the alphabet postion number to a string
            if lookupString.find(item.lower()) >= 0:
                returnList.append(str(lookupString.find(item.lower()) + 1))
    # join the list to create a string with each string separated by a space
    if len(returnList) > 0:
        returnString = " ".join(returnList)
    return returnString
   # pass


class alphabetPosition(unittest.TestCase):
    
    # tests from kata

    #from random import randint
    #test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
    #test.assert_equals(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

    #number_test = ""
    #for item in range(10):
    #    number_test += str(randint(1, 9))
    #test.assert_equals(alphabet_position(number_test), "")

    # test empty text string returns empty string output
    def test_blank_string_returns_blank(self):
        self.assertEqual(alphabet_position(""),"")

    # test one letter text string returns one alphabet position
    def test_one_letter_returns_number(self):
        self.assertEqual(alphabet_position("j"),"10")

    # test that a text string containing just a space does not return any value
    def test_one_space_returns_blank(self):
        self.assertEqual(alphabet_position(" "),"")

    # test long string of characters, mixed case
    # punctuation and space should be ignored
    # upper case values should show the correct alphabet postion, the same as the corresponding
    # lower case value
    def test_multiple_mixed_characters_spaces_punctuation(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."),"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."),"20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")
    
    # test that a text string containing just a space does not return any value
    def test_numbers_return_blank(self):
        number_test = ""
        for item in range(10):
            number_test += str(random.randint(1,9))
        print(number_test)
        self.assertEqual(alphabet_position(number_test),"")


if __name__ == "__main__":
    unittest.main()

