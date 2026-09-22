class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        q = collections.deque([0])
        visited = [0]*len(rooms)
        while q:
            x = q.popleft()
            if visited[x] == 1:
                continue
            visited[x] = 1
            for i in rooms[x]:
                if visited[i] == 0:
                    q.append(i)
        for i in visited:
            if i == 0:
                return False
        return True