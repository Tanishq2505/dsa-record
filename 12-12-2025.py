# Min max of array - easy
class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        for i in arr:
            if i<min:
                min = i
            elif i>max:
                max = i
        return min,max

  # Reverse array in place - easy
  class Solution:
    def reverseArray(self, arr):
        # code here
        i = 0
        j = len(arr)-1
        while (i<j):
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return arr
        
        


# Max subarray - easy
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxEnding = nums[0]
        for i in nums[1:]:
            maxEnding = max(i, maxEnding+i)
            res = max(res, maxEnding)
        return res


# Next perm - Med
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify numss in-place instead.
        """
        # Find decreasing array
        i = len(nums)-1
        while (i>0 and nums[i-1]>=nums[i]):
            i-=1
        j=i    
        i-=1
        if(i>=0):
            # Just larger than numss[i]
            minInd = j
            while (j<len(nums)-1 and nums[j+1]>nums[i]):
                j+=1
            
            # swap i and j
            nums[i],nums[j]=nums[j],nums[i]
        # reverse array
        nums[i+1:] = nums[i+1:][::-1]

        
