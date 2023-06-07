import sys

def task():
    f = open(sys.argv[1], 'r')
    data = f.read().split('\n')
    f.close
    nums = [int(item) for item in data]
    nums.sort()
    if len(nums)%2 == 0:
        median = (nums[int(len(nums)/2 - 1)] + nums[int(len(nums)/2)])/2
    else:
        median = nums[int(len(nums)/2)]
    steps = []
    for item in nums:
        steps.append(abs(item - int(median)))
    return sum(steps) 

print(task())
