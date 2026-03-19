# week04-5.py 學習計畫 Prefix sum 第2題
# LeetCode 724. Find Pivot Index
# 找到一個數, 使得左右兩邊一樣重, 取得平衡
# 左邊「往右」加起來的同時, 右邊也同時「往左」邊加起來
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        N = len(nums)
        prefix = [0]
        for i in range(N):
            prefix.append( prefix[-1] + nums[i] )
        print(prefix)
        postfix = [0] * (N+1)
        for i in range(N-1, -1, -1):
            postfix[i] = postfix[i+1] + nums[i]
        print(postfix)
        for i in range(N):
            if prefix[i] == postfix[i+1]: return i
        return -1

