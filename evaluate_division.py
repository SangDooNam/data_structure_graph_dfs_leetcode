from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        
        def add_edge(start, end, value):
            if start in graph:
                graph[start].append((end, value))
            else:
                graph[start] = [(end, value)]
        
        for (dividend, divisor), value in zip(equations, values):
            add_edge(dividend, divisor, value)
            add_edge(divisor, dividend, 1 / value)
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            elif start == end:
                return 1.0
            visited.add(start)
            
            for neighbour, value in graph[start]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                temp_result = dfs(neighbour, end, visited)
                if temp_result != -1.0:
                    return temp_result * value
                visited.remove(neighbour)
            
            return -1.0
        
        results = []
        for equation in queries:
            results.append(dfs(equation[0], equation[1], set()))
        
        return results


sol = Solution()

# Test the function with the provided examples
equations1 = [["a","b"],["b","c"]]
values1 = [2.0,3.0]
queries1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

equations2 = [["a","b"],["b","c"],["bc","cd"]]
values2 = [1.5,2.5,5.0]
queries2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

equations3 = [["a","b"]]
values3 = [0.5]
queries3 = [["a","b"],["b","a"],["a","c"],["x","y"]]

result1 = sol.calcEquation(equations1, values1, queries1)
result2 = sol.calcEquation(equations2, values2, queries2)
result3 = sol.calcEquation(equations3, values3, queries3)

print(result1)







































class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
    
    # Build the graph from equations
        def addEdge(start, end, value):
            if start in graph:
                graph[start].append((end, value))
            else:
                graph[start] = [(end, value)]
        
        for (dividend, divisor), value in zip(equations, values):
            addEdge(dividend, divisor, value)
            addEdge(divisor, dividend, 1 / value)
    
    # DFS function to find the result of the query
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            
            for neighbour, value in graph[start]:
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                tempResult = dfs(neighbour, end, visited)
                if tempResult != -1.0:
                    return tempResult * value
                visited.remove(neighbour)
            return -1.0
        
        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))
        
        return results
