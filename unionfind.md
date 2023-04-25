The union-find, or disjoint-set, data structure is used to model a collection of non-overlapping sets of elements.

find(x)
Finds the set that x is a part of. This function returns a representative element of that set.

union(x, y)
Merges the sets containing x and y into a single set.

# Path Compression
In path compression, whenever we traverse the tree for a FIND operation we attach all nodes traversed in getting to the root directly to the root; this maintains the validity of the structure, since the root is the representative for all these nodes. The intuition is that any subsequent calls to FIND on the same node or any recursive parent of the node will be faster.

