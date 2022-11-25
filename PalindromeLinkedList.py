# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

"""
Example:
Input: head = [1,2,2,1]
Output: true
"""

# The space complexity is O(1)
# The time complexity is O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None:  # if it's an empty linked list then just return true
            return True
        
        slow = fast = head
        temp = None

        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            temp = slow
            slow = slow.next

        # slow stands on the first node of the second part
        # temp stands on the last node of the first part
        curr = nxt = slow

        # reversing the second part of the linked list
        prev = None
        while nxt != None:
            nxt = nxt.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp.next = prev # connecting the two parts
        slow = temp.next
        # comparing the first part to the second part
        while slow != None:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True