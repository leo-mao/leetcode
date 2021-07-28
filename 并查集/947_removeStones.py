class Solution:
    def removeStones(self, stones):
        parent = {}
        nodes = {}
        # i 表示输入编号为i的石头
        # parent[i] 是节点i的代表节点编号
        # nodes[i]是以i为代表节点的节点编号
        for i in range(len(stones)):
            parent[i] = i
            nodes[i] = [i]

        # print(parent, nodes)

        for i in range(len(stones)-1):
            for j in range(len(stones)):
                if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]) and (parent[i] != parent[j]):
                    parent_j = parent[j]
                    # parent[s[j]] = parent[i]
                    for n in nodes[parent_j]: 
                        parent[n] = parent[i]
                    nodes[parent[i]].extend(nodes[parent_j])
                    nodes[parent_j] = []
                    # print(parent, nodes)
        
        distinct = []
        for i in parent.values():
            if i not in distinct:
                distinct.append(i)
        # print(distinct)
        return len(stones) - len(distinct)

def main():
    s = Solution()
    l = 
    print(s.removeStones(l))
