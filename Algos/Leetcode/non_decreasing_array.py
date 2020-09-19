'''

Given an array nums with n integers, your task is to check 
if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing 
if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
'''


'''
print( "TEST", 2<=3 & 3<=4)

def check(nums):
    counter=1
    for i in range(len(nums)-1):
        if ((nums[i] <= nums[i+1]) & (nums[i] <= nums[i+2])):
            counter = counter + 1
            print(counter, "yes")
        else:
            counter = counter
            print(counter, "no")
    if (counter + 1 >= len(nums)):
        return(True) 
    else: 
        return(False)
'''
'''
def check(nums): 
        change = 0
        a = nums
        b = nums
        t = 0 
        while t < 1:
            for i in range(len(a)-1):
                if a[i] <= a[i+1]:
                    print("a")
                    print(a)
                    print(change)
                    True
                else:
                
                    a[i+1] = a[i]
                    change = change+1
                    print("a")
                    print(a)
                    print(change)
                    print("nums")
                    print(nums)

            change_two = 0
            print("b pre")
            print(b)
            print("nums")
            print(nums)
            for j in range(len(b)-1):
                if b[j] <= b[j+1]:
                    True
                    print("b")
                    print(b)
                    print(change_two)
                else:
                    diff = b[j] - b[j+1]
                    b = [x + diff for x in b]
                    change_two = change_two + 1
                    print("b")
                    print(b)
                    print(change_two)
                t = t +1

        print(change, "change")
        print(change_two, "change two")
        if change < 2 or change_two < 2:
            return(True)
        else:
            return(False)
   
'''
'''
def check(nums):
    max = nums[0]
    bad = 0
    for i in range(len(nums)-1):
            if nums[i] < max:
                bad = bad + 1
                if bad == 2: break
            else:
                max = nums[i]
    return bad
            
'''

def check(nums):
    new_array_max_delete = nums.copy()
    new_array_min_delete = nums.copy()
    # check if there is one decrease and delete max into new array max
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            new_array_max_delete.pop(i)
            print("new array max")
            print(new_array_max_delete)
            print("for i =", i)
            new_array_min_delete.pop(i+1)
            print("new array min")
            print(new_array_min_delete)
            print("for i =", i)
            break
        else:
            print("new array max")
            print(new_array_max_delete)
            print("for i =", i)
            print("new array min")
            print(new_array_min_delete)
            print("for i =", i)
    
    #check if new array is strictly monotonic now
    def monotonic(new_array):
        x = 0
        for i in range(len(new_array)-1):
            if new_array[i] <= new_array[i+1]:
                x = x+1
            else: 
                x = x
        if x == len(new_array)-1: 
            return(True)
        else: return(False)
    
    x = monotonic(new_array_max_delete)
    y = monotonic(new_array_min_delete)
    print(x)
    print(y)

    return(x or y)





x = [4,5,2,5]
y= [7,8,9,1,2,3]
z= [7,8,9,10,1,2,3,4]

k =[4,2,3]
print(check(y))
