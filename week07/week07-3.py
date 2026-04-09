# week07-3.py 學習計畫 Stack 第3題
# LeetCode 2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in s:
            if i == "*": ans.pop()
            else: ans.append(i)
        return ''.join(ans) # 只有陣列才可以 stack

