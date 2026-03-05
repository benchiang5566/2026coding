## week02-3.py 學習計畫 Twe Pointers 第2題
## LeetCode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len (t) ## 字串長度
        if N1==0: return True
        i = 0
        for k in range(N2): ## 右邊一個個去試
            if s[i] == t[k]: ## 找到 1 個「左右」符合的了
                i+=1 ## 左邊的 i 往右升一級
            if i==N1: ## 左邊的 i 有走到左邊的結束, 太好了
                return True ## 成功
        ## 沒有走到最後、沒有比對成功, 太糟了
        return False ## 失敗
