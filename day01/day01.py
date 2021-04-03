def twoSum(nums,target):
    visitedNums= set()
    for num in nums:
        if(target-num) in visitedNums:
            return num,target-num
        else:
            visitedNums.add(num)
    return None

def threeSum(nums, target):
    nums.sort()
    for i in range(len(nums)-2):
        sums = target-nums[i]
        low = i+1
        high = len(nums)-1

        while(low<high):
            if(nums[low]+nums[high]==sums):
                return nums[i], nums[low], nums[high]
            elif nums[low]+nums[high]<sums:
                low+=1
            else:
                high-=1
    return None

if __name__ == "__main__":
    text = open("input.txt")
    lines = text.readlines()
    nums = list(map(int, lines))
    text.close()
    #numOne,numTwo = twoSum(nums,2020)
    numOne, numTwo, numThree = threeSum(nums, 2020)
    #print(numOne*numTwo)
    print(numOne*numTwo*numThree)

