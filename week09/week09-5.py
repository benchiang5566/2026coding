# week09-5.py 學習計畫 Linked List 第1題 Medium 有點難 把中間的 node 刪掉
# LeetCode 2095. Delete the Middle Node of a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head # fast 兔子 slow 烏龜 一開始都在起跑點
        if head.next==None : return None # 當前面只有一格兔子跳不出去
        while fast != None and fast.next != None:
            fast = fast.next.next # 兔子跳2格
            prev = slow # 烏龜在走過的前一格被標註起來
            slow = slow.next # 烏龜走1格
        # print( slow.val ) # 當兔子走到終點時, 烏龜在中間(沒錯)
        prev.next = slow.next
        return head
