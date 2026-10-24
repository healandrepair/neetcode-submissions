# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)

        finalList = []
        while len(queue) > 0:
            subList = []
            for i in range(len(queue)):
                v = queue.popleft()
                
                if (v is not None):
                    subList.append(v.val)
                    queue.append(v.left)
                    queue.append(v.right)

            if (subList):
                finalList.append(subList)

        return finalList