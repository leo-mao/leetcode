class ListNode():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = greater = None 
        cur = head
        l_cur, g_cur = ListNode(0), ListNode(0) # header

        while cur: 
            if cur.val < x:
                if not less:
                    less = ListNode(None)
                    less.next = cur
                l_cur.next = cur
                l_cur = l_cur.next

            else:
                if not greater:
                    greater = ListNode(None)
                    greater.next = cur

                g_cur.next = cur
                g_cur = g_cur.next

                
            cur = cur.next



        l_cur.next = g_cur.next = None # delete last node of l_cur and g_cur

        if not less:
            less = ListNode(None)
        if not greater:
            greater = ListNode(None)
        
        # find last of less and link 
        l_cur = less
        while l_cur and l_cur.next:
            l_cur = l_cur.next

        l_cur.next = greater.next
        return less.next


cur = None
# for x in range(4, 0, -1):
#     cur = ListNode(x, cur)
cur = sen = ListNode(None)
for x in [1,4,3,2,5,2]:
    cur.next = ListNode(x)
    cur = cur.next
s = Solution()
r = s.partition(sen.next, 3)

while r:
    print(r.val)
    r = r.next

