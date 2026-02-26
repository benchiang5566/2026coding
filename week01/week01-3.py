## week01-3.py
## LeetCode 1071. Greatest Common Divisor of Strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
     ## 程そ计 gcd Τ闽
     N1, N2 = len(str1), len(str2) ## ㄢ﹃
     N = gcd(N1, N2) ## 程そ计
     ans = str1[:N] ## ﹃ 1 玡 N 计

     if ans*(N1//N) != str1: return "" ##ぃ才, 碞ア毖
     if ans*(N2//N) != str2: return ""
     return ans
