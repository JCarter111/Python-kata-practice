import unittest
def all_primes(num):

    # return a list of prime numbers in the
    # range up to and including num
    # using the Sieve of Erasothenes algorithm
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    # raise an error if an integer is not provided
    if not(isinstance(num,int)) or isinstance(num,bool):
        raise TypeError("Please provide an integer number")
    
    # Using the Sieve of Erasthemes

    # create a list of possible prime numbers for checking
    # the list needs to be in the range 2 to num
    numList = list(range(2,num+1))
    primeNumbers = []
    # start with p = 2
    p=2
    # only need to check numbers up to sqrt(num)
    while p**2 < num:

        # x in e.g. range(4, 18, step of 2)
        for x in range(2*p,num+1,p):
            numList[x-2] = 0
        
        # print new number list
        print("after p = " + str(p) + " " + str(numList))
    
        # find next value of p to check
        # find next non zero number in the list 
        for y in range(0,len(numList)-1):
            if numList[y] !=0 and  y > p-2:
                newpValue = numList[y]
                break
        print(newpValue)
        p = newpValue  

    # format list of prime numbers
    # remove zeros from numList
    for x in numList:
        if x !=0:
            primeNumbers.append(x)
    print(primeNumbers)
    # return list of prime numbers    
    return(primeNumbers)

# test class
class allPrimes(unittest.TestCase):
    
    # tests from kata
    # test.assert_equals(square_digits(9119), 811181)
    
    # test square is returned for one integer
    def test_empty_lists(self):
        self.assertEqual(all_primes(0),[])
        self.assertEqual(all_primes(1),[])
        
    def test_negative_numbers_not_prime(self):
        self.assertEqual(all_primes(-1),[])
        self.assertEqual(all_primes(-41),[])

    def test_all_primes_returned(self):
        # num is a prime number
        self.assertEqual(all_primes(17),[2,3,5,7,11,13,17])
        # num is not a prime number
        self.assertEqual(all_primes(75),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73])

    def test_large_number(self):
        self.assertEqual(all_primes(500),
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 
        97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 
        193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 
        307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 
        421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499])
    
 
    # test what happens if num is larger than the maximum integer values
    #def test_large_number_returns_squares(self):
    #    self.assertEqual(square_digits(21574864912),412549166436168114)
    # error handling tests
    # test that an error is raised if a non-integer number is 
    # provided
    def test_noninteger_raises_error(self):
        with self.assertRaises(TypeError):
            all_primes(9.5) 
        with self.assertRaises(TypeError):
            all_primes("hello")
        with self.assertRaises(TypeError):
            all_primes([6,7])
        with self.assertRaises(TypeError):
            all_primes(True) 
     
   # tests from kata

    # basic tests
    # test 0 is not a prime number
#    def basic_tests(self):
 #       self.assertEqual(all_primes(0),[])
#        self.assertEqual(all_primes(1),[])
 #       self.assertEqual(all_primes(2),[2])
#        self.assertEqual(all_primes(17),[2,3,0,5,0,7,0,0,0,11,0,13,0,0,0,17])
#        self.assertEqual(is_prime(75),False)
#        self.assertEqual(is_prime(-1),False)

    # test prime
 #   def test_prime(self):
 #       self.assertEqual(is_prime(3), True)
 #       self.assertEqual(is_prime(5), True)
 #       self.assertEqual(is_prime(7),True)
#        self.assertEqual(is_prime(41),True)
#        self.assertEqual(is_prime(5099),True)

    # test not prime
 #   def test_not_prime(self):
 #       self.assertEqual(is_prime(4),False)
#        self.assertEqual(is_prime(6),False)
#        self.assertEqual(is_prime(8),False)
 #       self.assertEqual(is_prime(9),False)
 #       self.assertEqual(is_prime(45),False)
 #       self.assertEqual(is_prime(-5),False)
 #       self.assertEqual(is_prime(-8),False)
 #       self.assertEqual(is_prime(-41),False)

    # error handling tests
    # test that an error is raised if a non-integer number is 
    # provided
 #   def test_noninteger_raises_error(self):
#        with self.assertRaises(TypeError):
 #           all_primes(9.5) 
#        with self.assertRaises(TypeError):
#            all_primes("hello")
if __name__ == "__main__":
    unittest.main()

 
