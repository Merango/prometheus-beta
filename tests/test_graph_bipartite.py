import pytest
from src.graph_bipartite import is_bipartite

def test_simple_bipartite_graph():
    """Test a simple bipartite graph"""
    graph = [
        [1, 3],    # Node 0 connects to nodes 1 and 3
        [0, 2],    # Node 1 connects to nodes 0 and 2
        [1, 3],    # Node 2 connects to nodes 1 and 3
        [0, 2]     # Node 3 connects to nodes 0 and 2
    ]
    assert is_bipartite(graph) == True

def test_non_bipartite_graph():
    """Test a graph that is not bipartite"""
    graph = [
        [1, 2, 3],  # Node 0 connects to nodes 1, 2, and 3
        [0, 2],     # Node 1 connects to nodes 0 and 2
        [0, 1, 3],  # Node 2 connects to nodes 0, 1, and 3
        [0, 2]      # Node 3 connects to nodes 0 and 2
    ]
    assert is_bipartite(graph) == False

def test_disconnected_bipartite_graph():
    """Test a disconnected bipartite graph"""
    graph = [
        [1],        # First component
        [0],
        [3],        # Second component
        [2]
    ]
    assert is_bipartite(graph) == True

def test_disconnected_non_bipartite_graph():
    """Test a disconnected non-bipartite graph"""
    graph = [
        [1, 2],     # First component
        [0, 2],
        [0, 1],
        [4, 5],     # Second component
        [3, 5],
        [3, 4]
    ]
    assert is_bipartite(graph) == False

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        is_bipartite([])

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = [[]]
    assert is_bipartite(graph) == True

def test_two_node_graph_connected():
    """Test a two-node graph that is bipartite"""
    graph = [[1], [0]]
    assert is_bipartite(graph) == True

def test_two_node_graph_not_connected():
    """Test a two-node graph that is not connected"""
    graph = [[], []]
    assert is_bipartite(graph) == True