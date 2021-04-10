from collections import defaultdict

def processRawData(location):
    text = open(location)
    lines = text.readlines()
    text.close()
    lines = [int(line) for line in lines]
    return lines

def countDifference(nums, targetDif):
    nums.sort()
    count = defaultdict(lambda:0)
    count[nums[0]]+=1
    for i in range(len(nums)-1):
        dif = nums[i+1]-nums[i]
        count[dif] +=1
    count[3]+=1
    return count[targetDif]

def countCombs(nums):
    nums.sort()
    target = nums[-1]
    # dp[x] = dp[x-3]+dp[x-2]+dp[x-1] if x in nums
    #       = 0 if x not in nums
    dp = [0]*(target+1)
    dp[0] = 1
    dp[1] = 1 if 1 in nums else 0
    dp[2] = dp[1]+dp[0] if 2 in nums else 0
    for i in range (3, target+1):
        if i in nums:
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
    return dp[target]

if __name__ == "__main__":
    data = processRawData("input.txt")
    print("Part 1:",countDifference(data,1)*countDifference(data,3))
    print("Part 2:", countCombs(data))
