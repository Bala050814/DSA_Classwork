class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        cursum = 0
        minlen = float('inf')

        for r in range(len(nums)):
            cursum += nums[r]

            while cursum >= target:
                minlen = min(minlen, r - l + 1)

                cursum -= nums[l]
                l += 1

        if minlen == float('inf'):
            return 0

        return minlen
