# Table Of Contents

## Basic API
1. Add Element(Completed)
2. Search for Element(Completed)
3. Remove Element
4. Visualize tree
## Easy
1. Binary Tree Inorder Traversal(Completed)
2. Binary Tree Preorder Traversal(Completed)
3. Binary Tree PostOrder Traversal(Completed)
4. Binary Tree Level order traversal(Completed)
5. Same Tree(Completed)
6. Symmetric Tree
7. Height(Completed)
8. Array to BST

## Medium
1. Unique Binary Search Tree
2. Unique Binary Search Tree 2
3. Recover BST
4. Zigzag traversal
5. 

## Hard
1. Serialize and Deserialize BST



# Binary Tree Inorder Traversal(completed)

Given the root of a binary tree, return the inorder traversal of its nodes' values. In an inorder traversal, we first visit the left subtree of a node, then visit the node itself, and finally visit the right subtree of the node
[Question](https://leetcode.com/problems/same-tree/)

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

# Binary Tree Preorder Traversal(completed)

Given the root of a binary tree, return the preorder traversal of its nodes' values. Binary Tree Preorder Traversal is a tree traversal algorithm that visits the root node first, then recursively visits the left subtree and then the right subtree.
[Question](https://leetcode.com/problems/binary-tree-preorder-traversal/)
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

# Binary Tree PostOrder Traversal(completed)

Given the root of a binary tree, return the postorder traversal of its nodes' values. In postorder traversal, we first visit the left subtree, then the right subtree, and finally the root node.
[Question](https://leetcode.com/problems/binary-tree-postorder-traversal/)
Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

# Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
[Question](https://leetcode.com/problems/same-tree/)

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

# Balanced BST

Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
[Question](https://leetcode.com/problems/balanced-binary-tree/)


Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

## Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
[Question](https://leetcode.com/problems/symmetric-tree/)

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

## Height
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

## Binary Tree Paths
Given the root of a binary tree, return all root-to-leaf paths in any order.A leaf is a node with no children.
[Question](https://leetcode.com/problems/binary-tree-paths/)

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

## Sorted Array To Balanced BST
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9]

## Unique Binary Search Tree
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.
(1 <= n <= 8)
[Question](https://leetcode.com/problems/unique-binary-search-trees/)

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

## Unique Binary Search Tree 2
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.
(1 <= n <= 8)
[Question](https://leetcode.com/problems/unique-binary-search-trees-ii/)

Example 1:
Input: n = 3
Output: \[\[1,null,2,null,3\],\[1,null,3,2\],\[2,1,3\],\[3,1,null,null,2\],\[3,2,null,1\]\]

Example 2:
Input: n = 1
Output: \[\[1\]\]

## Recovery Binary Search Tree
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

## Zigzag traversal
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:
Input: root = \[3,9,20,null,null,15,7\]
Output: \[\[3\],\[20,9\],\[15,7\]\]


## Serialize and Deserialize