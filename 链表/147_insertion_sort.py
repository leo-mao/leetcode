class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        sen = None  # senitel for result
        cur = head
        while cur:
            # print(cur.val)

            if not sen:
                sen = ListNode(None)
                # sen.next = cur # 不能直接把原节点放进result的中，会造成环或者跳过节点，混淆了原节点和当前节点

            # 找到首个大于cur值的节点
            pre = sen
            find = sen.next
            while find and find.val <= cur.val:
                # print(find.val)
                pre = find
                find = find.next

            pre.next = cur

            cur_next = cur.next
            cur.next = find

            cur = cur_next
        if sen:
            return sen.next
        else:
            return None