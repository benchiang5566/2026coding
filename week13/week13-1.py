# week13-1.py 學習計畫 Graphs - BFS 第1題
# LeetCode 1926. Nearest Exit from Entrance in Maze
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        M, N = len(maze), len(maze[0]) # 地圖有多大
        visited = set() # 已經走過的不要再排一次隊了
        visited.add(tuple(entrance)) # 因為 list 資料結構, 所以要轉成 tuple
        queue = deque() # 排隊、雙向佇列, 當需要使用佇列, 意味著使用 BFS 思考
        queue.append((entrance[0], entrance[1], 0)) # 右邊塞入、排隊

        while queue:
            i, j, step = queue.popleft() # 現在處理 (i,j)
            for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if ii<0 or jj<0 or ii>=M or jj>=N: continue # 如果掉出邊界, 就下一位
                if maze[ii][jj] == '+': continue # 撞牆囉~下面一位

                # if ii==0 or jj==0 or ii==M-1 or jj==N-1: return step+1 # 找到出口

                if (ii,jj) not in visited: # 如果沒有去過這一格
                    if ii==0 or jj==0 or ii==M-1 or jj==N-1: return step+1
                    visited.add( (ii, jj) ) # 標示已處理, 排隊中, 別重覆排隊
                    queue.append( (ii, jj, step+1) ) # 真的進入隊伍當中, 記錄自己找到出口總計走了幾步
        return -1 # 哭哭找不到出口
