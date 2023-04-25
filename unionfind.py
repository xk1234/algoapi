class UnionFind:
    def __init__(self, size):
        for i in range(size):
            self.id = i # Link to itself (self root)
            self.sz = 1 # Each component is originally of size one
        pass

    def find(self, elem):
        """
        Find which component/set 'p' belongs to, takes amortized constant time.
        """
        pass

    def union(self, p, q):

        pass


