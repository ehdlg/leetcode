"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0  
        right = len(s) - 1

        while left < right:
            while left < right and s[left].isalnum() is False:
                left += 1
            while right > left and s[right].isalnum() is False: 
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            right -= 1
            left += 1
            
        
        return True
