import re
from functools import reduce
def loadData(path):
	with open("input.txt", "r") as file:
		data = file.read().split("\n\n")
	return data[0].split('\n'),[int(num) for num in data[1].split('\n')[1].split(',')],[[int(num) for num in line.split(',')] for line in data[2].split('\n')[1:]]

def makeClosure(begin1, end1, begin2, end2):
	return lambda x: ((x>=begin1 and x<= end1) or (x>=begin2 and x<=end2))

def parseRules(rawRules):
	return {name:makeClosure(begin1,end1,begin2,end2) for name,begin1,end1,begin2,end2 in [[int(item) if item.isdigit() else item for item in re.split(": | or |-",rawRule)] for rawRule in rawRules]}

def isParamValid(param,rules):
	return any([rule(param) for rule in rules.values()])

def isTicketValid(ticket, rules):
	return all([isParamValid(param,rules) for param in ticket])
# Part 1
def sumInvalidNum(tickets, rules):
	return sum([0 if isParamValid(param,rules) else param for ticket in tickets for param in ticket])
# Part 2
def filterValidTickets(tickets,rules):
	return [ticket for ticket in tickets if isTicketValid(ticket, rules)]

def matchSingleField(tickets,rule):
	return [i for i in range(len(tickets[0])) if all([rule(tickets[row][i]) for row in range(len(tickets))])]

def removeIdx(fieldsMap, num):
	for field, idx in fieldsMap.items():
		if num in idx: 
			idx.remove(num)
	return fieldsMap

def eliminatePossibilities(possibleMap):
	finalMap = {}
	while len(finalMap)!= len(possibleMap):
		for field, idx in possibleMap.items():
			if(len(idx)== 1):
				finalMap[field] = idx[0]
				possibleMap = removeIdx(possibleMap,idx[0])
	return finalMap

def multiplyValidDepFields(tickets,rules,myTicket):
	validTickets = filterValidTickets(tickets,rules)
	matchedPossibles = {name:matchSingleField(validTickets,rules[name]) for name in rules}
	matchFields = eliminatePossibilities(matchedPossibles)
	return reduce((lambda x, y: x * y), [myTicket[num] for field,num in matchFields.items() if field.startswith("departure")])
	
if __name__ == '__main__':
	rawRules, myTicket, nearbyTickets = loadData("input.txt")
	rules = parseRules(rawRules)
	print("Part 1:",sumInvalidNum(nearbyTickets,rules))
	print("Part 2:",multiplyValidDepFields(nearbyTickets,rules,myTicket))