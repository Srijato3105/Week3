'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    def insertAtEnd(self, head, x):
        if head==None:
            n=Node(x)
            return n
        ptr=head
        while(ptr.next !=None):
            ptr=ptr.next
        n=Node(x)
        ptr.next=n
        return head
