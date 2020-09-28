# 普通版
# class Solution:
#     def isPalindrome(self, head: ListNode) -> bool:

#         head_0 = head
#         rev = ListNode(None)
#         while head:
#             rev = ListNode(head.val, rev)
#             head = head.next
#         flag = True
#         while head_0 and rev:
#             if head_0.val != rev.val:
#                 flag = False
#             head_0, rev= head_0.next, rev.next
        
#         return flag

# 递归版, t = s = O(n) , 124 ms	74.2 MB 又费时又费空间
# 一路走到终点，
# class Solution:
#     front = None

#     def isPalindrome(self, head: ListNode) -> bool:
#         global front 
#         front = head
#         def check(head) -> bool:
#             # 返回值, 既表示是否到达结尾又表示是否回文, 没到结尾或者不是回文都是false
#             global front
#             if head:
#                 print(head.val)
#                 if check(head.next): # 开始判断回文
#                     result = front.val == head.val
#                     front = front.next
#                     return result
#                 else: # 下一层的返回过来说不是回文，传递上去
#                     return False
#             else:
#                 return True
            
#         return check(front)
# 快慢指针 t = O(n), s = (1)

class Solution:

    def isPalindrome(self, head: ListNode) -> bool:

        def reverse(head: ListNode) -> bool:
            pre, next = None, None
            while head:
                next, head.next = head.next, pre
                pre = head # 当前head要保存起来当作pre用
                head = next
            return pre

        def begin_of_last_half(head: ListNode) -> ListNode:
            h0 = h1 = head
            while h0 and h1 and h0.next and h1.next and h1.next.next: # h1.next must exist before h1.next.next
                h0 = h0.next
                h1 = h1.next.next
            

            return h0.next

        if not head:
            return True

        h0, h1 = head, begin_of_last_half(head)
        rev_h1 = reverse(h1)
        flag = True
        while h0 and rev_h1:
            if h0.val != rev_h1.val:
                flag = False
            h0, rev_h1 = h0.next, rev_h1.next

        h0.next = reverse(rev_h1)
        return flag
