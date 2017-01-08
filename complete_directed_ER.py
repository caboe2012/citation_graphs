import random

def undirected_ER(n,p):
	temp = {}
	V = range(0,n)
	E = 0
	for node_i in V:
		temp[node_i] = set()
		for node_j in V:
			a = random.random()
			if node_i == node_j:
				pass
			elif a < p:
				temp[node_i].add(node_j)
				if node_j not in temp.keys():
					temp[node_j] = set()
					temp[node_j].add(node_i)
				else:
					temp[node_j].add(node_i)
	return temp

test1 = undirected_ER(5,0.5)
for k,v in test1.items():
	print k, ":", v