class Solution:
    def dfs(self,node,v,visited,isConnected):
        visited[node] = 1
        for i in range(v):
            if isConnected[node][i] == 1 and visited[i] == 0:
                self.dfs(i,v,visited,isConnected)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        count = 0
        for i in range(n):
            if visited[i] == 0:
                count += 1
                self.dfs(i,n,visited,isConnected)
        return count