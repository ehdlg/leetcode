"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        number_set = set()
        for n in nums:
            if n in number_set:
                return True
            
            number_set.add(n)
        
        return False


s = Solution.containsDuplicate(self=None, nums=[1,2,3,45, 45,6])

print(s)
        