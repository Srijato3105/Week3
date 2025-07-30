'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''
class Node:
    def __init__(self, val):
        self.next = None
        self.data = val

class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # Edge case: if list is empty or has only one node, no loop can exist
        if not head or not head.next:
            return

        slow = fast = head
        
        # Detect if a loop exists using Floyd's Cycle Detection Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Loop detected
                self.removeLoopUtil(head, slow)
                return
    
    def removeLoopUtil(self, head, meeting_point):
        # Initialize the 'start' pointer from the head of the list
        start = head
        
        # Move both pointers (start and slow) one step at a time
        while start != meeting_point:
            start = start.next
            meeting_point = meeting_point.next
        
        # Now, meeting_point is at the start of the loop, we need to find the last node in the loop
        # and set its next to None
        prev = None
        while meeting_point.next != start:
            meeting_point = meeting_point.next
        
        # Remove the loop by setting the next pointer of the last node to None
        meeting_point.next = None

    # Function to check if there is a loop in the linked list
    def hasLoop(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
