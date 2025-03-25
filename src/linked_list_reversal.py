class Node:
    """
    Represents a node in a singly linked list.
    
    Attributes:
        value: The value stored in the node
        next: Reference to the next node in the list (or None)
    """
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    """
    Reverse a linked list in-place.
    
    Args:
        head (Node): The head of the linked list
    
    Returns:
        Node: The new head of the reversed linked list
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize three pointers
    prev = None
    current = head
    
    # Traverse and reverse links
    while current:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # prev is now the new head
    return prev