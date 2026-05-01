class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = dict()
        for num in nums:
            if num in dup and dup[num] == 1:
                return True
            dup[num] = 1
        return False
        