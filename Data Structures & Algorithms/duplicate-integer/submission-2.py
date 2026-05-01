class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = dict()
        for num in nums:
            if num in duplicates:
                return True
            duplicates[num] = num
        return False
        