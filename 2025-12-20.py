# Chocolate Distribution
class Solution:
# Array slicing is O(n)
    def findMinDiff(self, arr,m):

        # code here
        if len(arr)==m:
            return max(arr)-min(arr)
        
        arr.sort()
        minDiff = 1000000000
        for i in range(len(arr)-m+1):
            diff = arr[i+m-1] - arr[i]
            if(diff<minDiff):
                minDiff=diff
        return minDiff      


# Binary on rotated
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while (left<=right):
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            if(nums[mid]<nums[right]):
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if(nums[left] <= target < nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
        return -1

# Missing and repeated in 1...n
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, a):
        n = len(a)
        eSum = (n*(n+1))//2
        eSsum = n * (n + 1) * (2*n + 1) // 6
        
        aSum = 0
        aSsum = 0
        for i in a:
            aSum+=i
            aSsum += (i*i)
        sDiff = aSum-eSum
        sSdiff = aSsum - eSsum
        
        sRm = sSdiff//sDiff
        
        rep = (sDiff+sRm) // 2
        mis = rep - sDiff
        
        return rep, mis


# kth largest - quickselect
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if not nums: return
        pivot = random.choice(nums)

        less = [x for x in nums if x>pivot]
        equal = [x for x in nums if x==pivot]
        more = [x for x in nums if x<pivot]

        L,M = len(less), len(equal)

        if k<=L:
            return self.findKthLargest(less,k)
        elif k>L+M:
            return self.findKthLargest(more,k-L-M)
        else:
            return equal[0]
