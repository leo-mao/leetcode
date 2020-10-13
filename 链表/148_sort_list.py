class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        def merge(h1: ListNode, h2: ListNode) -> ListNode:
            cur = sen = ListNode(None)  # 合并的更规范的写法
            while h1 and h2:
                if h1.val >= h2.val:
                    cur.next, h2 = h2, h2.next
                    cur = cur.next
                else:
                    cur.next, h1 = h1, h1.next
                    cur = cur.next
            cur.next = h1 if h1 else h2
            return sen.next

        if not head or not head.next:
            return head
        fast, slow = head.next, head  # 快慢指针的用法, slow.next  作为下一个的起点，然后，长度奇数时，用中点归前面

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow.next, mid = None, slow.next  # cut and new head

        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)
