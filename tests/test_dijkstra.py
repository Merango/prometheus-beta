import pytest
from src.dijkstra import dijkstra, reconstruct_path

def test_basic_dijkstra():
    # Simple graph with known shortest paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test distances
    distances, previous = dijkstra(graph, 'A')
    assert distances == {
        'A': 0,
        'B': 3,  # via C
        'C': 2,
        'D': 6   # via C and B
    }

def test_disconnected_node():
    graph = {
        'A': {'B': 4},
        'B': {},
        'C': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    assert distances == {
        'A': 0,
        'B': 4,
        'C': float('inf')
    }

def test_path_reconstruction():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Run Dijkstra
    distances, previous = dijkstra(graph, 'A')
    
    # Reconstruct path
    path = reconstruct_path(previous, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']

def test_single_node_graph():
    graph = {'A': {}}
    
    distances, previous = dijkstra(graph, 'A')
    assert distances == {'A': 0}

def test_error_handling():
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    
    # Test non-existent start node
    with pytest.raises(ValueError, match="Start node 'C' not found in the graph"):
        dijkstra(graph, 'C')

def test_no_path_between_nodes():
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    
    # Run Dijkstra from A
    distances, previous = dijkstra(graph, 'A')
    
    # Test path reconstruction when no path exists
    with pytest.raises(ValueError, match="No path exists between A and B"):
        reconstruct_path(previous, 'A', 'B')

def test_complex_graph():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5, 'E': 6},
        'D': {'E': 2},
        'E': {}
    }
    
    # Test Dijkstra with a more complex graph
    distances, previous = dijkstra(graph, 'A')
    
    # Verify distances
    assert distances == {
        'A': 0,
        'B': 3,  # via C
        'C': 2,
        'D': 6,  # via C and B
        'E': 4   # via B
    }
    
    # Reconstruct path to E
    path = reconstruct_path(previous, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']