# Best time to buy and sell stocks
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxP = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
                r+=1
            else:
                maxP = max(maxP,prices[r]-prices[l])
                r+=1
        return maxP

# Contains duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        return True if len(n)!=len(nums) else False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictN = {}
        for i in nums:
            if i in dictN:
                return True
            dictN[i] = 1
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False

