#938 Range Sum of BST

#O(log(n)) solution 73% runtime 88% memory Recursive

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangeSumBSTHelper(root,low,high):
            if not root: # check if the root is none
                return 0
            elif root.val < low: # if the value is lower than the low check the right side if it has a higher value
                return rangeSumBSTHelper(root.right,low,high)
            elif root.val > high: # if the value is higher than the high check the left side if it has a lower value
                return rangeSumBSTHelper(root.left,low,high)
            return root.val + rangeSumBSTHelper(root.left,low,high) + rangeSumBSTHelper(root.right,low,high)
            # if the value is in between the low and high add them to the sum
        #print(rangeSumBSTHelper(root,low,high))
        
        return rangeSumBSTHelper(root,low,high)
        


        
        