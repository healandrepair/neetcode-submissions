# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        string1 = self.GetNumbers(l1)
        string2 = self.GetNumbers(l2)

        finalResult = str(int(string1) + int(string2))
        newNode = ListNode(finalResult[-1])
        current = newNode
        for i in range(len(finalResult) - 2, -1, -1):
            current.next = ListNode(finalResult[i])
            current = current.next
        return newNode



    def GetNumbers(self, node):
        if (node.next == None):
            return str(node.val)
        
        return str(self.GetNumbers(node.next)) + str(node.val)