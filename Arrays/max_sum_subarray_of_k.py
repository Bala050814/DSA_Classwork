class Solution:
    def maxSubarraySum(self, arr, k):
        n=len(arr)
        maxsum=sum(arr[:k])
        cursum=sum(arr[:k])
        
        for i in range(1,n-k+1):
            cursum+=arr[i+k-1]-arr[i-1]
            maxsum=max(cursum,maxsum)
            
        return maxsum
