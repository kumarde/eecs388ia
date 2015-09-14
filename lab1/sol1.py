''' 
    1. Write an implementation of FizzBuzz iteratively. 

    FizzBuzz takes in an integer n, and for every number from 1 - n,
    prints "Fizz" if the number is divisible by 3, "Buzz" if it is divisible
    by 5, and "FizzBuzz" if the number is divisible by 15. If none of those 
    is true, print the number.
'''

def FizzBuzz(n):
    for x in range(1, n):
        final = ''
        if x % 3 == 0:
            final += 'Fizz'
        if x % 5 == 0:
            final += 'Buzz'
        print final or x

''' 
    2. Write both an iterative and list comprehension solution to the following:
    
    Given a list of integers (myList), print the number * 10 if the number is NOT 
    a multiple of ten.
'''

myList = [10, 11, 15, 17, 20, 21, 24, 25, 28, 29, 30, 31, 35, 36, 40, 45, 50]

def IterativeFunc():
    returnList = []
    for x in myList:
        if x % 10 != 0:
            returnList.append(x * 10)
    print returnList

def ListComprehensionFunc():
    print [x * 10 for x in myList if x % 10 != 0]


'''
    3. Write a function that prints every three letter permutation of the alphabet
    using a data structure comprehension. Don't worry about being inefficient from a memory perspective,
    be focused on doing it pythonically.
'''
def AlphabetPermutation():
    alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
    print [a + b + c for a in alphabet1 for b in alphabet1 for c in alphabet1]

#FizzBuzz(100)
#IterativeFunc()
#ListComprehensionFunc()
AlphabetPermutation()
