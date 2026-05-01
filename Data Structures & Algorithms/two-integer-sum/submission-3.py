class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i in range(len(nums)):
            if store.get(target - nums[i]) != None:
                return [store[target-nums[i]],i]
            store[nums[i]] = i

        