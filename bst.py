import array
import numpy as np
from graphviz import Digraph

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
        pass

    @staticmethod
    def inorder(n):
        # left center right
        if n == None:
            return []
        return  BST.inorder(n.left) + [n.data] + BST.inorder(n.right)

    @staticmethod
    def preorder(n):
        if n == None:
            return []
        return [n.data] + BST.preorder(n.left) + BST.preorder(n.right)

    @staticmethod
    def postorder(n):
        if n == None:
            return []
        return BST.postorder(n.left) + BST.postorder(n.right) + [n.data]

    def levelorder(self):
        ordering = []
        q = [self.root]
        while len(q) > 0:
            # get first
            n = q.pop(0)
            ordering.append(n.data)
            if n.left is not None:
                q.append(n.left)
            if n.right is not None:
                q.append(n.right)
        return ordering

    @staticmethod
    def same_t(r1, r2):
        if r1 is None and r2 is not None:
            return False
        if r2 is None and r1 is not None:
            return False
        if r1 is None and r2 is None:
            return True
        if r1.data != r2.data:
            return False

        return BST.same_t(r1.left, r2.left) and BST.same_t(r1.right, r2.right)

    @staticmethod
    def height(n):
        if n is None:
            return 0
        return max(BST.height(n.left), BST.height(n.right)) + 1

    def add(self, elem):
        x = b.search(elem)
        if elem > x.data:
            x.right = Node(elem)
            return x.right
        elif elem < x.data:
            x.left = Node(elem)
            return x.left
        else:
            return x

    # @TODO
    def remove(self, elem):
        pass

    def size(self):
        def size_helper(n):
            if n is None:
                return 0
            return size_helper(n.left) + size_helper(n.right) + 1
        return size_helper(self.root)

    def search(self, elem):
        curr = self.root
        while True:
            if elem > curr.data:
                if curr.right is not None:
                    curr = curr.right
                    continue
                else:
                    break
            if elem < curr.data:
                if curr.left is not None:
                    curr = curr.left
                    continue
                else:
                    break
            if elem ==  curr.data:
                break
        return curr
    
    @staticmethod
    def visualize_tree(tree):
        def add_nodes_edges(tree, dot=None):
            # Create Digraph object
            if dot is None:
                dot = Digraph()
                dot.node(name=str(tree), label=str(tree.data))

            # Add nodes
            if tree.left:
                dot.node(name=str(tree.left) ,label=str(tree.left.data))
                dot.edge(str(tree), str(tree.left))
                dot = add_nodes_edges(tree.left, dot=dot)
                
            if tree.right:
                dot.node(name=str(tree.right) ,label=str(tree.right.data))
                dot.edge(str(tree), str(tree.right))
                dot = add_nodes_edges(tree.right, dot=dot)

            return dot
        
        # Add nodes recursively and create a list of edges
        dot = add_nodes_edges(tree)

        # # Visualize the graph
        # display(dot)
        
        return dot
    
    

b = BST()
b.root = Node(25, Node(15, Node(10, Node(4), Node(12)), Node(22, Node(18), Node(24))), Node(50, Node(35, Node(31), Node(44)), Node(70, Node(66), Node(90))))
b2 = BST()
b2.root = Node(25, Node(15, Node(10, Node(4)), Node(22, Node(18), Node(24))), Node(50, Node(35, Node(31), Node(44)), Node(70, Node(66), Node(90))))
print(BST.inorder(b.root))
print(BST.preorder(b.root))
print(BST.postorder(b.root))
print(b.levelorder())
print(BST.same_t(b.root, b2.root))
print(BST.height(b.root))
allrs = []
for i in range(10):
    r = np.random.randint(0, 50)
    cnode = b.search(r)
    if cnode.data != r:
        b.add(r)
        allrs.append(r)
print(allrs)
print(f"size: {b.size()}")
print(b.search(18).data)

dot = BST.visualize_tree(b.root)
dot.format = 'png'
dot.view(filename='digraph', directory='./')