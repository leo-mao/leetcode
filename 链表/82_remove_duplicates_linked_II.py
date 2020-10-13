"""
本题的关键在与找到一个 与前值不同的数值不能直接拿来，而是要再次与next对比，用while可实现
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        sen = pre = ListNode(None) # pre is the start of duplication
        cur = head
            # print(cur.val)
        def check_dup(head: ListNode):# 当前这个是否有重复，返回当前这个是否重复，如果是，返回重复的最后一个节点；否则就当前节点
            flag = False
            next = head.next # helper to check duplication
            while head.next and head.val == head.next.val:  # if not duplicate， 但是cur.next是空时，是无法判断的
                flag = True
                head = head.next
            return flag, head 
            
        while cur: # find next not duplicated node
            flag, cur = check_dup(cur)
            if not flag:
                pre.next = cur
                pre = pre.next
                cur = cur.next
            else:
                cur = cur.next
        pre.next = cur # 最后结束肯定是cur = None, 但是最后的cur可能重复，要把pre.next置空

        return sen.next