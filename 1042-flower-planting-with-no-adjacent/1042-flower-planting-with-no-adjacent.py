class Solution:
    def gardenNoAdj(self, n, paths):

        # Create empty graph
        graph = [[] for _ in range(n)]

        # Build graph
        for a, b in paths:
            a = a - 1
            b = b - 1

            graph[a].append(b)
            graph[b].append(a)

        # 0 means no flower assigned yet
        ans = [0] * n

        # Color each garden
        for i in range(n):

            # Flowers already used by neighbors
            used = set()

            # Check all neighbors
            for j in graph[i]:
                if ans[j] != 0:
                    used.add(ans[j])

            # Try flowers 1, 2, 3, 4
            for flower in range(1, 5):
                if flower not in used:
                    ans[i] = flower
                    break

        return ans