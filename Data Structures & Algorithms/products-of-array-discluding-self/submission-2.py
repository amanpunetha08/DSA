class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suff = [0] * len(nums)
        pref = [0] * len(nums)
        res = [0] * len(nums)

        suff[0] = 1
        for i in range(1,len(nums)):
            suff[i] = suff[i-1] * nums[i-1]
        pref[-1] = 1
        for i in range(len(nums)-2,-1,-1):
            pref[i] = pref[i+1] * nums[i+1]
        print(suff,pref)
        for i in range(len(nums)):
            res[i] = suff[i] * pref[i]
        return res        