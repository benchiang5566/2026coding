# week07-6.py 學習計畫 第2題
# LeetCode 649. Dota2 Senate
# Dota2 兩個陣營「Radiant」「Dire」照 senate 字串的順序出現
# 巡完一輪, 繞道前面繼續, 直到全部字母相同, 問最後「哪個陣營得勝」
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0 # 目前被對方消滅的次數
        R, D = senate.count('R'), senate.count('D') # 數一數字串內有幾個有幾個單位
        while queue: # 進行「互相 Ban 對方」的遊戲
            now = queue.popleft() # 左邊吐出個字母, 他要消滅「敵對陣營」
            if now=='R':
                if banR>0: # 已經紀錄要消滅1個人
                    banR -= 1 # 用掉1個消滅的名額
                    R -= 1 # 馬上少掉一個人
                    continue
                else: # 你沒有被消滅的單位, 反過來消滅對方
                    banD += 1
                    queue.append(now) # 再到最右邊排隊
            else:
                if banD>0:
                    banD -= 1
                    D -= 1
                    continue
                else:
                    banR += 1
                    queue.append(now)
            if R==0: return 'Dire' # 把 R 消滅光, 'D'就得勝
            if D==0: return 'Radiant' # 把 D 消滅光, 'R'就得勝
