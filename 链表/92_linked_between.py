class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        sen = pre = ListNode(None, head)
        cur = head
        i = 1
        m_pre = n_next = None
        while cur:
            if i == m:
                m_pre = pre
            elif i == n: # else排除掉 m=n 的情况
                n_next = cur.next

                m_pre.next.next = n_next # 指向原尾部的next指针 复制给 被反转部分原来第一个的next
                # print(m_pre.next.next.val)
                m_pre.next = cur # 原来指向被反转部分头部的，指向原尾部
                # print(m_pre.next.val)
         
                cur.next, cur = pre, n_next
                # print(m_pre.next.next.val)
                # print(m_pre.next.next.next.val) # print 大法好，所有问题都能解决
                return sen.next

            if i > m and i < n:
                cur_next = cur.next
                pre, cur.next = cur, pre
                cur = cur_next
            else:
                pre, cur = cur, cur.next # geneal situation
            i += 1
        return sen.next
