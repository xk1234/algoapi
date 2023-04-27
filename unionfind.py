class UnionFind:
    def __init__(self, size):
        for i in range(size):
            self.id = i  # Link to itself (self root)
            self.sz = 1  # Each component is originally of size one
        pass

    def find(self, elem):
        """
        Find which component/set 'p' belongs to, takes amortized constant time.
        """
        path = [elem]
        while self.ids[elem] != elem:
            elem = self.ids[elem]
            path.append(elem)
        root = self.ids[elem]
        for nd in path:
            self.ids[nd] = root
        return self.ids[elem]

    def union(self, p1, p2):
        x = self.find(p1)
        y = self.find(p2)
        self.ids[x] = self.ids[y]
