'''
    1. Write an implementation of stringToNum 
    
    Takes in input string, returns list of 0-indexed values of characters in string
    in lowercase

    "abcde" -> [0, 1, 2, 3, 4]
'''

def stringToNum(string_in):
    string_in = string_in.lower()
    print [ord(char) - ord('a') for char in string_in]

'''
    2. Write an implementation of numToString

    Takes in a list of numbers (0 indexed alphabet characters from 0 - 25)
    returns a string
'''

def numToString(nums):
    print ''.join([chr(num + ord('a')) for num in nums])
