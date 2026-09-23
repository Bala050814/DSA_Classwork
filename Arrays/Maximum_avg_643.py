class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)

        cur = sum(nums[:k])
        maxi = cur

        for i in range(k, n):
            cur += nums[i] - nums[i-k]
            maxi = max(maxi, cur)

        return maxi / k
