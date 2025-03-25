import pytest
from src.linked_list import LinkedList, Node, create_linked_list

def test_node_creation():
    """Test Node class initialization"""
    node = Node(5)
    assert node.value == 5
    assert node.next is None

def test_linked_list_append():
    """Test appending nodes to a linked list"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    
    assert ll.to_list() == [1, 2, 3]

def test_linked_list_reverse_empty():
    """Test reversing an empty linked list"""
    ll = LinkedList()
    ll.reverse()
    assert ll.to_list() == []

def test_linked_list_reverse_single_node():
    """Test reversing a linked list with a single node"""
    ll = LinkedList()
    ll.append(1)
    ll.reverse()
    assert ll.to_list() == [1]

def test_linked_list_reverse_multiple_nodes():
    """Test reversing a linked list with multiple nodes"""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.reverse()
    assert ll.to_list() == [4, 3, 2, 1]

def test_create_linked_list():
    """Test creating a linked list with n nodes"""
    ll = create_linked_list(5)
    assert ll.to_list() == [0, 1, 2, 3, 4]

def test_create_linked_list_zero_nodes():
    """Test creating a linked list with zero nodes"""
    ll = create_linked_list(0)
    assert ll.to_list() == []

def test_create_linked_list_negative_nodes():
    """Test creating a linked list with negative nodes"""
    with pytest.raises(ValueError, match="Number of nodes must be non-negative"):
        create_linked_list(-1)