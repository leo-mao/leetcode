# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        cur1 = head
        pre = ListNode(None)
        pre.next = head
        l = 0
        flag = False
        while cur1:
            print(cur1.val)
            tmp = cur1.next
            cur1.next = pre
            pre = cur1
            cur1 = tmp
            l += 1
            if (cur1 == head):
               flag = True
               break
        return flag

cur = None
for x in range(4,0,-1):
  cur = ListNode(x, cur)
cur.next.next.next.next = cur.next
# cur = ListNode(1)
s = Solution()
print(s.hasCycle(cur))
# while cur:
#   print(cur.val)
#   cur = cur.next