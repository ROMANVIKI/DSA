class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        # Edge case: if the list is empty or has only one node, return it as is
        if not head or not head.next:
            return head
        
        current = head  # Start with the head of the linked list
        
        while current and current.next:  # Loop through the list
            if current.val == current.next.val:  # Check if the current node's value is the same as the next one
                current.next = current.next.next  # Skip the next node if it's a duplicate
            else:
                current = current.next  # Move to the next node if no duplicate
        
        return head  # Return the modified linked list




# The test cases to use with this Solution

# Create a linked list: 1 -> 1 -> 2
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)

# Call the function
solution = Solution()
new_head = solution.deleteDuplicates(head)

# Resulting linked list will be: 1 -> 2

