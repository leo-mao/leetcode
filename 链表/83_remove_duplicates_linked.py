class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        sen = pre = ListNode(None, head)
        while h:
            if pre.val == h.val: 
                pre.next = h.next
            else:# pre指针应该始终呆在原来的地方，不该提前往后走,否则pre就是被删节点了，那么pre.next就无意义了
                pre = h
            h = h.next
        return sen.next
