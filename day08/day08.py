class InstruExecutor:
	def __init__(self,inputPath):
		self.instructions = InstruExecutor.processRawData(inputPath)
		self.fixed = False
		self.fixedAcc = 0

	def executeIntructs(self):
		return self.executeSingleLine(0,0,[])		

	def executeSingleLine(self, acc, row, visited):
		if row in visited:
			return acc
		else:
			visited.append(row)
		line = self.instructions[row]
		op = line[0]
		num = line[1]
		if op == "nop":
			return self.executeSingleLine(acc, row+1,visited)
		elif op=="acc":
			return self.executeSingleLine(acc+num,row+1,visited)
		elif op =="jmp":
			return self.executeSingleLine(acc,row+num, visited)

	def fixIntructs(self):
		self.fixSingleLine( 0, 0, [], False)
		return self.fixedAcc

	def fixSingleLine(self, acc, row, visited, switched):
		if self.fixed :
			return
		if row in visited or row>=len(self.instructions):
			return
		else:
			visited.append(row)
		line = self.instructions[row]
		op = line[0]
		num = line[1]
		if row == len(self.instructions) -1:
			acc = acc+num if op=="acc" else acc
			self.fixed = True
			self.fixedAcc = acc
		if op=="acc":
			acc+=num
			self.fixSingleLine(acc,row+1,visited, switched)
		else:
			if op =="jmp":
				self.fixSingleLine(acc,row+num, visited, switched)
				if not switched:
					self.fixSingleLine(acc, row+1,visited.copy(), True)
			elif op =="nop":
				self.fixSingleLine(acc,row+1, visited, switched)
				if not switched:
					self.fixSingleLine(acc, row+num,visited.copy(), True)

	@staticmethod
	def processRawData(location):
		text = open(location)
		lines = text.readlines()
		text.close()
		operations = [[line.split()[0], int(line.split()[1])] for line in lines]
		return operations

if __name__ == "__main__":
	instruExecutor = InstruExecutor("input.txt")
	print("part 1:", instruExecutor.executeIntructs())
	print("part 2:", instruExecutor.fixIntructs())