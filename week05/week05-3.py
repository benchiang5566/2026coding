## week05-3.py 厩策璸礶 材2肈 Hash Map / Set
## LeetCode 1207. Unique Number of Occurrences
## –贺计, 瞷Ω计, ゲ斗常ぃ妓翅~!
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr) # 参璸计瞷Ω计
        s = set() ## ノㄓ瞷Ω计琌縒礚
        ## 代刚
        for c in counter: ## 盢计硋ㄓ
        ##    print(c, counter[c]) # 计瞷Ω计(痷Τ参璸)
        ## 拜 counter[c] 琌计常琌縒礚
            if counter[c] in s: ## 狦Τ瞷筁, 碞ア毖
                return False
            s.add( counter[c] ) ## 瞷硂瞷Ω计,  s 柑
        return True
