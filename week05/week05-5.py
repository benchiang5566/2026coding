## week05-5.py 學習計畫 Hash Map / Set
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1) ## 統計用過的字母, 出現的次數
        counter2 = Counter(word2)

        ## 用過的字母, 是否是相同的集合(左邊有、右邊也有、做邊也會有)
        if set(counter1.keys()) != set(counter2.keys()): # 用的字母部不同, 就是拜
            return False
        ## 把出現的次數, 小到大排好, 如果兩邊都一樣, 那可以換到一樣為止
        if sorted(counter1.values()) != sorted(counter2.values()):
            return False
        return True

