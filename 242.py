"""
Given two strings s and t, return true if t is an anagram
of s, and false otherwise.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        s_dict = dict()
        t_dict = dict()

        def updateDict(dictionary, str):
            for c in str:
                val = dictionary.get(c, 0)

                dictionary.update({c: val + 1})


        updateDict(dictionary=s_dict, str=s)
        updateDict(dictionary=t_dict, str=t)

        for key in s_dict:
            if key not in t_dict or s_dict.get(key) != t_dict.get(key):
                return False

        
        return True
    
s = Solution.isAnagram(self=None, s='stra', t='atsr')

print(s)

        
        

