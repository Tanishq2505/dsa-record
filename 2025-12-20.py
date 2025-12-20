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
