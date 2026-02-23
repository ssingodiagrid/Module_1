# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head

        # Push values into stack
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next

        temp = head

        # Pop values back into linked list
        while stack:
            temp.val = stack.pop()
            temp = temp.next

        return head