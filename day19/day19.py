def loadRules(path):
    with open(path, "r") as file:
        data = file.read().split("\n\n")
    return {rule.split(': ')[0]:rule.split(': ')[1] for rule in data[0].split('\n')},[message for message in data[1].split('\n')]

def generatePossibilities(rule,rules):
    if '|' in rule:
        return generatePossibilities(rule.split(' | ')[0],rules)+generatePossibilities(rule.split(' | ')[1],rules)
    elif rule in ['"a"','"b"']:
        return [rule[1]]
    else:
        return generateComb(*[generatePossibilities(rules[singleRule],rules) for singleRule in rule.split(' ')])

def generateComb(*lists):
    result = [""]
    for li in lists:
        result = [cur+item for cur in result for item in li]
    return result

def countValidMessages1(messages, possibilities):
    return sum([1 if message in possibilities else 0 for message in messages])

def countValidMessages2(messages,rules):
    count = 0
    possibilities42 = generatePossibilities(rules['42'],rules)
    possibilities31 = generatePossibilities(rules['31'],rules)
    for message in messages:
        count42 =0
        count31 =0
        firstHalf = True
        for i in range(0,len(message),len(possibilities42[0])):
            part = message[i:i+len(possibilities42[0])]
            if part in possibilities42 and firstHalf:
                count42+=1
            elif part in possibilities31:
                count31+=1
                firstHalf = False
            else:
                break
        if i == len(message)-len(possibilities42[0]) and count42>count31 and count31>0:
            count+=1
    return count


if __name__ == '__main__':
    rules, messages = loadRules("input.txt")
    print("Part1", countValidMessages1(messages,generatePossibilities(rules['0'],rules)))
    print("Part2", countValidMessages2(messages,rules))