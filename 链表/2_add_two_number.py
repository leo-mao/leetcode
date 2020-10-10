class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sen = cur = ListNode(None)
        val1 = 0
        val2 = 0
        r = 0
        carry = 0
        while l1 or l2 or (carry > 0):
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            r = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            cur.next = ListNode(r)
            cur = cur.next
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        return sen.next