# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        finalArray = []

        q = deque()
        q.append(root)

        while q:
            levelSize = len(q)

            for i in range(len(q)):

                node = q.popleft()
                if (not node):
                    continue

                if (node.left):
                    q.append(node.left)
                if (node.right):
                    q.append(node.right)
                
                if (i == levelSize - 1):
                    finalArray.append(node.val)

        return finalArray
        