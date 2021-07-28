class Solution:
    # 并查集的含义就是，如果图中已经存在的点，相互已经能够联通了，这时候，新的输入又给了图中两点多了一条新路径
    # 此时，必然图中形成了环
    # 术语，某节点的代表节点，即该节点的父节点，没有父节点是为自己；
    # 集合的代表节点，集合的根节点
    # 集合树，即集合构成的多叉树
    # 参见解析 https://leetcode-cn.com/problems/redundant-connection/solution/tong-su-jiang-jie-bing-cha-ji-bang-zhu-xiao-bai-ku/

    # !! parent[e[0]] == e[0]不代表这是e[0]首次出现，也有可能是成为了别人的代表节点
    # parent[1] 表示节点1 的代表节点/父亲
    # nodes[1] 表示节点1的孩子们
    def findRedundantConnection(self, edges):
        parent = {} # `节点` -> `代表节点`
        nodes = {} # `代表节点` -> `节点`, 代表节点的集合
        for i in range(len(edges)):
            parent[i+1] = i+1
            nodes[i+1] = [i+1]
        for e in edges:

            if parent[e[0]] != parent[e[1]]:
                e0_parent = parent[e[0]]
                e1_parent = parent[e[1]]

                nodes[e1_parent].extend(nodes[e0_parent]) # 可能我的孩子已经过继了，所以，要转移我孩子养父的所有孩子
                for i in nodes[e0_parent]: # 给孩子改姓
                    parent[i] = e1_parent
                nodes[e0_parent] = []

                # print(e)
                # print(parent)
                # print(nodes)
            else:
                print(e)
                return e
        return []
s = Solution()
s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]])