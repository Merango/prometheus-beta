import pytest
from src.bfs import breadth_first_search

def test_basic_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Basic traversal
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_single_node_graph():
    graph = {'X': []}
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_disconnected_graph():
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_visit_function():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }
    
    # Stop searching after reaching 'B'
    def stop_at_b(node):
        return node == 'B'
    
    result = breadth_first_search(graph, 'A', visit=stop_at_b)
    assert result == ['A', 'B']

def test_nonexistent_start_node():
    graph = {'A': ['B'], 'B': ['A']}
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        breadth_first_search(graph, 'X')

def test_empty_graph():
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        breadth_first_search({}, 'X')