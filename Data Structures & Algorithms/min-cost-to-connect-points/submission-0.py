class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0
        ans = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or dist[i] < dist[u]):
                    u = i

            visited[u] = True
            ans += dist[u]

            x1, y1 = points[u]

            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    cost = abs(x1 - x2) + abs(y1 - y2)
                    dist[v] = min(dist[v], cost)

        return ans