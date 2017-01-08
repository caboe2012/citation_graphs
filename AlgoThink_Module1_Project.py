""" Algorithmic Thinking - Module 1: Project Graphs """
from collections import defaultdict
import urllib2
import matplotlib.pyplot as plt
import math

EDGES = 352768
# Constant Dictionary Representations of Graphs as described by Adjacency Lists (NOT matrices)
EX_GRAPH0 = {0: set([1,2]),
			 1: set([]),
			 2:	set([]),
			 }

EX_GRAPH1 = {0: set([1,4,5]),
			 1: set([2,6]),
			 2: set([3]),
			 3: set([0]),
			 4: set([1]),
			 5: set([2]),
			 6: set([]),
			 }

EX_GRAPH2 = {0: set([1,4,5]),
			 1: set([2,6]),
			 2: set([3,7]),
			 3: set([7]),
			 4: set([1]),
			 5: set([2]),
			 6: set([]),
			 7: set([3]),
			 8: set([1,2]),
			 9: set([0,3,4,5,6,7]),
			 }

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"


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

#print make_complete_graph(4)

 
def compute_in_degrees_DUMB(digraph):
	''' Takes a directed graph _digraph_ (represented as 
 	as a dictionary) and computes the in-degrees for
 	the nodes in the graph '''
 	_in_degree_dict = {}
 	for _node,_ignore in digraph.items():
 		_num_edges = 0
 		for _key,_values in digraph.items():
 			for _each_value in _values:
 				if _each_value == _node:
 					_num_edges += 1
 		_in_degree_dict[_node] = _num_edges
 	return _in_degree_dict


def compute_in_degrees(digraph):
	''' Takes a directed graph _digraph_ (represented as 
 	as a dictionary) and computes the in-degrees for
 	the nodes in the graph '''
 	ans = defaultdict(int)
 	for i,j in digraph.items():
 		for paper in j:
 			ans[paper] += 1
 	for i,j in digraph.items():
 		if i not in ans:
 			ans[i] = 0
 	return ans




GRAPH7 = {0: set([1, 2, 3, 4]), 
          1: set([0, 2, 3, 4]), 
          2: set([0, 1, 3, 4]), 
          3: set([0, 1, 2, 4]), 
          4: set([0, 1, 2, 3]), 
          5: set([2, 3, 4]), 
          6: set([0, 1, 4]), 
          7: set([0, 1, 2, 3]), 
          8: set([0, 1, 4, 7]), 
          9: set([2, 4]), 
          10: set([1, 2, 4]), 
          11: set([1, 3, 4, 7]), 
          12: set([0, 2, 3]), 
          13: set([0, 2, 4, 10]), 
          14: set([0, 2, 3, 4, 13])}
print compute_in_degrees(GRAPH7)

def in_degree_distribution(digraph):
	''' Takes a directed graph _digraph_ (represented as 
	a dictionary) and computes the unnormalized distribution
	of the in-degrees of the graph'''
	_temp = compute_in_degrees(digraph)
	_ans = defaultdict(int)
	for _key,_value in _temp.items():
		_ans[_value] += 1
 	return _ans

def normalized_in_degree_distribution(unnormalized_distro):
	''' Takes an unnormalized ph_ (represented as 
	a dictionary) and computes the normalized distribution
	of the in-degrees of the graph'''
	total_nodes = 0.
	final_ans  = {}
	for k,v in unnormalized_distro.items():
		total_nodes += v
	for k,v in unnormalized_distro.items():
		final_ans[k] = v/total_nodes
	return final_ans

#print in_degree_distribution(GRAPH0)



def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

#citation_graph = load_graph(CITATION_URL)
#print type(citation_graph)

def plot_log_graph(normalized_distro, title):
	''' Takes a dictonary contatining normalized distro of in-degrees of a graph and plots the log/log graph'''
	x = []
	y = []
	for k,v in normalized_distro.items():
		if k == 0:
			pass
		else:
			x.append(math.log(k))
			y.append(math.log(v))
	plt.scatter(x,y)
	plt.xlabel("Log of Number of In-degrees")
	plt.ylabel("Log of Normalized In-Degree Distribution")
	plt.title(title)
	plt.show()



def compute_out_degree(digraph):
	'''compute the average number of out_degrees in the citation_graph'''
	total_out_degrees = 0.
	total_nodes = 0
	for k,v in digraph.items():
		out_degrees = len(v)
		total_out_degrees += out_degrees
		total_nodes += 1
	average_out_degrees = total_out_degrees/total_nodes
	return average_out_degrees

def DPA(n,m):
	'''Compute randomly generated additional nodes from m to n
	starting from a complete graph of m nodes.'''
	V = range(0,m)
	E = make_complete_graph(m)
	total_in_degrees = m*(m-1)
	randomly_added_nodes = 0
	for i in range(m,n):
		total_in_degrees += randomly_added_nodes
		V_prime = 0
		


 