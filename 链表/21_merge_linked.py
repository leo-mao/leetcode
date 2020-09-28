# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 两个指针，谁的值小谁动
# class Solution: # 省内存的方法
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     head = l1 
    #     pre = ListNode(float('-inf')) # 如果l2全部比l1小怎么办
    #     while l1 and l2:
    #         if l1.val >= l2.val: #插在l1 前面
    #             pre.next = ListNode(l2.val, l1) # previous
    #             # l1 = l1.next # 之后插进来的还是不一定比当前的大
    #             l1 = pre
    #             l2 = l2.next
    #         elif l1.val < l2.val: # 比他小则不插
    #             pre = l1 # pre 保存l1的前一个值
    #             l1 = l1.next
    #     return head

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(None)
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = ListNode(l2.val)
                l3 = l3.next
                l2 = l2.next
            
            elif l1.val <= l2.val:
                l3.next = ListNode(l1.val)
                l3 = l3.next
                l1 = l1.next

        # 如果连上剩下节点
        if not l1:
            l3.next = l2
        elif not l2:
            l3.next = l1

        return head.next
