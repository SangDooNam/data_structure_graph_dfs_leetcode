class Solution:
    def canVisitAllRooms(self, rooms):
        
        visited = set([0])
        
        def dfs(room):
            
            for key in rooms[room]:
                
                if not key in visited:
                    visited.add(key)
                    dfs(key)
        
        dfs(0)
        
        return len(visited) == len(rooms)

rooms = [[1],[2],[3],[]] 
rooms = [[1,3],[3,0,1],[2],[0]] 
sol = Solution()

print(sol.canVisitAllRooms(rooms))