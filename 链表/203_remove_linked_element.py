class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        sen = pre = ListNode(None, head) # sentinel node
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = cur
            cur = cur.next

        return sen.next
