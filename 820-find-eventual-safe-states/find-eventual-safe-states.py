class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited = [0] * (n)

        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] =1
            for edge in graph[node]:
                if not dfs(edge):
                    return False
            visited[node] = 2
            return True
        results = []
        for i in range(n):
            if dfs(i):
                results.append(i)
        return results
        