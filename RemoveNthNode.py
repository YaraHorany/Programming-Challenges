""" 
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# The space complexity is O(1)
# The time complexity is O(N)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        count = 0
        cur = head
        while cur != None: # counting the total number of nodes
            count += 1
            cur = cur.next

        n = count - n
        if n == 0: # if we want to remove the head (first node) of the linkedlist
            head = head.next
            return head

        count = 0
        cur = head
        prev = None
        while cur and count != n:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = cur.next # removing cur node
        return head
