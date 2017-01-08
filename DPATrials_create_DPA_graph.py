"""
Provided code for application portion of module 1

Helper class for implementing efficient version
of DPA algorithm
"""

# general imports
import random

n = 27700
# Edges in Citation Papers = 352,768
m = 13


#n = 20
#m = 3

def make_complete_graph(num_nodes):
    ''' returns a dictionary corresponding 
    to a complete directed graph with the specified '''
    _directed_graph = {}
    for _node_row in range(num_nodes):
        _num_edges = set([])
        for _node_col in range(num_nodes):
            if _node_row != _node_col:
                _num_edges.add(_node_col)
        _directed_graph[_node_row] = _num_edges
    return _directed_graph

class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors
    

def create_DPA_graph(m,n):
    complete_dgraph = make_complete_graph(m)
    test = DPATrial(m)
    for each in range(m,n):
#       print test._num_nodes, each
#       print test.run_trial(m)
        complete_dgraph[each] = test.run_trial(m)
    return complete_dgraph

print create_DPA_graph(m,n)
