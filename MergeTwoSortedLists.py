"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        # we're creating a new linked list which includes both merged lists
        if list1.val <= list2.val:
            head = ListNode(list1.val)
            list1 = list1.next
        else:
            head = ListNode(list2.val)
            list2 = list2.next
            
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                temp = ListNode(list1.val)
                cur.next = temp
                cur = temp
                list1 = list1.next
            else:
                temp = ListNode(list2.val)
                cur.next = temp
                cur = temp
                list2 = list2.next
                
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2
        return head