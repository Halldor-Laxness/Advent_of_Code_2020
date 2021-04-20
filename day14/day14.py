def loadData(path:str):
    text = open(path)
    lines = text.readlines()
    text.close()
    return lines

def applyMaskOnAddress(num,mask):
    numStr="{0:0>36b}".format(num)
    return int("".join([mask[i] if mask[i]!='X' else numStr[i] for i in range(len(numStr))]),2)

def applyMaskOnKey(num, mask):
    numStr = "{0:0>36b}".format(num)
    result = []
    applyMaskOnKeyHelper(numStr,mask,"",0,result)
    return result

def applyMaskOnKeyHelper(num,mask,curStr,loc,result):
    if loc==len(num) :
        result.append(int(curStr,2))
        return
    if mask[loc]=="1":
        applyMaskOnKeyHelper(num,mask,curStr+"1",loc+1,result)
    elif mask[loc]=="0":
        applyMaskOnKeyHelper(num,mask,curStr+num[loc],loc+1,result)
    elif mask[loc]=='X':
        applyMaskOnKeyHelper(num,mask,curStr+"1",loc+1,result)
        applyMaskOnKeyHelper(num,mask,curStr+"0",loc+1,result)


def batchProcessData(data,maskOnAddress = True):
    result = {}
    mask = "X"*36;
    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            key = int(''.join(list(filter(str.isdigit, line.split(" = ")[0]))))
            num = int(line.split(" = ")[1])
            if maskOnAddress:
                result[key] = applyMaskOnAddress(num,mask)
            else:
                for idx in applyMaskOnKey(key,mask):
                    result[idx] = num

    return sum(result.values())

if __name__=="__main__":
    data = loadData("input.txt")
    print("Part 1:",batchProcessData(data))
    print("Part 2:",batchProcessData(data,False))
