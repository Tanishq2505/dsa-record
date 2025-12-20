# Chocolate Distribution
class Solution:

    def findMinDiff(self, arr,m):

        # code here
        if len(arr)==m:
            return max(arr)-min(arr)
        
        arr.sort()
        minDiff = 1000000000
        for i in range(len(arr)-m+1):
            subArray = arr[i:i+m]
            minDiff = min(minDiff, max(subArray)-min(subArray))
        return minDiff            
