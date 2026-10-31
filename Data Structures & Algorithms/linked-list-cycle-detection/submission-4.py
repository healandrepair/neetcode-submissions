# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while slow and fast:
            if (fast.next and fast.next.next):
                if (slow == fast.next.next):
                    return True
                
                fast = fast.next.next
            else:
                break
            
            slow = slow.next
        
        return False

