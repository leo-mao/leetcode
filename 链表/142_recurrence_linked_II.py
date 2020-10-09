class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# 2 * (x + y) = x + y + z + y =>  x = z特例, 或者是 x = n圈 + z


class Solution():
    def detectCycle(self, head: ListNode) -> ListNode:
        cur = None # 可能会返回None
        slow = fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break

        # 确保有环存在
        if fast is slow and fast and fast.next and fast.next.next:
            cur = head
            while cur != slow:
                cur = cur.next
                slow = slow.next
        return cur


cur = None
# for x in range(4, 0, -1):
#     cur = ListNode(x, cur)
# cur.next.next.next.next = cur
cur = ListNode(None)
pre = ListNode(None)
print(cur is pre)
print(cur == pre)
print(id(cur), id(pre))
# cur.next = cur
# cur.next = ListNode(2)
# s = Solution()
# r = s.detectCycle(cur)
# print(r)
# print(s.detectCycle(cur).val)
