import re
import sys, getopt

def checkPasswordSled(low, high, chara, string):
    count = 0
    for i in range(len(string)):
        if string[i]==chara:
            count+=1
    if count>=low and count<=high:
        return True;
    else:
        return False;

def checkPasswordToboggan(low, high, chara, string):
    char1 = string[low-1]
    char2 = string[high-1]
    return (char1==chara)!=(char2==chara)


def countValidPassword(data,method):
    count = 0
    for row in data:
        if(method=="sled"):
            result = checkPasswordSled(row[0], row[1],row[2],row[3])
        else:
            result = checkPasswordToboggan(row[0], row[1],row[2],row[3])
        if result:
            count+=1
    return count

def processRawData(location):
    text = open(location)
    lines = text.readlines()
    text.close()
    processedData = []
    for line in lines:
        words = re.split(' |-|: ',line)
        processedData.append([int(words[0]), int(words[1]), words[2],words[3]])
    return processedData

if __name__ =="__main__":
    data = processRawData("input.txt")
    method = ''
    opts, args = getopt.getopt(sys.argv[1:],"hm:",["method="])

    for opt, arg in opts:
        if opt in ("-m", "--method"):
            method = arg
    if not method in ("sled", "toboggan"):
        raise getopt.GetoptError("please input method name, sled or toboggan, following -m")

    count = countValidPassword(data,method)

    print("valid count with ",method, ":", count)
