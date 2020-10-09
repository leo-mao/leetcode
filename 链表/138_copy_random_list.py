# class Solution:
    # def copyRandomList(self, head: 'Node') -> 'Node':
    #     # DFS
    #     ori_dup = {} # original_duplicate, Map 存储节点
    #     def clone(cur: 'Node')-> 'Node':
    #         if not cur:
    #             return None # None 比 Node(None)更合适！！！
    #         elif ori_dup[cur.val]:
    #             return ori_dup[cur.val]
    #         else:
    #             ori_dup[cur.val] = Node(cur.val) # 必须先放进去，避免无限死循环，生成无数节点
    #             ori_dup[cur.val].next, ori_dup[cur.val].random = clone(cur.next), clone(cur.random)
    #             return ori_dup[cur.val]

    #     # cur = head
    #     # sen_h = sen = Node(None)
    #     # while cur:
    #     #     sen_h.next = Node(cur.val, None, cur.random)
    #     #     sen_h = sen_h.next
    #     #     cur = cur.next
    #     return ori_dup[head.val]

class Solution:
    def copyRandomList(self, head: ListNode) -> ListNode:
        # BFS

        ori_dup = {None:None} # None must be there
        if head:
            s = [head]
        else:
            s = []
        i = 0
        # generate all the duplicate node
        while i < len(s):
            cur = s[i]
            if cur not in ori_dup:
                ori_dup[cur] = ListNode(cur.val)
                ori_dup[cur].next = None
                ori_dup[cur].random = None

            if cur.next not in ori_dup:
                ori_dup[cur.next] = ListNode(cur.next.val)
                ori_dup[cur].next = None
                s.append(cur.next)
            else:
                ori_dup[cur].next = ori_dup[cur.next]

            if cur.random not in ori_dup:
                ori_dup[cur.random] = ListNode(cur.random.val)
                ori_dup[cur].random = None
                s.append(cur.random)
            else: 
                ori_dup[cur].random = ori_dup[cur.random]
                
            i += 1
            
        # link all the node
        cur = head
        while cur:
            ori_dup[cur].next = ori_dup[cur.next]
            ori_dup[cur].random = ori_dup[cur.random]
            cur = cur.next
        return ori_dup[head]

def main():
    cur = sen = ListNode(None)
    # for i in range(8):
    #     cur.next = ListNode(i+1)
    #     cur = cur.next
    s = {}
    for i in [7, 13, 11, 10,1]:
        cur.next = ListNode(i)
        cur = cur.next
        s[i] = cur
    s[7].random = None
    s[13].random = s[7]
    s[11].random = s[1]
    s[10].random = s[11]
    s[1].random = s[7] 

    s = Solution()
    r = s.copyRandomList(sen.next)
    cur = sen.next
    while r:
        print(r.val)
        if r.random:
            assert r.random is not cur.random
            assert r.random.val is cur.random.val
        r = r.next
        cur = cur.next
if __name__ == '__main__':
    main()