class Solution:
    def findCircleNum(self, isConnected):
        
        def dfs(city):
            visited.add(city)
            for neighbor, connected in enumerate(isConnected[city]):
                if connected and neighbor not in visited:
                    dfs(neighbor)
        
        province = 0
        n = len(isConnected)
        visited = set()
        
        for city in range(n):
            if city not in visited:
                dfs(city)
                province += 1
        
        return province


sol = Solution()

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]

print(sol.findCircleNum(isConnected))