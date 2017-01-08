"""
Provided code for application portion of module 2

Helper class for implementing efficient version
of UPA algorithm
"""

import random

n = 1239 # number of nodes from example computer network
m = 3047 # number of edges from example computer network


class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

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

def create_UPA_graph(m,n):
    complete_ugraph = make_complete_graph(m)
    UPA_obj = UPATrial(m)
    for _new_node in range(m,n):
        _new_node_edges = UPA_obj.run_trial(m)
        complete_ugraph[_new_node] = _new_node_edges
        for _edge in _new_node_edges:
            complete_ugraph[_edge].add(_new_node)
    return complete_ugraph

def optimal_m(trials, m):
    results = []
    for trial in range(trials):
        total_edges_per_trial = 0
        check = create_UPA_graph(m,1239)
        for node in check.keys():
            total_edges_per_trial += len(check[node])
        ans = total_edges_per_trial/2.
        final = ans/1239.
        results.append(final)
    return results
#print optimal_m(10,3)

test_UPA = create_UPA_graph(3,1239)
print test_UPA

def random_order(ugraph):
    '''Takes a graph and returns a list of the nodes in the graph in some random order.'''
    V = ugraph.keys()
    n = len(V)
    random_node_order = random.sample(V,n)
    return random_node_order 



print len(random_order(test_UPA))
check = random_order(test_UPA)
print all(x in check for x in range(0,1239))