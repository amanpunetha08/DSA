class Solution:
    def  create_mp(self,s):
        mp = [0] * 26
        for c in s:
            mp[ord(c) - ord('a')]+=1
        return mp

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()

        for s in strs:
            s_collection = tuple(self.create_mp(s))
            if store.get(s_collection) !=None:
                store[s_collection].append(s)
            else:
                store[s_collection] = [s]
        return list(store.values())