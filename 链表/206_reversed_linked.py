class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None  # previous
        cur = head
        while cur:
            tmp = cur.next  # next

            cur.next = pre
            pre = cur

            cur = tmp
        return pre
