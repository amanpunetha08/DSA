import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        pq = [(0,k)]
        adj = [[]for _ in range(n + 1)]
        for u,v,w in times:
            adj[u].append((v,w))

        while pq:
            d,u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v,w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq,(dist[v],v))
        
        result = max(dist[1:])
        return result if result != float('inf') else -1

        