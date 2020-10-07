# # # log 2 n = i 
import math as m


# def isPowerOfTwo(n):
#     if n ==0:
#         return True
#     else:
#         i=0
#         rounded_log = round(m.log(n,2),10)
#         print(rounded_log)
#         while i <= rounded_log:
#             if rounded_log == i:
#                 print(i)
#                 return True
#             else: i += 1 
#         if i > m.log(n,2):
#             return False
#         else:
#             pass

# (isPowerOfTwo(n=4194303))

# print((m.log(4194303,2)))

def findDisappearedNumbers(nums):
    nums_set = set(nums)
    complete_set = set((range(1 , len(nums)+1)))
    diff_set = complete_set.difference(nums_set)
    
    return list(diff_set)
    '''
    Below is an iterative approuch
    '''
    # set_nums = set(nums)
    # n = len(nums)
    # output = []
    # print(n)
    # for i in range(1,n+1):
        
    #     if i in nums:
            
    #         pass
    #     else: 
            
    #         output.append(i)
    # return output

print(findDisappearedNumbers([1,1]))


