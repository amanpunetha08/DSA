from collections import defaultdict
class DSU:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,x,y):
        px,py = self.find(x),self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px,py = py,px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] +=1
        return True
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_id = {}
        email_to_name = {}
        id = 0
        
        for account in accounts:
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id
                    id+=1
                if email not in email_to_name:
                    email_to_name[email_to_id[email]] = account[0]
        dsu = DSU(id)

        for account in accounts:
            emails = account[1:]
            for i in range(1,len(emails)):
                dsu.union(email_to_id[emails[i-1]],email_to_id[emails[i]])
        
        groups = defaultdict(list)
        for email,idx in email_to_id.items():
            root = dsu.find(idx)
            groups[root].append(email)
        
        results = []
        for root,emails in groups.items():
            results.append([email_to_name[root]] + sorted(emails))
        return results
        

        
        

        
        

        