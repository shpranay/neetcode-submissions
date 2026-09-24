class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}

        for frm, to in tickets:
            if frm not in graph:
                graph[frm] = []
            graph[frm].append(to)

        for airport in graph:
            graph[airport].sort(reverse=True)

        route = []

        def dfs(airport):
            while airport in graph and graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)

            route.append(airport)

        dfs("JFK")

        return route[::-1]