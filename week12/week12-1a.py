# week12-1a.py 學習計畫 Graphs - DFS 第1題 Medium 題
# 房間裡有鑰匙, 可以再開心的房間, 最後能開全部房間嗎?
# DFS: Depth Firsst Search 通常會利用 stack 或 function stack(函式呼叫函式)
# LeetCode 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0] # 利用 stack 裡面有待處理的房間, 一開始房間 0 是開的
        visited = set() # 有去過、處理過的房間, 不要在進去了
        visited.add(0) # 已經排好、等待處理, 下次有拿到鑰匙, 不要再放進去 stack 囉~
        while stack: # 只要 stack 裡面還有東西, 就繼續處理
            now = stack.pop() # 吐出 1 個房間, 現在要來處理
            for k in rooms[now]: # 把 room now 房間裡, 所有鑰匙 k, 都別拿來檢查
                if k in visited: continue # 鑰匙 k 對應的房間 k 看過了, 別再檢查
                # 如果走到這裡, 代表沒走過、沒有待處理的房間 k
                stack.append(k) #加入 stack 資料結構
                visited.add(k) # 標記這個房間也待處裡、其他人不要再排處理
        return len(rooms) == len(visited) # 房間數目, 全部參觀過了, 成功
