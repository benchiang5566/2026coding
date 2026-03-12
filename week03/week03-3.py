# week03-3.py  學習計畫 Sliding Window 第2題
# LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
# 母音 Vowels: a, e, i, o, u 長度 k 的小字串, 最多幾個母音
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou') # 把 5 個字母, 變成 set()
        # 以後用 if c in vowel: 就可以快速確認他是母音
        # 以前 if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        count = 0 # 紀錄目前有幾個字母
        for i in range(k): # 找前面 k 個字母, 逐一檢查, 看是不是母音
            if s[i] in vowels: count += 1 # 找到 1 個母音, 開心!!!
        ans = count # 離開迴圈時, 確認前 k 個字母, 有 count 個母音, 先當答案
        N = len(s) # 全部字串的長度 N
        for i in range(k, N): # 右邊的每一個字母, 逐一檢查
            if s[i] in vowels: count += 1 # 右邊的頭 s[i] 又吃到 1 個字母
            if s[i-k] in vowels : count -= 1 # 左邊的尾吐掉 s[i-1], 失去一個母音
            ans = max(ans, count) # 持續更新, 找到最大值
        return ans # 回傳值
