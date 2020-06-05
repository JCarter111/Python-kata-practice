# Kata practice from codewars
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

# import the Python unit test module
import unittest

def countMultiples3And5(number):
# find sum of all the multiples of 3 and 5
# below the number provided
# e.g. number = 10
# multiples of 5 are 5 (note below the number 10)
# multipes of 3 are 3,6,9
# total sum is 5 + 3 + 6 + 9 = 23

# number must be an integer
# number can be negative
# if number is not an integer
# raise an error
# note Boolean value for number is interpreted as 0 or 1
# raise error if Boolean value provided
    if not(isinstance(number,int)) or isinstance(number,bool):
       raise TypeError("Please provide an integer number")
 

# loop counting up from 3 to the number
# or down from -3 to number if number is negative

# in each loop divide number by 3 and by 5
# if the remainder is zero in either case, add the current 
# number to the total score

    # initially set store of total multiples to zero    
    totalMultiples = 0

    

    # if number is less than 3 and greater than -3 
    # there are no multiples of 3 and 5
    # no further processing required

    if number >= 3:  
        # set counter for loop to number, start checking at value 3
        #loopCounter = 3 
        # loop through integers starting at 3 and less than number
        for loopCounter in range(3,number):   
            if loopCounter%3 == 0 or loopCounter%5 == 0:
                totalMultiples = totalMultiples + loopCounter
    elif number <= -3:
        # set counter for loop to negative number, start checking a value - 3
        #loopCounter = -3
        # loop through negative integers starting at -3 and greater than negative number
        for loopCounter in range(-3,number,-1):
            if loopCounter%3 ==0 or loopCounter%5 ==0:
                totalMultiples = totalMultiples + loopCounter
    return totalMultiples


# tests
# using unittest to run testing

# example test provided for the kata
#test.describe("Multiples of 3 and 5")
#test.it("should handle basic cases")
#test.assert_equals(solution(10), 23)


class multiple3And5Tests(unittest.TestCase):

    # test number is zero
    def test_number_zero_returns_zero(self):
        self.assertEqual(countMultiples3And5(0),0)
    # test for single multiple of 3
    def test_four_returns_three(self):
        self.assertEqual(countMultiples3And5(4),3)
    # test number three should return total of zero
    def test_three_returns_zero(self):
       self.assertEqual(countMultiples3And5(3),0)
    # test number five should only return 3, not include 5
    def test_five_returns_three(self):
        self.assertEqual(countMultiples3And5(5),3)
    # test for a single multiple of 5 (will also have multiple of 3)
    # test six
    def test_five_returns_eight(self):
        self.assertEqual(countMultiples3And5(6),8)
    # test in the kata spec
    # number = 10, return value = 23
    def test_ten_returns_twentythree(self):
        self.assertEqual(countMultiples3And5(10),23)
    # test for a large number
    def test_thirtyeight_returns_358(self):
        self.assertEqual(countMultiples3And5(38),329)
    # test negative number
    def test_minusthirtyeight_returns_minus358(self):
        self.assertEqual(countMultiples3And5(-38),-329)
    # test number = 1
    def test_one_returns_zero(self):
        self.assertEqual(countMultiples3And5(1),0)

    # error handling tests
    # test that an error is raised if a non-integer number is 
    # provided
    def test_noninteger_raises_error(self):
        with self.assertRaises(TypeError):
            countMultiples3And5(9.5) 
        with self.assertRaises(TypeError):
            countMultiples3And5("hello")
        with self.assertRaises(TypeError):
            countMultiples3And5([6,7])
        with self.assertRaises(TypeError):
            countMultiples3And5(True)
    
if __name__ == "__main__":
    unittest.main()