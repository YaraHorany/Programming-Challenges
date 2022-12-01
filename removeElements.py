# Given the head of a linked list and an integer val, 
# remove all the nodes of the linked list that has Node.val == val, and return the new head.

"""
Example:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return head
        prev = head
        cur = head
        while cur:
            if cur.val == val:
                if cur == head:
                    head = head.next
                    prev = prev.next
                else:
                    prev.next = cur.next
            else:
                if prev != cur:
                    prev = prev.next
            cur = cur.next
        return head
