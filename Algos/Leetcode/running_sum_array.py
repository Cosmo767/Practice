#Given an array nums. We define a 
# running sum of an array as 
# runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums.

''' takes an array and creates a new array such that the nth term 
    in the new array is the sum of the first nths terms in the
    original array '''

def running_sum(nums):
    
    ''' set running_sum = 0, add'''
    new_nums = []
    running_total = 0 
    for i in range(len(nums)):

        new_nums.append(nums[i] + running_total)
        running_total =  nums[i] + running_total
    return new_nums

print(running_sum([5,2,10,0,100]))