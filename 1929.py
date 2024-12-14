"""
Given an integer array nums of length n, you want to create an array ans of length 2n where
ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

from typing import List


def getConcatenation(nums: List[int]) -> List[int]:
    size = len(nums) * 2
    ans = list()

    for i in range(size):
        j = i % len(nums)
        ans.append(nums[j])
        
    return ans

getConcatenation([1,23,4,5,456,345,6345,36])
    