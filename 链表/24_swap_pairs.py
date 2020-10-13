# 交换过后相对位置改变了，所以用index时要注意；其实也可以不用
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        i = 1
        sen = pre = ListNode(None, head)
        cur = head
        while cur:
            # if i % 2 == 1:
            if cur.next:
                pre_next = pre.next
                cur_next = cur.next
                cur_next_next = cur.next.next
                
                # 下面顺序不能变,不然拿不到cur.next.next
                pre.next = cur_next
                cur.next.next = pre_next
                cur.next = cur_next_next
                #  进入下一次交换
                pre = cur
                cur = cur.next
            else:
                break

        return sen.next