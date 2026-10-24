# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Go for fast and slow pointer

        fast = head
        slow = head

        while fast and fast.next:
            print(f"slow:{slow.val}")
            print(f"fast:{fast.val}")
            slow = slow.next
            fast = fast.next.next
                

        return slow
