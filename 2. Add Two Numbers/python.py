# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize dummy node and current pointer
        dummy = curr = ListNode()
        # Initialize carry-over variable
        carry = 0
        # Iterate over both linked lists
        while l1 or l2:
            # Get the values of the current nodes or 0 if the linked list is shorter
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            # Add the values and the carry
            s = x + y + carry
            # Update the carry
            carry = s // 10
            # Append the current digit to the result linked list
            curr.next = ListNode(s % 10)
            curr = curr.next
            # Move to the next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # If there is still a carry, append it to the result linked list
        if carry:
            curr.next = ListNode(carry)
        return dummy.next

#time and space complexity is O(max(n, m)) where n is size of l1 and m is size of l2