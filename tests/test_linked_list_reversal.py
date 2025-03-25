import pytest
from src.linked_list_reversal import Node, reverse_linked_list

def list_to_array(head):
    """Helper function to convert linked list to array for easy assertion"""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def test_reverse_empty_list():
    """Test reversing an empty list"""
    assert reverse_linked_list(None) is None

def test_reverse_single_node_list():
    """Test reversing a list with a single node"""
    head = Node(5)
    reversed_head = reverse_linked_list(head)
    assert list_to_array(reversed_head) == [5]

def test_reverse_multiple_nodes():
    """Test reversing a list with multiple nodes"""
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    # Reverse the list
    reversed_head = reverse_linked_list(head)
    
    # Check if list is correctly reversed
    assert list_to_array(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_two_nodes():
    """Test reversing a list with two nodes"""
    head = Node(1)
    head.next = Node(2)
    
    reversed_head = reverse_linked_list(head)
    
    assert list_to_array(reversed_head) == [2, 1]