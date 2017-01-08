def FastTargetedOrder(ugraph):
	DegreeSets = [0]*len(ugraph)
	for k in range(len(ugraph)):
		DegreeSets[k] = set()
	for i in range(len(ugraph)):
		d = len(ugraph[i])
		DegreeSets[d].add(i)
	L = ['']*len(ugraph)
	i = 0
	for k in range(len(ugraph)):
		print "Degree Sets at", k, "is", DegreeSets[k]
	for k in range(len(ugraph)-1,-1,-1):
		print "DegreeSets",k, "is", DegreeSets[k]
		while DegreeSets[k] != set():
			u = random.sample(DegreeSets[k],1)
			print "u",u
			DegreeSets[k] = DegreeSets[k] - set(u)
			neighbors = ugraph[u[0]]
			print "The neighbors of node",u[0],"are", neighbors
			for neighbor in neighbors:
				d = len(ugraph[neighbor])
				print "Node", neighbor, "has", d, "connections"
				print "DegreeSets[",d,"]", "is", DegreeSets[d]
				DegreeSets[d] = DegreeSets[d] - set([neighbor])
				DegreeSets[d-1].add(neighbor)
			L[i] = u[0]
			i += 1
			delete_node(ugraph,u[0])
	return L