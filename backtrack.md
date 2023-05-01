

## Easy
1. Permutations(Completed)
2. Subsets(Completed)
3. Combinations

## Medium
1. Generate Parentheses
2. Count Numbers with Unique Digits
3. Target Sum
4. 

## Hard
1. n queens
2. Sudoku
3. Expression Add Operators
4. Word Break II
5. Expression Add Operators
6. Knight's tour

# TODO

## Combinations
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
[Question](https://leetcode.com/problems/combinations/)

Example 1:

Input: n = 4, k = 2
Output: \[\[1,2\],\[1,3\],\[1,4\],\[2,3\],\[2,4\],\[3,4\]\]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., \[1,2\] and \[2,1\] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: \[\[1\]\]
Explanation: There is 1 choose 1 = 1 total combination.

## Count Numbers with Unique Digits
Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.
[Question](https://leetcode.com/problems/count-numbers-with-unique-digits/)

Example 1:
Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99

Example 2:
Input: n = 0
Output: 1

## Target Sum
You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
[Question](https://leetcode.com/problems/target-sum/)

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

## Expression Add Operators
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.
[Question](https://leetcode.com/problems/expression-add-operators/)

Example 1:
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Example 3:
Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.

## Word Break II
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
[Question](https://leetcode.com/problems/word-break-ii/)

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

