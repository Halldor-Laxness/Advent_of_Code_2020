def loadData(path):
    with open(path, "r") as file:
        data = file.readlines()
    return [line.replace(' ','') for line in data]

def executeOpsWithoutPrecedence(opt):
    operations = {'+':(lambda x,y:x+y),'*':(lambda x,y:x*y) }
    num = opt[0]
    operator = None
    for item in opt[1:]:
        if item=='+' or item=='*':
            operator= item
        else:
            num = operations[operator](num,item)
    return num

def executeOpsWithPrecedence(opts):
    while('+' in opts):
        idx = opts.index('+')
        num = opts[idx-1]+opts[idx+1]
        opts.pop(idx-1)
        opts.pop(idx-1)
        opts[idx-1] = num
    return executeOpsWithoutPrecedence(opts)

def calculate(inp, method):
    inp = [int(inp[i]) if inp[i].isdigit() else inp[i] for i in range(len(inp))]
    expressionStack =[]
    expression = []
    for i in range(len(inp)):
        char = inp[i]
        if char == '(':
            expressionStack.append(expression)
            expression=[]
        elif char ==')':
            poped = expressionStack.pop()
            if poped ==None:
                expresion = [method(expression)]
            else:
                poped.append(method(expression))
                expression=poped
        else:
            expression.append(char)
    return method(expression)

def sumExpressions(data, method):
    return sum([calculate(line.replace('\n',''),method) for line in data])

if __name__ == "__main__":
    data = loadData("input.txt")
    print("part 1:",sumExpressions(data,executeOpsWithoutPrecedence))
    print("part 2:",sumExpressions(data,executeOpsWithPrecedence))

