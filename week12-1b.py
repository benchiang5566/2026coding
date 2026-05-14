# week12-1b.py 學習計畫 Graphs - DFS 第1題 Medium 題
# 房間裡有鑰匙, 可以再開心的房間, 最後能開全部房間嗎?
# DFS: Depth Firsst Search 通常會利用 stack 或 function stack(函式呼叫函式)
# LeetCode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def helper(now): # 利用「函式呼叫函式」的版本，也是 stack 的概念
            for k in rooms[now]:
                if k not in visited:
                    visited.add(k)
                    helper(k)
        visited.add(0)
        helper(0)
        return len(rooms)==len(visited)
