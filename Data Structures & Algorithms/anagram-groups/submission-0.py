from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()

        for s in strs:
            s_collection = tuple(sorted(s))
            if store.get(s_collection) != None:
                store[s_collection].append(s)
            else:
                store[s_collection] = [s]
        return list(store.values())