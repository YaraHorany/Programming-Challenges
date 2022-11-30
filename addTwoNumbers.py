"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
The number of nodes in each linked list is in the range [1, 100].

Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        prev = head
        prev.val = (l1.val + l2.val) % 10
        carry = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        while l1 != None or l2 != None:
            cur = ListNode()
            prev.next = cur
            prev = cur
            if l1 and l2:
                cur.val = (l1.val + l2.val + carry) % 10
                carry = (l1.val + l2.val + carry) // 10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                cur.val = (l1.val + carry) % 10
                carry = (l1.val + carry) // 10
                l1 = l1.next
            else: # l2 only exists
                cur.val = (l2.val + carry) % 10
                carry = (l2.val + carry) // 10
                l2 = l2.next
        if carry != 0:
            cur = ListNode(carry)
            prev.next = cur
        return head
