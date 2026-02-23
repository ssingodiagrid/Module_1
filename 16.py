# 19. Remove Nth Node From End of List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head

        fast = temp
        slow = temp

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches last node
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Delete nth node from end
        slow.next = slow.next.next

        return temp.next
        