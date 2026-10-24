# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if (not root):
            return None
        
        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            if (not root.left):
                return root.right
            elif( not root.right):
                return root.left

            # get the min leaf of the right sub tree
            leaf = self.findMin(root.right)
            root.val = leaf.val
            #  set the value of the leaf to the root
            root.right = self.deleteNode(root.right, leaf.val)
            # Now get rid of the duplicate by running deleteNode recurisvely against the right subtree and use the key as delete
        return root


    def findMin(self, root):
        curr = root;

        while curr and curr.left:
            curr = curr.left
        
        return curr


        