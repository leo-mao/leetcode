# 很不情愿的用了递归，原因很简单，我认为考链表的题目就该排除栈和队列，所以官方题解我很不忍可
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def len(l: ListNode):
            i = 0
            while l:
                i += 1
                l = l.next
            return i

        def next_bit(l1: ListNode, l2: ListNode, carry: int, result: ListNode)-> (int, ListNode):
            l1_next = None if not l1.next else l1.next
            l2_next = None if not l2.next else l2.next

            if l1_next or l2_next:
                carry, result = next_bit(l1_next, l2_next, carry, result)
            
            r = (l1.val + l2.val + carry) % 10
            new_carry = (l1.val + l2.val + carry) // 10
            old = result
            result = ListNode(r)
            result.next = old
            return new_carry, result
        
        len_1 = len(l1)
        len_2 = len(l2)
        
        if len_1 < len_2:
            l1, l2 = l2, l1
            len_1, len_2 = len_2, len_1
        
        l2_new = l2
        for _ in range(len_1 - len_2):
            old = l2_new
            l2_new = ListNode(0)
            l2_new.next = old

        c, r = next_bit(l1, l2_new, 0, None)

        if c > 0: # carry bit more than 0
            r = ListNode(c, r)
        # while r:
        #     print(r.val)
        #     r = r.next
        return r