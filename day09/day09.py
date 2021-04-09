from typing import List
def processRawData(location):
    text = open(location)
    lines = text.readlines()
    lines = [int(line)  for line in lines]
    text.close()
    return lines

def findFirstInvalidXmas( nums:List[int], premeableSize:int)->int:
    for i in range(premeableSize,len(nums)):
        if not checkTwoSum(nums[i-premeableSize:i],nums[i]):
            return nums[i]
    return -1

def checkTwoSum(nums:List[int], target:int)->bool:
    visitedNums= set()
    for num in nums:
        if(target-num) in visitedNums:
            return True
        else:
            visitedNums.add(num)
    return False

def findSubarrayOfValue(nums:List[int], target:int)->List[int]:
    sums = 0
    sumsIdx = dict();
    for i in range(len(nums)):
        sums+=nums[i]
        if (sums - target) in sumsIdx and i - sumsIdx[sums-target] >1:
            return nums[sumsIdx[sums-target]+1:i+1]
        else:
            sumsIdx[sums]= i
    return []

def sumMinAndmax(nums:List[int])->int:
    return min(nums)+max(nums)


if __name__ == "__main__":
    data = processRawData("input.txt")
    firstInvalidNum = findFirstInvalidXmas(data, 25)
    print("Part 1:",firstInvalidNum)
    numsSubList = findSubarrayOfValue(data, firstInvalidNum)
    print("Part 2:", sumMinAndmax(numsSubList))



