# week08-5.py 學習計畫 Binary Search 第3題
# LeetCode 162. Find Peak Element
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N==1: return 0 # 如果只有一筆資料何來左右邊界
        for i in range(N):
            if i==0: # 沒有左邊, 只測右邊 (要比右邊大)
                if nums[i] > nums[i+1]: return i
            elif i==N-1: # 最右邊, 沒有右邊, 只測左邊 (要比左邊大)
                if nums[i-1] < nums[i]: return i
            # 下面會當機, 因為 i-1 或 i+1 可能會超過範圍
            elif nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
