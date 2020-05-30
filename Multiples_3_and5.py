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

# check that the number supplied is an integer
# if it is not, return zero
#    if not(isinstance(number,int)):
#        return 0
# loop counting up from 3 to the number
# in each loop divide number by 3 and by 5
# if the remainder is zero in either case, add the current 
# number to the total score

    # initially set store of total multiples to zero    
    totalMultiples = 0

    # set counter for loop to number, start checking at value 3
    loopCounter = 3

    #loop through all integers less than number
    while loopCounter < number:   
        if loopCounter%3 == 0 or loopCounter%5 == 0:
            totalMultiples = totalMultiples + loopCounter
        loopCounter = loopCounter + 1

    return totalMultiples


# tests
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
    # test non integer number
    #def test_noninteger_returns_multiples(self):
    #    self.assertEqual(countMultiples3And5(10.5),23) 

    # test single t34
    #def test_one_t34_costs_99(self):
    #    self.assertEqual(checkout(["t34"]),99) 

    # test a99, b15
    #def test_one_a99_and_one_b15_costs_80(self):
    #    self.assertEqual(checkout(["a99","b15"]),80)

    # test c40 and t34
    #def test_one_c40_and_one_t34_costs_159(self):
    #    self.assertEqual(checkout(["c40","t34"]),159)
    # test b15 and t34
    #def test_one_b15_and_one_t34_costs_129(self):
    #    self.assertEqual(checkout(["b15","t34"]),129)

    # test one of each item in list
    #def test_one_a99_one_t34_and_one_c40_and_one_b15_costs_189(self):
    #    self.assertEqual(checkout(["t34","c40","b15","a99"]),239)

    # test that discount is applied to 2 * b15 when no other items present
    #def test_two_b15_costs_45(self):
    #    self.assertEqual(checkout(["b15","b15"]),45)

    # test that discount is applied to 3 * a99 when no other items present
    #def test_three_a99_costs_130(self):
    #    self.assertEqual(checkout(["a99","a99","a99"]),130)

    # test that discount is applied to 2 * b15 when other items present
    #def test_two_b15_and_c40_costs_105(self):
    #    self.assertEqual(checkout(["b15","c40","b15"]),105)

    # test that discount is applied to 3 * a99 when other items present
    #def test_three_a99_and_c40_costs_190(self):
    #    self.assertEqual(checkout(["a99","c40","a99","a99"]),190)

    # test deduction applied to three items when 4 * a99 in the checkout items
    #def test_four_a99(self):
    #    self.assertEqual(checkout(["a99","a99","a99","a99"]),180)

    # test deduction applied to two items when 3 * b15 in the checkout items
    #def test_three_b15(self):
    #    self.assertEqual(checkout(["b15","b15","b15"]),75)

    # test deduction applied more than once e.g. 7 * a99, 11 * b15
    # items in random order
    #def test_seven_a99_eleven_b15(self):
    #    self.assertEqual(
    #        checkout(["a99","b15","b15","b15","a99","b15","b15","a99","b15","a99","b15","b15","a99","a99","b15","b15","a99","b15"]),
    #        565)

    # test deduction applied more than one, with other items in the basket
    #def test_nine_a99_seven_b15_two_c40_three_t34(self):
    #    self.assertEqual(
    #        checkout(["c40","a99","t34","b15","b15","a99","b15","c40","a99","b15","a99","b15","t34","t34","b15","a99","a99","b15","a99","a99","a99"]),
    #        972)
if __name__ == "__main__":
    unittest.main()