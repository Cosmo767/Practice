        
def find_duplicate(nums):
        # sum_nums = sum(nums)
        # sum_unique = sum(list(range(1,len(nums))))
        # print(sum_nums, sum_unique)
        # return sum_nums - sum_unique
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                print("nums", i , "is", nums[i], "and nums", j, "is" , nums[j])
                if nums[i] == nums[j]:
                    return nums[i]
                    break
                else:
                    pass 


print(find_duplicate([3,1,3,4,2]))



