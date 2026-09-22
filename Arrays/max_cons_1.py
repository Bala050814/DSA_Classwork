class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        from itertools import groupby
        return max((len(list(g)) for k, g in groupby(nums) if k == 1), default=0)
