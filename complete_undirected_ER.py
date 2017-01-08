import random

def undirected_ER(n,p):
	temp = {}
	V = range(0,n)
	for node_i in V:
		temp[node_i] = set()
	for node_i in V:
		for node_j in V:
			a = random.random()
			if node_i == node_j:
				pass
			elif a < p and node_j not in temp[node_i]:
				temp[node_i].add(node_j)
				temp[node_j].add(node_i)
	return temp

test1 = undirected_ER(10,0.5)
print test1
for k,v in test1.items():
	print k, ":", v