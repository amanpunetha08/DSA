class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        store = dict()

        for num in nums:
            if num not in store:
                store[num] = 0 
            store[num]+=1
        
        store = dict(sorted(store.items(),key=lambda x:x[1],reverse=True))
        ans = []
        for key,values in store.items():
            ans.append(key)
        return ans[0:k]
                
        