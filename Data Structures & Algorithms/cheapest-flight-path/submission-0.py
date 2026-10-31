class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices[:]              # snapshot so each round uses only the previous round's costs
            for u, v, w in flights:
                if prices[u] == INF:
                    continue
                if prices[u] + w < tmp[v]:
                    tmp[v] = prices[u] + w
            prices = tmp

        return -1 if prices[dst] == INF else prices[dst]