from collections import Counter
class Solution:
    def create_map(self,s:str)->list[int]:
        mapper = [0]*26

        for c in s:
            mapper[ord(c) - ord('a')] += 1
        return mapper

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = dict()

        for s in strs:
            s_collection = tuple(self.create_map(s))
            if store.get(s_collection) != None:
                store[s_collection].append(s)
            else:
                store[s_collection] = [s]
        return list(store.values())