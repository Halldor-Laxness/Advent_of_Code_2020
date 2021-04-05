def processRawData(location):
    text = open(location)
    lines = text.readlines()
    text.close()
    lines = "".join(lines).split("\n\n")
    return lines

def countGroupAnswerUnion(line):
	line = line.replace('\n','')
	return len(set(line))

def countGroupAnswerIntersection(line):
	answers = [set(item) for item in line.split('\n')]
	result = set.intersection(*answers)
	return len(result) 


def countAllAnswers(data , method):
	count = 0
	for line in data:
		count += method(line)
	return count
	

if __name__ == "__main__":
	data = processRawData("input.txt")
	sumOfCount = countAllAnswers(data,countGroupAnswerUnion)
	print("part 1: ", sumOfCount)
	sumOfCount = countAllAnswers(data,countGroupAnswerIntersection)
	print("part 2: ", sumOfCount)