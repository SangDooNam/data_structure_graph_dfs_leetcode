
class Solution:
    def minReorder(self, n: int, connections) -> int:
        
        dct = {i:[] for i in range(n)}
        
        for a, b in connections:
            dct[a].append((b, True))
            dct[b].append((a, False))
        
        def dfs(city, visited):
            visited.add(city)
            reversals = 0
            for neighbor, needsReversal in dct[city]:
                if neighbor not in visited:
                    reversals += needsReversal
                    reversals += dfs(neighbor, visited)
            return reversals

        return dfs(0, set())





n = 6
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]

# n = 5
# connections = [[1,0],[1,2],[3,2],[3,4]]

sol = Solution()

print(sol.minReorder(n, connections))
