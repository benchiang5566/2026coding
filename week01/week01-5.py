## week01-5.py 學習計畫 Array/String 第7題
## LeetCode 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        preSum = [1] ## 左邊累積乘起來的值
        postSum= [1]
        for i in range(N):
            preSum.append( preSum[-1] * nums[i] ) ## 每次多乘一個數字
            postSum.append( postSum[-1] * nums[N-1-i] ) ## 每次多乘右邊數字
        ans = [] ## 最後的答案
        for i in range(N):
            ans.append( preSum[i] * postSum[N-1-i] ) ## 左邊累積 * 右邊累積
        return ans ## 回傳資料
