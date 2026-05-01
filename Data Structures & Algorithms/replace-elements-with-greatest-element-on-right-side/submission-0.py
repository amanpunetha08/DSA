class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        l = len(arr)
        right_max = [0] * len(arr)
        curr_max = arr[-1]
        right_max[-1] = -1
        for i in range(l-2,-1,-1):
            right_max[i] = curr_max
            curr_max = max(curr_max,arr[i])
        
        return right_max