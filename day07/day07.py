class BagGraph:

	def __init__(self):
		self.graph = {}

	def addRulesFromFile(self, location):
		data = self.processRawData(location)
		for line in data:
			self.addRule(line)

	def addRule(self, line):
		color, childrenColors, weights = self.parseRule(line)
		parent = self.getNode(color)
		children = [self.getNode(childColor) for childColor in childrenColors]
		parent.children = children
		parent.weights = weights
		for child in children:
			child.parents.append(parent)
		
	def getNode(self, color):
		if color in self.graph:
			return self.graph[color]
		else:
			node = Node(color)
			self.graph[color] = node
			return node

	def findParents(self, targetName):
		target = self.getNode(targetName)
		visited = set()
		toExplore = set()
		toExplore.update(target.parents)
		while(len(toExplore)>0):
			item = toExplore.pop()
			if not item.color in visited:
				visited.add(item.color)
				for newNode in item.parents:
					if newNode.color not in visited:
						toExplore.add(newNode)
		return len(visited)

	def countBagsByName(self, targetName):
		return self.countBags(self.getNode(targetName))-1

	def countBags(self, target):
		if( len(target.children)==0):
			return 1
		else:
			count = 1
			for node,number in  zip(target.children,target.weights):
				count+= number * self.countBags(node)
			return count

	@staticmethod
	def parseRule(line):
		color = line.split(" bags contain ")[0]
		edgeStatements = line.split(" bags contain ")[1]
		children = []
		weights = []
		if not edgeStatements.startswith("no other"):			
			for edgeStatement in edgeStatements.split(', '):
				components = edgeStatement.split()
				children.append(" ".join(components[1:-1]))
				weights.append(int(components[0]))
		
		return color, children, weights

	@staticmethod
	def processRawData(location):
		text = open(location)
		lines = text.readlines()
		text.close()
		return lines

class Node:
	def __init__(self, color):
		self.color = color
		self.children = []
		self.weights = []
		self.parents = []

if __name__ == "__main__":
	graph = BagGraph()
	graph.addRulesFromFile("input.txt")
	
	print("Part 1:", graph.findParents("shiny gold"))
	print("Part 2:", graph.countBagsByName("shiny gold"))