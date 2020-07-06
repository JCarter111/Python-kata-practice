import unittest

def is_prime(num):
# return true if num is a prime number
# return false if num is not a prime number
# a prime number (or a prime) is a natural number
# greater than 1 that has no positive divisors other than 1 and itself.
# check values in the range 2 to num-1
# if any num is exactly divisible by any value in this range
# then num is not a prime number
# need to be able to check negative numbers to determine 
# whether they are prime numbers

    # set default return value to False, number is not a prime number
    numIsPrime = False

    # zero, 1, and -1 are not prime numbers
    # only need to check numbers that are greater than or equal
    # to two or less than or equal to minus two
    if  num != 0 and abs(num) != 1:
        # check every value from 2 to num
        # if num divided by any value of x does
        # not leave a remainder then num is not a prime
        # number
        # set default to return True, number is a prime number
        numIsPrime = True

        for x in range(2,num):
            if num % x == 0: numIsPrime = False

    return numIsPrime
# kata tests
#@Test.describe("Basic")
#def basic():
    
 #   @Test.it("Basic tests")
#    def basic_tests():
#        Test.assert_equals(is_prime(0),  False, "0  is not prime")
#        Test.assert_equals(is_prime(1),  False, "1  is not prime")
 #       Test.assert_equals(is_prime(2),  True, "2  is prime")
 #       Test.assert_equals(is_prime(73), True, "73 is prime")
 #       Test.assert_equals(is_prime(75), False, "75 is not prime")
 #       Test.assert_equals(is_prime(-1), False, "-1 is not prime")

    
#    @Test.it("Test prime")
#    def test_prime():
#        Test.assert_equals(is_prime(3),  True, "3  is prime");
#        Test.assert_equals(is_prime(5),  True, "5  is prime");
#       Test.assert_equals(is_prime(7),  True, "7  is prime");
#        Test.assert_equals(is_prime(41), True, "41 is prime");
#       Test.assert_equals(is_prime(5099), True, "5099 is prime");
        
#    @Test.it("Test not prime")
#    def test_not_prime():
#Test.assert_equals(is_prime(4),  False, "4  is not prime");
#        Test.assert_equals(is_prime(6),  False, "6  is not prime");
#        Test.assert_equals(is_prime(8),  False, "8  is not prime");
#        Test.assert_equals(is_prime(9), False, "9 is not prime");
#        Test.assert_equals(is_prime(45), False, "45 is not prime");
#       Test.assert_equals(is_prime(-5), False, "-5 is not prime");
#Test.assert_equals(is_prime(-8), False, "-8 is not prime");
#       Test.assert_equals(is_prime(-41), False, "-41 is not prime");

# test class
class isPrime(unittest.TestCase):
    
    # tests from kata
    # test.assert_equals(square_digits(9119), 811181)
    
    # test 0 is not a prime number
    def test_zero_not_prime(self):
        self.assertEqual(is_prime(0),False)
    # test 1 is not a prime number
    def test_one_not_prime(self):
        self.assertEqual(is_prime(1),False)
    # test 2 is a prime number
    def test_two_is_prime(self):
        self.assertEqual(is_prime(2),True)
    # error handling tests
    # test that an error is raised if a non-integer number is 
    # provided
    #def test_noninteger_raises_error(self):
    #    with self.assertRaises(TypeError):
    #        square_digits(9.5) 
    #    with self.assertRaises(TypeError):
    #        square_digits("hello")
    #    with self.assertRaises(TypeError):
    #        square_digits([6,7])
    #   with self.assertRaises(TypeError):
    #        square_digits(True) 
        #with self.assertRaises(TypeError):
        #    square_digits(2323232323231212312312424)

if __name__ == "__main__":
    unittest.main()