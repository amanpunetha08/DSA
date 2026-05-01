class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in hashset:
                streak = 0
                curr = num
                while curr in hashset:
                    streak+=1
                    curr+=1
                res = max(streak,res)
        return res
        