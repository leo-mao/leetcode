# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 如果两条链有共同的部分，那么他们长度差的部分肯定是不同的，所以从那里开始找
# 长的出发，走过 长度差的部分， 然后两条链一起往后走，直到找到共同的节点
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        def ln(node: ListNode):
            n = 0
            while node:
                node = node.next
                n += 1
            return n
            
        l_a, l_b = ln(headA), ln(headB)

        if l_a > l_b:
            headA, headB = headB, headA
            l_a, l_b = l_b ,l_a

        # a < b
        for _ in range(l_b - l_a):
            headB = headB.next

        while headA and headB and (headA is not headB):
            headA = headA.next
            headB = headB.next

        return headA
