class UnionFind:

    def __init__(self, size) -> None:
        self.parent = [i for i in range(size)]

    def find(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        rootX = self.find(node1)
        rootY = self.find(node2)
        if rootX != rootY:
            self.parent[rootY] = rootX

    def connected(self, node1, node2):
        return self.find(node1) == self.find(node2)


if __name__ == '__main__':

    # My Test Case
    uf = UnionFind(10)

    # 1-2-5-6-7, 3-8-9, 4
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)

    print(uf.connected(1, 5))
    print(uf.connected(5, 7))
    print(uf.connected(4, 9))

    uf.union(9, 4)
    print(uf.connected(4, 9))

    print(uf.connected(2, 3))
    uf.union(5, 4)
    print(uf.connected(2, 3))
    print(uf.connected(5, 4))
    print(uf.connected(7, 8))
    print(uf.connected(2, 9))
