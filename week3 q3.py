class Node:
    def __init__(self):
        self.data = None
        self.next = None

def deleteNode(head, x):
    # If the head is to be deleted
    if x == 1:
        return head.next
    
    current = head
    # Traverse the list to find the (x-1)-th node
    for i in range(x - 2):
        if current is None:
            return head  # If x is out of range
        current = current.next
    
    # current now points to (x-1)-th node, so we can delete the x-th node
    if current and current.next:
        current.next = current.next.next
    
    return head

