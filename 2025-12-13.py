# Contains duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return False if len(setNums)==len(nums) else True

# Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i]!=t[i]:
                return False
        return True

# Two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            rem = target - nums[i]
            try:
                ind = nums.index(rem)
            except:
                ind = -1
            if ind != -1 and ind!=i:
                return [i,ind]
