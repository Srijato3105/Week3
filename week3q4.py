'''
	A linked list node has the following structure
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def getKthFromLast(self, head, k):
        fast = slow = head
        
        # Move the fast pointer k steps ahead
        for _ in range(k):
            if fast is None:
                return -1  # If k is larger than the length of the list
            fast = fast.next
        
        # Move both pointers one step at a time
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.data if slow else -1

