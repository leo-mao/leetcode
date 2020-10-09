class ListNode:
    def __init__(self, val: int, next=None):
        self.val = val
        self.next = next

"""
链表所有的关键都是主要是找出并保存用于指向元素的指针
这道题用了四个指针
head_k: 当前k元组中开始(初始顺序)的那个
last_head_k: 前一个head_k 的值
pre
cur
"""
class Solution:
    def reverse_every_k(self, head: ListNode, k: int) -> ListNode:
        cur = head
        l = 0
        while cur:
            l += 1
            cur = cur.next

        cur = head
        i = 1  # cur len
        # head_k, head of k segment; next, original next in k
        pre = last_head_k = head_k = next = None
        tail_k = None
        while cur:
            if i == (l % k):  # 刚开始剩余的那段的最后一个
                last_head_k = cur.next
                pre = cur
                tail_k = cur  # 保存 刚开始剩余的那段的最后一个

            if i > (l % k):  # begin 开始

                if (l - i) % k == 0:  # end k
                    next = cur.next

                    if (i // k > 1):  # update last head_k

                        last_head_k.next = cur
                        last_head_k = head_k
                        head_k = next
                    else:
                        tail_k.next = cur
                        head_k = next

                    cur.next = pre
                    pre = cur
                    cur = next

                else:
                    next = cur.next
                    cur.next = None if ((l - i + 1) %
                                        k == 0) else pre  # begin k
                    pre = cur
                    cur = next
            else:
                cur = cur.next

            i += 1
        return head


def main():
    cur = sen = ListNode(None)
    for i in range(11):
        cur.next = ListNode(i+1)
        cur = cur.next
    s = Solution()
    s.reverse_every_k(sen.next, 4)
    cur = sen.next
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == '__main__':
    main()


# 另一种方法也可以先逆整个链表，然后用递归，再逆回来 t: O(n*k^(n/k)) s: O(n)